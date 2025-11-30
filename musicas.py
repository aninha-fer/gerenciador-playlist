# Lista de 50 músicas famosas e variadas para projeto em Python

# Definição da classe Musica
class Musica:
    def __init__(self, nome, cantor, genero, duracao):
        self.nome = nome
        self.cantor = cantor
        self.genero = genero
        self.duracao = duracao

# Lista de músicas utilizando a classe Musica
musicas_para_projeto = [
    # POP / DANCE
    Musica("Blinding Lights", "The Weeknd", "Pop / Synthwave", "03:20"),
    Musica("Shape of You", "Ed Sheeran", "Pop", "03:53"),
    Musica("Uptown Funk", "Mark Ronson ft. Bruno Mars", "Funk Pop", "04:30"),
    Musica("Rolling in the Deep", "Adele", "Soul Pop", "03:48"),
    Musica("Levitating", "Dua Lipa", "Disco Pop", "03:23"),
    Musica("Watermelon Sugar", "Harry Styles", "Pop Rock", "02:54"),
    Musica("Happier Than Ever", "Billie Eilish", "Indie Pop", "04:58"),
    Musica("Bad Guy", "Billie Eilish", "Electropop", "03:14"),
    Musica("Get Lucky", "Daft Punk ft. Pharrell Williams", "Funk / Dance", "04:08"),
    Musica("Mr. Brightside", "The Killers", "Indie Rock", "03:42"),
    
    # ROCK
    Musica("Bohemian Rhapsody", "Queen", "Classic Rock", "05:55"),
    Musica("Smells Like Teen Spirit", "Nirvana", "Grunge", "05:01"),
    Musica("Sweet Child o' Mine", "Guns N' Roses", "Hard Rock", "05:56"),
    Musica("Stairway to Heaven", "Led Zeppelin", "Folk Rock", "08:02"),
    Musica("Hey Jude", "The Beatles", "Pop Rock", "07:11"),
    Musica("Imagine", "John Lennon", "Soft Rock", "03:04"),
    Musica("Back in Black", "AC/DC", "Hard Rock", "04:15"),
    Musica("Seven Nation Army", "The White Stripes", "Garage Rock", "03:52"),
    Musica("Livin' on a Prayer", "Bon Jovi", "Glam Metal", "04:09"),
    Musica("Californication", "Red Hot Chili Peppers", "Alternative Rock", "05:29"),
    
    # HIP-HOP / R&B
    Musica("Lose Yourself", "Eminem", "Hip Hop", "05:26"),
    Musica("Crazy in Love", "Beyoncé ft. Jay-Z", "R&B / Pop", "03:56"),
    Musica("Hotline Bling", "Drake", "Hip Hop / R&B", "04:31"),
    Musica("Humble", "Kendrick Lamar", "Hip Hop", "02:57"),
    Musica("Empire State of Mind", "Jay-Z ft. Alicia Keys", "Hip Hop", "04:36"),
    Musica("No Scrubs", "TLC", "R&B", "03:34"),
    Musica("Old Town Road", "Lil Nas X ft. Billy Ray Cyrus", "Country Trap", "02:37"),
    Musica("Mo Money Mo Problems", "The Notorious B.I.G.", "Hip Hop", "04:31"),
    Musica("God's Plan", "Drake", "Hip Hop / Trap", "03:18"),
    Musica("Alright", "Kendrick Lamar", "Conscious Hip Hop", "03:39"),

    # SERTANEJO / FORRÓ / MPB (Brasil)
    Musica("Evidências", "Chitãozinho & Xororó", "Sertanejo", "04:35"),
    Musica("Aquarela do Brasil", "Gal Costa", "MPB / Samba", "03:31"),
    Musica("Garota de Ipanema", "Tom Jobim & Vinícius de Moraes", "Bossa Nova", "02:44"),
    Musica("Cheia de Manias", "Raça Negra", "Samba-Rock / Pagode", "03:33"),
    Musica("Isso Aqui Tá Bom Demais", "Dominguinhos", "Forró", "02:54"),
    Musica("Meu Erro", "Os Paralamas do Sucesso", "Pop Rock Brasileiro", "03:28"),
    Musica("Anna Júlia", "Los Hermanos", "Rock Alternativo Brasileiro", "03:33"),
    Musica("Malandragem", "Cássia Eller", "Pop Rock", "04:12"),
    Musica("Fio de Cabelo", "Chitãozinho & Xororó", "Sertanejo Raiz", "02:45"),
    Musica("As Rosas Não Falam", "Cartola", "Samba", "03:00"),

    # LATINAS / REGGAETON / OUTROS
    Musica("Despacito", "Luis Fonsi ft. Daddy Yankee", "Reggaeton / Latin Pop", "03:49"),
    Musica("Vivir Mi Vida", "Marc Anthony", "Salsa", "04:12"),
    Musica("Gasolina", "Daddy Yankee", "Reggaeton", "03:12"),
    Musica("Havana", "Camila Cabello ft. Young Thug", "Latin Pop", "03:37"),
    Musica("Africa", "Toto", "Soft Rock", "04:55"),
    Musica("A Thousand Miles", "Vanessa Carlton", "Pop", "03:57"),
    Musica("Don't Stop Believin'", "Journey", "Arena Rock", "04:10"),
    Musica("The Chain", "Fleetwood Mac", "Classic Rock", "04:30"),
    Musica("One Dance", "Drake ft. Wizkid & Kyla", "Dancehall / Afrobeat", "02:54"),
    Musica("Thriller", "Michael Jackson", "Pop / Funk", "05:57")
]

# Exemplo de como você pode usar a lista em outro arquivo Python:
# from musicas import musicas_para_projeto
# print(f"Total de músicas: {len(musicas_para_projeto)}")
# print(musicas_para_projeto[0]['nome'])