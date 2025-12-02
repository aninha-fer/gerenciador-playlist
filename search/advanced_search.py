import os

# Get the directory of this file
current_dir = os.path.dirname(__file__)

# Execute the search files
exec(open(os.path.join(current_dir, 'linear-search.py')).read())
exec(open(os.path.join(current_dir, 'binary-search.py')).read())

def search_music_by_name(musicas, termo):
    """Busca música por nome usando busca linear"""
    nomes = []
    for musica in musicas:
        if isinstance(musica, dict):
            nomes.append(musica['nome'].lower())
        else:
            nomes.append(musica.nome.lower())
    
    # Busca exata primeiro
    indice = linear_search(nomes, termo.lower())
    if indice != -1:
        return [indice]
    
    # Busca parcial se não encontrar exata
    indices = []
    for i, nome in enumerate(nomes):
        if termo.lower() in nome:
            indices.append(i)
    
    return indices

def search_music_by_artist(musicas, termo):
    """Busca música por artista usando busca linear"""
    artistas = []
    for musica in musicas:
        if isinstance(musica, dict):
            artistas.append(musica['cantor'].lower())
        else:
            artistas.append(musica.cantor.lower())
    
    indices = []
    for i, artista in enumerate(artistas):
        if termo.lower() in artista:
            indices.append(i)
    
    return indices

def search_music_by_genre(musicas, termo):
    """Busca música por gênero usando busca linear"""
    generos = []
    for musica in musicas:
        if isinstance(musica, dict):
            generos.append(musica['genero'].lower())
        else:
            generos.append(musica.genero.lower())
    
    indices = []
    for i, genero in enumerate(generos):
        if termo.lower() in genero:
            indices.append(i)
    
    return indices

def advanced_search(musicas, termo):
    """Busca avançada que procura em nome, artista e gênero"""
    resultados = set()
    
    # Busca por nome
    resultados.update(search_music_by_name(musicas, termo))
    
    # Busca por artista
    resultados.update(search_music_by_artist(musicas, termo))
    
    # Busca por gênero
    resultados.update(search_music_by_genre(musicas, termo))
    
    return list(resultados)