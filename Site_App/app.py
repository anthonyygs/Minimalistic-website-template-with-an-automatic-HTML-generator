import os 
import textwrap
from pathlib import Path
import unicodedata
import re
import subprocess


#================================================

# Antes de tudo, retire este arquivo da pasta "Site" e o guarde em outro local do seu computador
# Para que este programa faça commit automaticamente do seu site no GitHub, é necessário configurar o repositório na pasta antes
# Na variável abaixo você deve adicionar o caminho no seu computador que leva até a pasta "Site".
# Note que, caso o caminho ou nome da pasta seja alterado, este arquivo Python também deverá ser.
# Siga o exemplo abaixo:
# Exemplo: /home/newman/documentos/

#================================================

caminho_ate_a_pasta_Site = "" #add here // adicione aqui

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
    GERADOR DE POSTAGEM HTML SIMPLES
=============================================

Digite um dos comandos abaixo para construir o conteúdo:

🔹 title    → adicionar um título a aba (<title>)
🔹 h1       → adicionar o título da página (<h1>)
🔹 h2       → adicionar um subtítulo (<h2>)
🔹 p        → adicionar um parágrafo (<p>)
🔹 img      → adicionar uma imagem (<img src='...'>)
🔹 data     → adicionar a data do post
🔹 desc     → adicionar a meta descrição
🔹 tag      → adicionar uma meta tag (palavras-chave)

---------------------------------------------
    COMANDOS DE REMOÇÃO:
---------------------------------------------
      
🔹 remover h1              → remove o título
🔹 remover data            → remove a data
🔹 remover descrição       → remove a meta descrição
🔹 remover tag             → remove a última meta tag
🔹 remover item do texto   → remove o último item (p, h2, img)
      
---------------------------------------------
Digite "parar" quando terminar de adicionar os elementos.
O programa então mostrará o HTML completo gerado.

=============================================
""")


while idioma.lower() not in ["en", "pt"]:

    idioma = input("Antes de começar adicione o idioma do post (EN ou PT): ")

def funcao_meta_description():
    desc = str(input("Digite a meta descrição: "))
    return desc

def funcao_tags():
    tag = str(input("Digite uma meta tag: "))
    lista_tag.append(tag)
    return lista_tag

def funcao_title():
    title = str(input("Digite o título da aba:"))
    return title 

def funcao_h1():
    h1 = str(input("Digite o título <h1>:"))
    return h1 

def funcao_data():
    data = str(input("Digite a data:"))
    return data

def funcao_h2():
    h2 = str(input("Digite o subtítulo <h2>:"))

    h2 = "<h2>" + h2 + "</h2>"
    lista_texto.append(h2)
    return h2

def funcao_p():

    p = str(input("Digite o parágrafo <p>"))
    p = "<p class='texto'>" + p + "</p>"
    lista_texto.append(p)
    return lista_texto

def funcao_mencao():

    mencao = str(input("Digite uma menção:"))
    mencao = "<p class='mencao'>" + mencao + "</p>"
    lista_texto.append(mencao)
    return lista_texto
    

def funcao_imagem():
    img = input("Digite o nome do arquivo imagem: ")
    img = f"<img class='imagens' src='../imagens/{img}'>"
    lista_texto.append(img)
    return img


while adicionar != "parar":

    adicionar = str(input("Digite um comando: "))

    if adicionar == "h1":
        h1 = funcao_h1()

    elif adicionar == "desc" or adicionar == "descrição" or adicionar == "descricao":
        desc = funcao_meta_description()

    
    elif adicionar == "data":
        data = funcao_data()

    elif adicionar == "tag":
        funcao_tags()

    elif adicionar == "title":
        title = funcao_title()


    elif adicionar == "img" or adicionar == "imagem":
        funcao_imagem()

    elif adicionar == "p":
        funcao_p()
    
    elif adicionar == "h2":
        funcao_h2()
    
    elif adicionar == "mencao" or adicionar == "menção" or adicionar == "mencão" or adicionar == "mençao":
        funcao_mencao()
    
    elif adicionar == "remover descrição" or adicionar == "remover desc" or adicionar == "remover descricao" or adicionar == "remover descricão" or adicionar == "remover descriçao":
        desc = ""
    
    elif adicionar == "remover h1":
        h1 = ""

    elif adicionar == "remover data":
        data = ""

    elif adicionar == "remover tag":
        if lista_tag:
            lista_tag.pop()
            print("✅ Última tag removida com sucesso.")
        else:
            print("⚠️ Nenhuma tag encontrada para remover.")

    elif adicionar == "remover item do texto" or adicionar == "remover texto" or adicionar == "remover p":

        if lista_texto:
            item_removido = lista_texto.pop()
            print(f"✅ Item removido do texto: {item_removido}")
        else:
            print("⚠️ Nenhum item no texto para remover.")

    elif adicionar.lower() == "parar":
        faltando = []
        if not h1:
            faltando.append("<h1>")
        if not lista_texto:
            faltando.append("<p> ou outro conteúdo de texto")
        if not data:
            faltando.append("data")
        if not lista_tag:
            faltando.append("meta tags")
        if not desc:
            faltando.append("descrição")
        if not title:
            faltando.append("título da aba")

        if faltando:
            print("\n⚠️ Não é possível finalizar. Faltam os seguintes itens obrigatórios:")
            for item in faltando:
                print(f"  - {item}")
            print("Por favor, adicione-os antes de finalizar.\n")
            continue 
        else:
            print("\n Gerando o post...\n")
            break


for item in lista_texto:
    if item.startswith("<p") and "class='texto'" in item:
        texto_index = item
        break
    
    
def slugify(text):
    text = str(text).lower()
    text = unicodedata.normalize("NFD", text)
    text = text.encode("ascii", "ignore").decode("utf-8")
    text = re.sub(r'[^a-z0-9]+', '_', text)  # ✅ Correção aqui
    text = re.sub(r'_+', '_', text)  # Remove underscores duplicados
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
    <meta name="autor" content="Anthony Gabriel Stürmer">



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
            
            <!-- Título / data de publicação -->

            <h1>{h1}</h1>
            



            <div class="espacoHorizontal"></div>
            <p class="entreLinhas">&lt;!-- Publicado em {data} --&gt;</p>  
            <div class="espacoHorizontal"></div> 

            {conteudo_html_com_espaco}

            <div class="barraLateralMobile"></div>
        </div>
        <div class="espacoVertical"></div>
        <div class="barraLateral"></div>
    </main>
    <footer>
        © 2025 Anthony’s Blog. All rights reserved.
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

    <!-- Palavras-chave -->

    <meta name="description" content="Resenha do livro O que é inteligência artificial” do escritor João Fernandes Teixeira, publicado pela Editora Primeiros Passos">

    <!-- Palavras-chave -->

    <meta name="keywords" content="{tags_html}">

    <!-- Favicon -->

    <link rel="icon" href="/favicon.ico" type="image/x-icon">

    <!-- Autor -->

    <meta name="autor" content="Anthony Gabriel Stürmer">
                           
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
        © 2025 Anthony’s Blog. All rights reserved.
    </footer>
</body>
</html>
""")

caminho_completo = caminho / nome_arquivo



with open(caminho_completo, "w", encoding="utf-8") as f:
    f.write(post)



palavra_alvo = "<!--!-TEXTO_A_SER_TROCADO-!-->"


if idioma == "PT" or idioma == "pt":

    caminho = Path(f"{caminho_ate_a_pasta_Site}Site/index.html")
    novo_texto = textwrap.dedent(f'''
                                 
            <!--!-TEXTO_A_SER_TROCADO-!-->
                                 
            <div class="espacoHorizontal some"></div>

            <a href="postsPT/{nome_arquivo}" class="linkIndex">{h1}</a>
            
            <div class="espacoHorizontal"></div>

            <a href="postsPT/{nome_arquivo}"  class="entreLinhasIndex">&lt;!-- Publicado em {data} --&gt;</a>

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
                                 
            <!--!-TEXTO_A_SER_TROCADO-!-->
                                 
            <div class="espacoHorizontal"></div>

            <a href="postsEN/{nome_arquivo}" class="linkIndex">{h1}</a>
            
            <div class="espacoHorizontal"></div>

            <a href="postsEN/{nome_arquivo}"  class="entreLinhasIndex">&lt;!-- Publicado em {data} --&gt;</a>

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





print(f"\n✅ Arquivo criado com sucesso!\n")


def git_commit(pasta, mensagem):
    try:
        pasta = Path(pasta)

        if not pasta.exists():

            print(f"❌ Pasta não encontrada: {pasta}")
            return False
            
        subprocess.run(["git", "add", "."], cwd=pasta, check=True)
        subprocess.run(["git", "commit", "-m", mensagem], cwd=pasta, check=True)
        subprocess.run(["git", "push"], cwd=pasta, check=True)

        print("✅ Commit realizado com sucesso!")
        return True
    
    except subprocess.CalledProcessError as e:

        print(f"❌ Erro no Git: {e}")
        return False
    
    except Exception as e:

        print(f"❌ Erro inesperado: {e}")
        return False


git_commit(f"{caminho_ate_a_pasta_Site}Site", "Novo post!")