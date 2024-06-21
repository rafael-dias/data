from pathlib import Path

import re

# Lista de textos para encontrar e substituir
to_find = [
    "Glifo"]
to_replace = [
    "Glifo: "
   
]

# Função para substituir os textos
def replace_text(file_path):
    try:
        # Ler o conteúdo do arquivo
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()

        # Substituir os textos de forma insensível a maiúsculas e minúsculas
        for find, replace in zip(to_find, to_replace):
            content = re.sub(re.escape(find), replace, content, flags=re.IGNORECASE)

        # Escrever o conteúdo modificado de volta para o arquivo
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(content)

        print("Texto substituído com sucesso.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

atributos = [{"id": 0, "nome": "ar", "tipo": "elemento", "dados":""},
{"id": 1, "nome": "agua", "tipo": "elemento", "dados":""},
{"id": 2, "nome": "fogo", "tipo": "elemento", "dados":""},
{"id": 3, "nome": "terra", "tipo": "elemento", "dados":""},
{"id": 4, "nome": "aries", "tipo": "signo", "dados":""},
{"id": 5, "nome": "touro", "tipo": "signo", "dados":""},
{"id": 6, "nome": "gemeos", "tipo": "signo", "dados":""},
{"id": 7, "nome": "cancer", "tipo": "signo", "dados":""},
{"id": 8, "nome": "leao", "tipo": "signo", "dados":""},
{"id": 9, "nome": "virgem", "tipo": "signo", "dados":""},
{"id": 10, "nome": "libra", "tipo": "signo", "dados":""},
{"id": 11, "nome": "escorpiao", "tipo": "signo", "dados":""},
{"id": 12, "nome": "sagitario", "tipo": "signo", "dados":""},
{"id": 13, "nome": "capricornio", "tipo": "signo", "dados":""},
{"id": 14, "nome": "aquario", "tipo": "signo", "dados":""},
{"id": 15, "nome": "peixes", "tipo": "signo", "dados":""},
{"id": 16, "nome": "sol", "tipo": "planeta", "dados":""},
{"id": 17, "nome": "mercurio", "tipo": "planeta", "dados":""},
{"id": 18, "nome": "lua", "tipo": "planeta", "dados":""},
{"id": 19, "nome": "venus", "tipo": "planeta", "dados":""},
{"id": 20, "nome": "jupiter", "tipo": "planeta", "dados":""},
{"id": 21, "nome": "marte", "tipo": "planeta", "dados":""},
{"id": 22, "nome": "saturno", "tipo": "planeta", "dados":""},
{"id": 23, "nome": "numero 1", "tipo": "numero", "dados":""},
{"id": 24, "nome": "numero 2", "tipo": "numero", "dados":""},
{"id": 25, "nome": "numero 3", "tipo": "numero", "dados":""},
{"id": 26, "nome": "numero 4", "tipo": "numero", "dados":""},
{"id": 27, "nome": "numero 5", "tipo": "numero", "dados":""},
{"id": 28, "nome": "numero 6", "tipo": "numero", "dados":""},
{"id": 29, "nome": "numero 7", "tipo": "numero", "dados":""},
{"id": 30, "nome": "numero 8", "tipo": "numero", "dados":""},
{"id": 31, "nome": "numero 9", "tipo": "numero", "dados":""},
{"id": 32, "nome": "numero 10", "tipo": "numero", "dados":""}]

for atr in atributos:
    # Caminho do arquivo a ser modificado
    file_path = "./atributos/"+str(atr["id"])+"_"+atr["nome"]+"_"+atr["tipo"]+".md"

    # Chamar a função com o caminho do arquivo
    replace_text(file_path)

