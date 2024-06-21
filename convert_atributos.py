import os
import json

# Função para extrair o ID e o nome do arquivo
def extrair_informacoes(nome_arquivo):
    partes = nome_arquivo.split('_')
    id = partes[0]
    nome = partes[1]
    tipo = partes[2]
    return id, nome, tipo


# Função para ler o conteúdo do arquivo
def ler_conteudo_arquivo(caminho):
    with open(caminho, 'r', encoding='utf-8') as arquivo:
        return arquivo.read()

# Estrutura para armazenar os dados
estrutura_json = []

# Caminho para a pasta 'cartas'
caminho_base = 'atributos/'



# Percorre os diretórios e arquivos
for diretorio, _, arquivos in os.walk(caminho_base):
    nome_diretorio = os.path.basename(diretorio)
   

    # Atualize o índice aqui (se necessário)
    for arquivo in arquivos:
        if arquivo.endswith('.md'):
            caminho_completo = os.path.join(diretorio, arquivo)
            id, nome, tipo = extrair_informacoes(arquivo)
            conteudo = ler_conteudo_arquivo(caminho_completo)
            estrutura_json.append({
                'id': int(id),
                'nome': nome,
                'tipo': tipo,
                'dados': conteudo
            })


# for item in estrutura_json:
#     item["dados"].sort(key=lambda x: x["id"])

#     import random
#     random_number = random.randint(1000000000, 9999999999)
#     versao = '{"versao":'+str(random_number)+'}'

with open('api/atributos.json', 'w', encoding='utf-8') as saida_json:
    json.dump(estrutura_json, saida_json, ensure_ascii=False, indent=4)