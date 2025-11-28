from main import app
from flask import render_template, request, redirect, url_for
from musicas import musicas_para_projeto
from structs.stack import Stack
from structs.queue import Queue

# Inicializa a pilha da playlist
playlist_stack = Stack()
for musica in musicas_para_projeto[:10]:
    playlist_stack.push(musica)

# Inicializa a fila
music_queue = Queue()

@app.route("/")
def home():
    playlist = playlist_stack.to_array()  # Converte pilha para array para exibição
    recomendadas = musicas_para_projeto[10:15]  # Apenas 5 músicas recomendadas
    fila = music_queue.to_array()  # Converte fila para array
    return render_template("home.html", playlist=playlist, recomendadas=recomendadas, fila=fila)

@app.route("/adicionar/<int:musica_id>")
def adicionar_musica(musica_id):
    if 10 <= musica_id < len(musicas_para_projeto):
        musica = musicas_para_projeto[musica_id]
        music_queue.enqueue(musica)
    return redirect(url_for('home'))
