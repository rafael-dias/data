js = []

# print (js[0])


import html2text
import os

# Your list of dictionaries
objects = js
nome_livro = "Guia para o tarot de thoth - Johann Heyss"

# Ensure the 'livro' directory exists
if not os.path.exists('./cartas/'+nome_livro):
    os.makedirs('./cartas/'+nome_livro)

# Convert HTML to Markdown and write to files
for obj in objects:
    # Convert HTML to Markdown
    markdown_content = html2text.html2text(obj['dados'])
    
    # Create file name
    file_name = f"{obj['id']}_{obj['nome']}.md"
    
    # Write to file inside 'livro' folder
    with open(os.path.join('./cartas/'+nome_livro, file_name), 'w', encoding='utf-8') as file:
        file.write(markdown_content)

print("Files have been created successfully.")
