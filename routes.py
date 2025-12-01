from main import app
from flask import render_template, redirect, url_for, session
from musicas import musicas_para_projeto
from structs.hash_table import HashTable
from structs.stack import Stack
from structs.queue import Queue
import traceback 

# Inicializa a Hash Table com índice de músicas
musica_hash_table = HashTable(size=100)
for i, musica in enumerate(musicas_para_projeto):
    # Normaliza o nome da música para a chave
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

# Inicializa a fila de reprodução (Queue)
music_queue = Queue()

# Inicializa a pilha de músicas puladas (Stack)
skipped_stack = Stack()

@app.before_request
def init_session():
    # Sessão agora apenas marca que está inicializada
    if 'queue_initialized' not in session:
        session['queue_initialized'] = True

@app.route("/")
def home():
    # Converte a fila para array para exibir
    playlist = music_queue.to_array() if hasattr(music_queue, 'to_array') else []
    
    # Converte objetos/dicts para dicts se necessário
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
    """Busca rápida usando Hash Table - O(1)"""
    global music_queue
    termo = termo.lower().strip()
    print(f"\n=== BUSCAR MÚSICA ===")
    print(f"Termo buscado: '{termo}'")
    
    # Busca exata na Hash Table usando .get()
    resultado = musica_hash_table.get(termo)
    
    if resultado:
        indice, musica = resultado
        
        # Converte para dict se for objeto
        if isinstance(musica, dict):
            musica_dict = musica
        else:
            musica_dict = {
                'nome': musica.nome,
                'cantor': musica.cantor,
                'genero': musica.genero,
                'duracao': musica.duracao
            }
        
        print(f"✓ Música encontrada: {musica_dict['nome']} (índice: {indice})")
        music_queue.enqueue(musica_dict)
    else:
        # Se não encontrar exato, busca parcial (O(n) fallback)
        print(f"✗ Busca exata não encontrou. Tentando busca parcial...")
        encontrou = False
        for i, musica in enumerate(musicas_para_projeto):
            nome_musica = musica['nome'].lower() if isinstance(musica, dict) else musica.nome.lower()
            if termo in nome_musica:
                musica_dict = musica if isinstance(musica, dict) else {
                    'nome': musica.nome,
                    'cantor': musica.cantor,
                    'genero': musica.genero,
                    'duracao': musica.duracao
                }
                print(f"✓ Música encontrada (busca parcial): {musica_dict['nome']}")
                music_queue.enqueue(musica_dict)
                encontrou = True
                break
        
        if not encontrou:
            print(f"✗ Nenhuma música encontrada com '{termo}'")
    
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
            
            # Converte para dict se for objeto
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
    
    # Remove a primeira música da fila (dequeue) e adiciona à pilha
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
        # 1. Verifica a Pilha
        if skipped_stack.is_empty():
            print(f"✗ Pilha vazia, nada para voltar.")
            return redirect(url_for('home'))

        # 2. Tenta tirar da Pilha (Se a Stack tiver erro, vai estourar aqui)
        musica_anterior = skipped_stack.pop()
        print(f"✓ Música recuperada da pilha: {musica_anterior['nome'] if isinstance(musica_anterior, dict) else musica_anterior.nome}")
        
        # 3. Faz o Backup da Fila atual
        # Como vimos que sua classe Queue TEM to_array, podemos usar com segurança!
        items_na_fila = music_queue.to_array()
        print(f"✓ Backup da fila feito. {len(items_na_fila)} itens salvos.")
        
        # 4. Limpa a Fila
        music_queue.clear() # Se sua classe Queue tiver clear(), use. Se não, use o loop abaixo:
        # while not music_queue.is_empty():
        #     music_queue.dequeue()
        
        # 5. Reconstrói: Primeiro a antiga, depois o resto
        music_queue.enqueue(musica_anterior)
        for musica in items_na_fila:
            music_queue.enqueue(musica)
            
        print(f"✓ Sucesso! Fila reconstruída.")
        return redirect(url_for('home'))

    except Exception as e:
        # AQUI ESTÁ O SEGREDO: Em vez de Tela de Erro 500, ele imprime o erro no terminal
        print("🔴 ERRO GRAVE NO /VOLTAR:")
        print(traceback.format_exc()) # Isso mostra exatamente a linha que quebrou
        return "Erro interno no servidor (veja o terminal)", 500