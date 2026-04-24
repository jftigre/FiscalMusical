import os
from flask import Flask, request, session, redirect, url_for, render_template
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv
from google import genai 

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv("FLASK_SECRET_KEY", "chave_padrao_para_desenvolvimento")
app.config['SESSION_COOKIE_NAME'] = 'cookie_do_fiscal'

gemini_client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

sp_oauth = SpotifyOAuth(
    client_id=os.getenv("SPOTIPY_CLIENT_ID"),
    client_secret=os.getenv("SPOTIPY_CLIENT_SECRET"),
    redirect_uri=os.getenv("SPOTIPY_REDIRECT_URI"),
    scope="user-top-read" 
)

@app.route('/')
def index():
    return '''
        <h1>Bem-vindo ao Fiscal Musical</h1>
        <p>Descubra o quão questionável é o seu gosto musical.</p>
        <a href="/login"><button>Entrar com Spotify</button></a>
    '''

@app.route('/login')
def login():
    auth_url = sp_oauth.get_authorize_url()
    return redirect(auth_url)

@app.route('/callback')
def callback():
    session.clear()
    code = request.args.get('code')
    try:
        token_info = sp_oauth.get_access_token(code)
        session["token_info"] = token_info
        return redirect(url_for('analisar'))
    except Exception as e:
        return f"<h1>Erro na Autenticação</h1><p>{e}</p>"

@app.route('/analisar')
def analisar():
    token_info = session.get("token_info")
    if not token_info:
        return redirect(url_for('login'))
        
    try:
        sp = spotipy.Spotify(auth=token_info['access_token'])
        top_artists_data = sp.current_user_top_artists(limit=5, time_range='short_term')
        
        nomes_artistas = [artista['name'] for artista in top_artists_data['items']]
        artistas_str = ", ".join(nomes_artistas)
        
        if not nomes_artistas:
            return "<h1>Hmm...</h1><p>Você não ouviu música suficiente nas últimas semanas.</p>"

        prompt_sistema = f"Você é um crítico musical insuportável e sarcástico. O usuário tem o seguinte top 5 de artistas mais ouvidos: {artistas_str}. Escreva um laudo de um parágrafo tirando sarro brutalmente do gosto dele. Vá direto ao ponto."
        
        resposta_ia = gemini_client.models.generate_content(
            model='gemini-2.5-flash',
            contents=prompt_sistema
        )
        
        return render_template('index.html', artistas=artistas_str, laudo=resposta_ia.text)

    except Exception as e:
        return f"<h1>Erro na Análise</h1><p>Detalhes: {e}</p>"

if __name__ == '__main__':
    app.run(debug=True, port=5000)