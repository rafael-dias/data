import sys

# try:
#     print (sys.argv[1])
# except:
#     print ('insira o nome do livro')



from pathlib import Path
Path("./atributos").mkdir(parents=True, exist_ok=True)

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
    with open(Path("./atributos/"+str(atr["id"])+"_"+atr["nome"]+"_"+atr["tipo"]+".md"), "w") as file:
        file.write("")