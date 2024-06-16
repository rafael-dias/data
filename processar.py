from pathlib import Path

import re

# Lista de textos para encontrar e substituir
to_find = [
    "Momento atual:", "Ancora:", "Infância:", "Relacionamentos:",
    "Voz da Essência e Método:", "Caminho de crescimento:",
    "Resultado interno:", "Resultado externo:"
]
to_replace = [
    "**Momento atual:**\n\n", "\n\n\n**Ancora:**\n\n", "\n\n\n**Infância:**\n\n",
    "\n\n\n**Relacionamentos:**\n\n", "\n\n\n**Voz da Essência e Método:**\n\n",
    "\n\n\n**Caminho de crescimento:**\n\n", "\n\n\n**Resultado interno:**\n\n",
    "\n\n\n**Resultado externo:**\n\n"
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

deck =  [
        {
          "id": 0,
          "nome": "Louco",
          "dados": ""
        },
        {
          "id": 1,
          "nome": "Mago",
          "dados": ""
        },
        {
          "id": 2,
          "nome": "Sacerdotisa",
          "dados": ""
        },
        {
          "id": 3,
          "nome": "Imperatriz",
          "dados": ""
        },
        {
          "id": 4,
          "nome": "Imperador",
          "dados": ""
        },
        {
          "id": 5,
          "nome": "Hierofante",
          "dados": ""
        },
        {
          "id": 6,
          "nome": "Amantes",
          "dados": ""
        },
        {
          "id": 7,
          "nome": "Carro",
          "dados": ""
        },
        {
          "id": 8,
          "nome": "Ajustamento",
          "dados": ""
        },
        {
          "id": 9,
          "nome": "Eremita",
          "dados": ""
        },
        {
          "id": 10,
          "nome": "Fortuna",
          "dados": ""
        },
        {
          "id": 11,
          "nome": "Luxúria",
          "dados": ""
        },
        {
          "id": 12,
          "nome": "Enforcado",
          "dados": ""
        },
        {
          "id": 13,
          "nome": "Morte",
          "dados": ""
        },
        {
          "id": 14,
          "nome": "Arte",
          "dados": ""
        },
        {
          "id": 15,
          "nome": "Diabo",
          "dados": ""
        },
        {
          "id": 16,
          "nome": "Torre",
          "dados": ""
        },
        {
          "id": 17,
          "nome": "Estrela",
          "dados": ""
        },
        {
          "id": 18,
          "nome": "Lua",
          "dados": ""
        },
        {
          "id": 19,
          "nome": "Sol",
          "dados": ""
        },
        {
          "id": 20,
          "nome": "Aeon",
          "dados": ""
        },
        {
          "id": 21,
          "nome": "O Universo",
          "dados": ""
        },
        {
          "id": 22,
          "nome": "A Raiz Dos Poderes De Fogo - Ás De Bastões",
          "dados": ""
        },
        {
          "id": 23,
          "nome": "Domínio - Dois De Bastões",
          "dados": ""
        },
        {
          "id": 24,
          "nome": "Virtude - Três De Bastões",
          "dados": ""
        },
        {
          "id": 25,
          "nome": "Conclusão - Quatro De Bastões",
          "dados": ""
        },
        {
          "id": 26,
          "nome": "Disputa - Cinco De Bastões",
          "dados": ""
        },
        {
          "id": 27,
          "nome": "Vitória - Seis De Bastões",
          "dados": ""
        },
        {
          "id": 28,
          "nome": "Valor - Sete De Bastões",
          "dados": ""
        },
        {
          "id": 29,
          "nome": "Rapidez - Oito De Bastões",
          "dados": ""
        },
        {
          "id": 30,
          "nome": "Força - Nove De Bastões",
          "dados": ""
        },
        {
          "id": 31,
          "nome": "Opressão - Dez De Bastões",
          "dados": ""
        },
        {
          "id": 32,
          "nome": "Cavaleiro De Bastões",
          "dados": ""
        },
        {
          "id": 33,
          "nome": "Rainha De Bastões",
          "dados": ""
        },
        {
          "id": 34,
          "nome": "Príncipe De Bastões",
          "dados": ""
        },
        {
          "id": 35,
          "nome": "Princesa De Bastões",
          "dados": ""
        },
        {
          "id": 36,
          "nome": "A Raiz Dos Poderes Da Água - Ás De Copas",
          "dados": ""
        },
        {
          "id": 37,
          "nome": "Amor - Dois De Copas",
          "dados": ""
        },
        {
          "id": 38,
          "nome": "Abundância - Três De Copas",
          "dados": ""
        },
        {
          "id": 39,
          "nome": "Luxúria - Quatro De Copas",
          "dados": ""
        },
        {
          "id": 40,
          "nome": "Desapontamento - Cinco De Copas",
          "dados": ""
        },
        {
          "id": 41,
          "nome": "Prazer - Seis De Copas",
          "dados": ""
        },
        {
          "id": 42,
          "nome": "Deboche (Corrupção) - Sete De Copas",
          "dados": ""
        },
        {
          "id": 43,
          "nome": "Indolência - Oito De Copas",
          "dados": ""
        },
        {
          "id": 44,
          "nome": "Felicidade - Nove De Copas",
          "dados": ""
        },
        {
          "id": 45,
          "nome": "Saciedade - Dez De Copas",
          "dados": ""
        },
        {
          "id": 46,
          "nome": "Cavaleiro De Copas",
          "dados": ""
        },
        {
          "id": 47,
          "nome": "Rainha De Copas",
          "dados": ""
        },
        {
          "id": 48,
          "nome": "Príncipe De Copas",
          "dados": ""
        },
        {
          "id": 49,
          "nome": "Princesa De Copas",
          "dados": ""
        },
        {
          "id": 50,
          "nome": "A Raiz Dos Poderes Do Ar - Ás De Espadas",
          "dados": ""
        },
        {
          "id": 51,
          "nome": "Paz - Dois De Espadas",
          "dados": ""
        },
        {
          "id": 52,
          "nome": "Dor - Três De Espadas",
          "dados": ""
        },
        {
          "id": 53,
          "nome": "Trégua - Quatro De Espadas",
          "dados": ""
        },
        {
          "id": 54,
          "nome": "Derrota - Cinco De Espadas",
          "dados": ""
        },
        {
          "id": 55,
          "nome": "Ciência - Seis De Espadas",
          "dados": ""
        },
        {
          "id": 56,
          "nome": "Futilidade - Sete De Espadas",
          "dados": ""
        },
        {
          "id": 57,
          "nome": "Interferência - Oito De Espadas",
          "dados": ""
        },
        {
          "id": 58,
          "nome": "Crueldade - Nove De Espadas",
          "dados": ""
        },
        {
          "id": 59,
          "nome": "Ruína - Dez De Espadas",
          "dados": ""
        },
        {
          "id": 60,
          "nome": "Cavaleiro De Espadas",
          "dados": ""
        },
        {
          "id": 61,
          "nome": "Rainha De Espadas",
          "dados": ""
        },
        {
          "id": 62,
          "nome": "Príncipe De Espadas",
          "dados": ""
        },
        {
          "id": 63,
          "nome": "Princesa De Espadas",
          "dados": ""
        },
        {
          "id": 64,
          "nome": "A Raiz Dos Poderes Da Terra - Ás De Discos",
          "dados": ""
        },
        {
          "id": 65,
          "nome": "Mudança - Dois De Discos",
          "dados": ""
        },
        {
          "id": 66,
          "nome": "Trabalho - Três De Discos",
          "dados": ""
        },
        {
          "id": 67,
          "nome": "Poder - Quatro De Discos",
          "dados": ""
        },
        {
          "id": 68,
          "nome": "Preocupação - Cinco De Discos",
          "dados": ""
        },
        {
          "id": 69,
          "nome": "Sucesso - Seis De Discos",
          "dados": ""
        },
        {
          "id": 70,
          "nome": "Fracasso - Sete De Discos",
          "dados": ""
        },
        {
          "id": 71,
          "nome": "Prudência - Oito De Discos",
          "dados": ""
        },
        {
          "id": 72,
          "nome": "Ganho - Nove De Discos",
          "dados": ""
        },
        {
          "id": 73,
          "nome": "Riqueza - Dez De Discos",
          "dados": ""
        },
        {
          "id": 74,
          "nome": "Cavaleiro De Discos",
          "dados": ""
        },
        {
          "id": 75,
          "nome": "Rainha De Discos",
          "dados": ""
        },
        {
          "id": 76,
          "nome": "Príncipe De Discos",
          "dados": ""
        },
        {
          "id": 77,
          "nome": "Princesa De Discos",
          "dados": ""
        }
      ]

for carta in deck:
    # Caminho do arquivo a ser modificado
    file_path = './cartas/Tarot Terapeutico - Veet Pramad/'+str(carta["id"])+'_'+carta["nome"]+'.md'

    # Chamar a função com o caminho do arquivo
    replace_text(file_path)

