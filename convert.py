import os
import json

# Função para extrair o ID e o nome do arquivo
def extrair_informacoes(nome_arquivo):
    partes = nome_arquivo.split('_')
    id = partes[0]
    nome = '_'.join(partes[1:]).replace('.md', '')
    return id, nome

# Função para ler o conteúdo do arquivo
def ler_conteudo_arquivo(caminho):
    with open(caminho, 'r', encoding='utf-8') as arquivo:
        return arquivo.read()

# Estrutura para armazenar os dados
estrutura_json = []

# Caminho para a pasta 'cartas'
caminho_base = 'cartas/'

# Percorre os diretórios e arquivos
for indice, (diretorio, _, arquivos) in enumerate(os.walk(caminho_base)):
    indice -=1
    nome_diretorio = os.path.basename(diretorio)
    if nome_diretorio not in estrutura_json:
        dados_livro = nome_diretorio.split('-')
        if(len(dados_livro) > 1):
            nome_livro = dados_livro[0].strip()
            nome_autor = dados_livro[1].strip()
        else:
            nome_livro = "vazio_livro"
            nome_autor = "vazio_autor"
        if nome_diretorio != '':
            estrutura_json.append({"id":indice, "livro": nome_livro,"autor": nome_autor, "dados": []})
   

    # Atualize o índice aqui (se necessário)
    if nome_diretorio != '':
        index = len(estrutura_json) -1
        for arquivo in arquivos:
            if arquivo.endswith('.md'):
                caminho_completo = os.path.join(diretorio, arquivo)
                id, nome = extrair_informacoes(arquivo)
                conteudo = ler_conteudo_arquivo(caminho_completo)
                estrutura_json[index]['dados'].append({
                    'id': int(id),
                    'nome': nome,
                    'dados': conteudo
                })

for item in estrutura_json:
    item["dados"].sort(key=lambda x: x["id"])

    import random
    random_number = random.randint(1000000000, 9999999999)
    versao = '{"versao":'+str(random_number)+'}'

with open(os.path.join('api/versao2.json'), 'w', encoding='utf-8') as file:
    file.write(versao)

# Converte a estrutura para JSON e salva em um arquivo
with open('api/tarot2.json', 'w', encoding='utf-8') as saida_json:
    json.dump(estrutura_json, saida_json, ensure_ascii=False, indent=4)