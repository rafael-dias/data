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
estrutura_json = {}

# Caminho para a pasta 'cartas'
caminho_base = 'cartas/'

# Percorre os diretórios e arquivos
for diretorio, _, arquivos in os.walk(caminho_base):
    nome_diretorio = os.path.basename(diretorio)
    if nome_diretorio not in estrutura_json:
        
        if nome_diretorio != '':
            estrutura_json[nome_diretorio] = []
    
    for arquivo in arquivos:
        if arquivo.endswith('.md'):
            caminho_completo = os.path.join(diretorio, arquivo)
            id, nome = extrair_informacoes(arquivo)
            conteudo = ler_conteudo_arquivo(caminho_completo)
            estrutura_json[nome_diretorio].append({
                'id': int(id),
                'nome': nome,
                'dados': conteudo
            })

for key in estrutura_json:
    estrutura_json[key].sort(key=lambda x: x['id'])

    import random
    random_number = random.randint(1000000000, 9999999999)
    versao = '{"versao":'+str(random_number)+'}'

with open(os.path.join('api/versao.json'), 'w', encoding='utf-8') as file:
    file.write(versao)

# Converte a estrutura para JSON e salva em um arquivo
with open('api/tarot.json', 'w', encoding='utf-8') as saida_json:
    json.dump(estrutura_json, saida_json, ensure_ascii=False, indent=4)

print('JSON criado com sucesso!')


# with open(os.path.join('api', 'tarot.json'), "w") as file:
#     file.write(json_object)
