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

        top_tracks_data = sp.current_user_top_tracks(limit=5, time_range='short_term')
        nomes_musicas = [f"{t['name']} ({t['artists'][0]['name']})" for t in top_tracks_data['items']]
        musicas_str = ", ".join(nomes_musicas)
        
        if not nomes_artistas:
            return "<h1>Hmm...</h1><p>Dados insuficientes no Spotify.</p>"

        prompt_sistema = f"""
        Você é o "Fiscal Musical", um crítico brasileiro extremamente sarcástico, ácido e impaciente.
        O usuário ouve estes artistas: {artistas_str}.
        E estas músicas: {musicas_str}.
        Sua tarefa:
        1. Comece com um apelido ofensivo para o gosto do usuário (ex: "O Caso do Cidadão Indeciso").
        2. Escreva o laudo em um parágrafo, dedicando trechos para cada artista e depois outro parágrafo dedicado às músicas
        3. Use um humor que misture referências de 'tiozão do rock' com 'jovem sommelier de indie' e um usuário do Twitter que tem humor de memes
        4. Use negrito (**) em palavras-chave para dar ênfase. 
        5. Seja direto: não passe de 4 ou 5 frases. Termine com uma frase de efeito.
        """
        
        resposta_ia = gemini_client.models.generate_content(
            model='gemini-2.5-flash',
            contents=prompt_sistema
        )
        
        return render_template('resultado.html', 
                               artistas=nomes_artistas, 
                               musicas=nomes_musicas, 
                               laudo=resposta_ia.text)

    except Exception as e:
        return f"<h1>Erro na Análise</h1><p>Detalhes: {e}</p>"

if __name__ == '__main__':
    app.run(debug=True, port=5000)