from main import app
from flask import render_template
from musicas import musicas_para_projeto

@app.route("/")
def home():
    return render_template("home.html", musicas=musicas_para_projeto)
