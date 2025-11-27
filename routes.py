from main import app
from flask import render_template
from musicas import musicas_para_projeto

@app.route("/")
def home():
    playlist = musicas_para_projeto[:10]  # Primeiras 10 músicas para a playlist
    recomendadas = musicas_para_projeto[10:]  # Restantes para recomendações
    return render_template("home.html", playlist=playlist, recomendadas=recomendadas)
