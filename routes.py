from main import app
from flask import render_template, redirect, url_for, session
from musicas import musicas_para_projeto
from structs.hash_table import HashTable
from structs.stack import Stack
from structs.queue import Queue
import traceback
from search.linear_search import linear_search
from sort.bubble_sort import bubble_sort
from search.advanced_search import advanced_search
from sort.shuffle_sort import fisher_yates_shuffle 

musica_hash_table = HashTable(size=100)
for i, musica in enumerate(musicas_para_projeto):
    if isinstance(musica, dict):
        chave = musica['nome'].lower().strip()
        musica_hash_table.set(chave, (i, musica))
    else:
        chave = musica.nome.lower().strip()
        musica_dict = {
            'nome': musica.nome,
            'cantor': musica.cantor,
            'genero': musica.genero,
            'duracao': musica.duracao
        }
        musica_hash_table.set(chave, (i, musica_dict))

music_queue = Queue()

skipped_stack = Stack()

@app.before_request
def init_session():
    if 'queue_initialized' not in session:
        session['queue_initialized'] = True

@app.route("/")
def home():
    playlist = music_queue.to_array() if hasattr(music_queue, 'to_array') else []

    recomendadas = []
    for musica in musicas_para_projeto[10:15]:
        if isinstance(musica, dict):
            recomendadas.append(musica)
        else:
            recomendadas.append({
                'nome': musica.nome,
                'cantor': musica.cantor,
                'genero': musica.genero,
                'duracao': musica.duracao
            })
    
    skipped_count = len(skipped_stack.to_array()) if hasattr(skipped_stack, 'to_array') else 0
    return render_template("home.html", playlist=playlist, recomendadas=recomendadas, skipped_count=skipped_count)

@app.route("/test")
def test():
    return f"Total de músicas: {len(musicas_para_projeto)}"

@app.route("/buscar/<termo>")
def buscar_musica(termo):
    """Busca usando algoritmos de busca implementados"""
    global music_queue
    termo = termo.strip()
    
    resultado = musica_hash_table.get(termo.lower())
    if resultado:
        indice, musica = resultado
        musica_dict = musica if isinstance(musica, dict) else {
            'nome': musica.nome, 'cantor': musica.cantor,
            'genero': musica.genero, 'duracao': musica.duracao
        }
        music_queue.enqueue(musica_dict)
        return redirect(url_for('home'))
    
    indices = advanced_search(musicas_para_projeto, termo)
    
    for i, indice in enumerate(indices[:3]):
        musica = musicas_para_projeto[indice]
        musica_dict = musica if isinstance(musica, dict) else {
            'nome': musica.nome, 'cantor': musica.cantor,
            'genero': musica.genero, 'duracao': musica.duracao
        }
        music_queue.enqueue(musica_dict)
    
    return redirect(url_for('home'))

@app.route("/adicionar/<musica_id>")
def adicionar_musica(musica_id):
    global music_queue
    print(f"\n=== ADICIONAR MÚSICA ===")
    print(f"musica_id recebido: {musica_id} (tipo: {type(musica_id)})")
    
    try:
        musica_id = int(musica_id)
        print(f"musica_id convertido: {musica_id}")
        print(f"Total de músicas: {len(musicas_para_projeto)}")
        
        if 0 <= musica_id < len(musicas_para_projeto):
            musica = musicas_para_projeto[musica_id]
            
            if isinstance(musica, dict):
                musica_dict = musica
            else:
                musica_dict = {
                    'nome': musica.nome,
                    'cantor': musica.cantor,
                    'genero': musica.genero,
                    'duracao': musica.duracao
                }
            
            print(f"✓ Música encontrada: {musica_dict['nome']}")
            music_queue.enqueue(musica_dict)
            print(f"Fila agora tem {len(music_queue.to_array())} músicas")
        else:
            print(f"✗ ID {musica_id} fora do intervalo [0, {len(musicas_para_projeto)})")
    except ValueError as e:
        print(f"✗ Erro ao converter para int: {e}")
    except Exception as e:
        print(f"✗ Erro: {e}")
    
    return redirect(url_for('home'))

@app.route("/pular", methods=['POST'])
def pular_musica():
    global music_queue, skipped_stack
    print(f"\n=== PULAR MÚSICA ===")
    
    if not music_queue.is_empty():
        musica_pulada = music_queue.dequeue()
        skipped_stack.push(musica_pulada)
        print(f"✓ Música pulada: {musica_pulada['nome']}")
        print(f"Fila: {len(music_queue.to_array())} | Pilha de puladas: {len(skipped_stack.to_array())}")
    else:
        print(f"✗ Fila vazia, nada a pular")
    
    return redirect(url_for('home'))

@app.route("/voltar", methods=['POST'])
def voltar_musica():
    global music_queue, skipped_stack
    print(f"\n=== VOLTAR MÚSICA (Debug Mode) ===")
    
    try:
        if skipped_stack.is_empty():
            print(f"✗ Pilha vazia, nada para voltar.")
            return redirect(url_for('home'))

        musica_anterior = skipped_stack.pop()
        print(f"✓ Música recuperada da pilha: {musica_anterior['nome'] if isinstance(musica_anterior, dict) else musica_anterior.nome}")
        
        items_na_fila = music_queue.to_array()
        print(f"✓ Backup da fila feito. {len(items_na_fila)} itens salvos.")

        music_queue.clear()
        
        music_queue.enqueue(musica_anterior)
        for musica in items_na_fila:
            music_queue.enqueue(musica)
            
        print(f"✓ Sucesso! Fila reconstruída.")
        return redirect(url_for('home'))

    except Exception as e:
        print("ERRO GRAVE NO /VOLTAR:")
        print(traceback.format_exc())
        return "Erro interno no servidor (veja o terminal)", 500

@app.route("/shuffle", methods=['POST'])
def shuffle_playlist():
    global music_queue
    
    if music_queue.is_empty():
        return redirect(url_for('home'))
    
    items = music_queue.to_array()
    
    shuffled_items = fisher_yates_shuffle(items)

    music_queue.clear()
    for item in shuffled_items:
        music_queue.enqueue(item)
    
    return redirect(url_for('home'))