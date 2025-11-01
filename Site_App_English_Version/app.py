import os 
import textwrap
from pathlib import Path
import unicodedata
import re
import subprocess

#================================================

# First of all, remove this file from the "Site" folder and save it in another location on your computer
# For this program to automatically commit your site to GitHub, it is necessary to configure the repository in the folder first
# In the variable below, you must add the path on your computer that leads to the "Site" folder.
# Note that if the path or folder name is changed, this Python file must also be updated.
# Follow the example below:
# Example: /home/newman/documents/

#================================================

caminho_ate_a_pasta_Site = "" #add here 

#================================================


quantidade_p = 0
adicionar = ""
h1 = ""
desc = ""
h2 = ""
p = ""
tag = ""
data = ""
title = ""
mencao = ""
texto_index = ""
lista_texto = list()
lista_tag = list()
post = ""
conteudo_html_com_espaco = ""

print("""
=============================================
    SIMPLE HTML POST GENERATOR
=============================================

Type one of the commands below to build the content:

🔹 title    → add a tab title (<title>)
🔹 h1       → add the page title (<h1>)
🔹 h2       → add a subtitle (<h2>)
🔹 p        → add a paragraph (<p>)
🔹 img      → add an image (<img src='...'>)
🔹 data     → add the post date
🔹 desc     → add the meta description
🔹 tag      → add a meta tag (keywords)

---------------------------------------------
    REMOVAL COMMANDS:
---------------------------------------------
      
🔹 remove h1              → remove the title
🔹 remove data            → remove the date
🔹 remove description     → remove the meta description
🔹 remove tag             → remove the last meta tag
🔹 remove text item       → remove the last item (p, h2, img)
      
---------------------------------------------
Type "stop" when you finish adding elements.
The program will then display the complete HTML generated.

=============================================
""")

idioma = str(input("Before starting, add the post language (EN or PT): "))

while idioma.lower() not in ["en", "pt"]:
    idioma = input("Before starting, add the post language (EN or PT): ")

def funcao_meta_description():
    desc = str(input("Enter the meta description: "))
    return desc

def funcao_tags():
    tag = str(input("Enter a meta tag: "))
    lista_tag.append(tag)
    return lista_tag

def funcao_title():
    title = str(input("Enter the tab title:"))
    return title 

def funcao_h1():
    h1 = str(input("Enter the <h1> title:"))
    return h1 

def funcao_data():
    data = str(input("Enter the date:"))
    return data

def funcao_h2():
    h2 = str(input("Enter the <h2> subtitle:"))

    h2 = "<h2>" + h2 + "</h2>"
    lista_texto.append(h2)
    return h2

def funcao_p():

    p = str(input("Enter the <p> paragraph"))
    p = "<p class='texto'>" + p + "</p>"
    lista_texto.append(p)
    return lista_texto

def funcao_mencao():

    mencao = str(input("Enter a mention:"))
    mencao = "<p class='mencao'>" + mencao + "</p>"
    lista_texto.append(mencao)
    return lista_texto
    

def funcao_imagem():
    img = input("Enter the image file name: ")
    img = f"<img class='imagens' src='../imagens/{img}'>"
    lista_texto.append(img)
    return img


while adicionar != "stop":

    adicionar = str(input("Enter a command: "))

    if adicionar == "h1":
        h1 = funcao_h1()

    elif adicionar == "desc" or adicionar == "description":
        desc = funcao_meta_description()

    
    elif adicionar == "data":
        data = funcao_data()

    elif adicionar == "tag":
        funcao_tags()

    elif adicionar == "title":
        title = funcao_title()


    elif adicionar == "img" or adicionar == "image":
        funcao_imagem()

    elif adicionar == "p":
        funcao_p()
    
    elif adicionar == "h2":
        funcao_h2()
    
    elif adicionar == "mencao" or adicionar == "mention":
        funcao_mencao()
    
    elif adicionar == "remove description" or adicionar == "remove desc":
        desc = ""
    
    elif adicionar == "remove h1":
        h1 = ""

    elif adicionar == "remove date":
        data = ""

    elif adicionar == "remove tag":
        if lista_tag:
            lista_tag.pop()
            print("✅ Last tag removed successfully.")
        else:
            print("⚠️ No tags found to remove.")

    elif adicionar == "remove text item" or adicionar == "remove text" or adicionar == "remove p":

        if lista_texto:
            item_removido = lista_texto.pop()
            print(f"✅ Item removed from text: {item_removido}")
        else:
            print("⚠️ No items in text to remove.")

    elif adicionar.lower() == "stop":
        faltando = []
        if not h1:
            faltando.append("<h1>")
        if not lista_texto:
            faltando.append("<p> or other text content")
        if not data:
            faltando.append("date")
        if not lista_tag:
            faltando.append("meta tags")
        if not desc:
            faltando.append("description")
        if not title:
            faltando.append("tab title")

        if faltando:
            print("\n⚠️ Cannot finish. The following required items are missing:")
            for item in faltando:
                print(f"  - {item}")
            print("Please add them before finishing.\n")
            continue 
        else:
            print("\n Generating post...\n")
            break


for item in lista_texto:
    if item.startswith("<p") and "class='texto'" in item:
        texto_index = item
        break
    
    
def slugify(text):
    text = str(text).lower()
    text = unicodedata.normalize("NFD", text)
    text = text.encode("ascii", "ignore").decode("utf-8")
    text = re.sub(r'[^a-z0-9]+', '_', text)  # ✅ Correction here
    text = re.sub(r'_+', '_', text)  # Remove duplicate underscores
    return text.strip('_')

nome_arquivo = slugify(h1) + ".html"

conteudo_html = ''.join(lista_texto)
tags_html = ", ".join(lista_tag)


for item in lista_texto:
    conteudo_html_com_espaco += f"{item}<div class='espacoHorizontal'></div>\n"

if idioma == "PT" or idioma == "pt":
    caminho = Path(f"{caminho_ate_a_pasta_Site}Site/postsPT")

    post = textwrap.dedent(f"""
                       
<!DOCTYPE html>
<html lang="pt">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="../styles.css">


    <!-- Title -->

    <title>{title}</title>
    <meta name="description" content="{desc}">
    <meta name="keywords" content="{tags_html}">

    <!-- Favicon -->

    <link rel="icon" href="/favicon.ico" type="image/x-icon">
    <meta name="author" content="Anthony Gabriel Stürmer">



</head>
<body>
    <header>
      
        <a href="../index.html" class="nomeDoSite">Anthony's Blog</a>
        <nav>
            <a href="../index.html"><home class="home"></home></a>
        </nav>
    </header>
    <main>
        <div class="conteudo">
            <hr class="linhasInicioFim">
            <div class="espacoHorizontal"></div>
            <div class="espacoHorizontal some"></div>
            
            <!-- Title / publication date -->

            <h1>{h1}</h1>
            



            <div class="espacoHorizontal"></div>
            <p class="entreLinhas">&lt;!-- Published on {data} --&gt;</p>  
            <div class="espacoHorizontal"></div> 

            {conteudo_html_com_espaco}

            <div class="barraLateralMobile"></div>
        </div>
        <div class="espacoVertical"></div>
        <div class="barraLateral"></div>
    </main>
    <footer>
        © 2025 Anthony's Blog. All rights reserved.
    </footer>
<script src="../script.js"></script>
</body>
</html>
""")


else:
    caminho = Path(f"{caminho_ate_a_pasta_Site}Site/postsEN")

    post = textwrap.dedent(f"""
                       
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
   
    <script src="../scriptEN.js"></script>
    <link rel="stylesheet" href="../styles.css"> 

    <!-- Title -->

    <title>{title}</title>

    <!-- Description -->

    <meta name="description" content="{desc}">

    <!-- Keywords -->

    <meta name="keywords" content="{tags_html}">

    <!-- Favicon -->

    <link rel="icon" href="/favicon.ico" type="image/x-icon">

    <!-- Author -->

    <meta name="author" content="Anthony Gabriel Stürmer">
                           
</head>
<body>
    <header>
        <a href="../indexEN.html" class="nomeDoSite">Anthony's Blog</a>
        <nav>
            <a href="../indexEN.html"><home class="home"></home></a>
        </nav>
    </header>
    <main>
        <div class="conteudo">
            <hr class="linhasInicioFim">
            <div class="espacoHorizontal"></div>
            <div class="espacoHorizontal some"></div>


            <h1>{h1}</h1>
            

            <div class="espacoHorizontal"></div>
       
            <p class="entreLinhas">&lt;!-- Published on {data} --&gt;</p>

            <div class="espacoHorizontal"></div>

            {conteudo_html_com_espaco}



            <div class="barraLateralMobile">
            </div>
        </div>
        <div class="espacoVertical"></div>
        <div class="barraLateral"></div>
    </main>
    <footer>
        © 2025 Anthony's Blog. All rights reserved.
    </footer>
</body>
</html>
""")

caminho_completo = caminho / nome_arquivo



with open(caminho_completo, "w", encoding="utf-8") as f:
    f.write(post)



palavra_alvo = "<!--!-TEXT_TO_BE_REPLACED-!-->"


if idioma == "PT" or idioma == "pt":

    caminho = Path(f"{caminho_ate_a_pasta_Site}Site/index.html")
    novo_texto = textwrap.dedent(f'''
                                 
            <!--!-TEXT_TO_BE_REPLACED-!-->
                                 
            <div class="espacoHorizontal some"></div>

            <a href="postsPT/{nome_arquivo}" class="linkIndex">{h1}</a>
            
            <div class="espacoHorizontal"></div>

            <a href="postsPT/{nome_arquivo}"  class="entreLinhasIndex">&lt;!-- Published on {data} --&gt;</a>

            <div class="espacoHorizontal"></div>

            <a href="postsPT/{nome_arquivo}" class="textoIndex">
                {texto_index}
            </a>

            <div class="espacoHorizontal"></div>

            <hr> 
            
            
            ''')

    conteudo = caminho.read_text(encoding="utf-8")
    conteudo_novo = conteudo.replace(palavra_alvo, novo_texto)
    caminho.write_text(conteudo_novo, encoding="utf-8")


else:


    caminho = Path(f"{caminho_ate_a_pasta_Site}Site/indexEN.html")
    novo_texto = textwrap.dedent(f'''
                                 
            <!--!-TEXT_TO_BE_REPLACED-!-->
                                 
            <div class="espacoHorizontal"></div>

            <a href="postsEN/{nome_arquivo}" class="linkIndex">{h1}</a>
            
            <div class="espacoHorizontal"></div>

            <a href="postsEN/{nome_arquivo}"  class="entreLinhasIndex">&lt;!-- Published on {data} --&gt;</a>

            <div class="espacoHorizontal"></div>

            <a href="postsEN/{nome_arquivo}" class="textoIndex">
                {texto_index}
            </a>

            <div class="espacoHorizontal"></div>

            <hr> 
            
            
            ''')

    conteudo = caminho.read_text(encoding="utf-8")
    conteudo_novo = conteudo.replace(palavra_alvo, novo_texto)
    caminho.write_text(conteudo_novo, encoding="utf-8")





print(f"\n✅ File created successfully!\n")


def git_commit(pasta, mensagem):
    try:
        pasta = Path(pasta)

        if not pasta.exists():

            print(f"❌ Folder not found: {pasta}")
            return False
            
        subprocess.run(["git", "add", "."], cwd=pasta, check=True)
        subprocess.run(["git", "commit", "-m", mensagem], cwd=pasta, check=True)
        subprocess.run(["git", "push"], cwd=pasta, check=True)

        print("✅ Commit completed successfully!")
        return True
    
    except subprocess.CalledProcessError as e:

        print(f"❌ Git error: {e}")
        return False
    
    except Exception as e:

        print(f"❌ Unexpected error: {e}")
        return False


git_commit(f"{caminho_ate_a_pasta_Site}Site", "New post!")