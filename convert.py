import glob


def Ler_arquivos(file_list):
    for file in file_list:
        with open(file, 'r') as fd:
            yield fd.read()


def Juntar_arquivos(file_list, filename='tarot.json'):
    with open(filename, 'w') as f:
        i=0
        f.write('\'{"data":[ ')
        for descricao in Ler_arquivos(file_list):
            print(file_list)
            nome = file_list[i].split('.md')[0].split('\\')
            livro = nome[1]
            cartacompleta = nome[2].split('-')
            carta = cartacompleta[1]
            numero_carta = cartacompleta[0]
            virgula =','

            if(i == (len(file_list) - 1)):
                virgula = ''

            f.write('{ "livro": "%s", "id": "%s", "nome_carta": "%s", "dados": "%s"}%s' % (livro, numero_carta, carta, descricao, virgula))

            i=i+1
        f.write(']}\'')


files = glob.glob("cartas/*/*.md")

Juntar_arquivos(files)
