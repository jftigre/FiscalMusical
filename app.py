import os
from flask import Flask, request, session, redirect, url_for
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv("FLASK_SECRET_KEY", "chave_padrao_para_desenvolvimento")
app.config['SESSION_COOKIE_NAME'] = 'cookie_do_fiscal'

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
        
    return "<h1>Sucesso!</h1><p>Você está logado. O back-end já tem o seu Token de Acesso do Spotify.</p>"

@app.route('/top_artists')
def top_artists():
    token_info = session.get("token_info")
    
    if not token_info:
        return redirect(url_for('login'))
    
    sp = spotipy.Spotify(auth=token_info['access_token'])
    top_artists_data = sp.current_user_top_artists(limit=5, time_range='short_term')
    
    nomes_artistas = [artista['name'] for artista in top_artists_data['items']]
    artistas_str = ", ".join(nomes_artistas)
    
    return f"<h1>Seus Top 5 Artistas:</h1><p>{artistas_str}</p>"

if __name__ == '__main__':
    app.run(debug=True, port=5000)