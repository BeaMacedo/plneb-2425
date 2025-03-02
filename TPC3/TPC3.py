import re
import os

file = open("TPC/TPC3/dicionario_medico.txt", encoding="utf-8")
texto = file.read()

texto = re.sub("\f","",texto)       #removemos os \f das quebras de páginas

#1 - colocar marca: colocamos @, porque vimos no texto que não existia nenhum @

'''r = re.findall(r"Significado",texto)
print(r)'''     #só ocorre no início a palavra Significado

texto = re.sub(r"Significado","Significado.",texto) #para apanhar o primeiro conceito

texto = re.sub(r"\.\n\n",".\n\n@",texto) #como as descrições acabam em '.' então os conceitos começam depois de 1 ponto final e 2 \n

texto = re.sub(r"@([A-Z][^@]*\.)", r"\1", texto) #Se começar em maiuscula e terminar em ponto final remover o @
#por causa de quimiotaxia, no meio da descrição tinha uma quebra de pagina a começar uma nova frase na nova página


#2 - extrair conceito
    
def limpa_descricao(descricao):
    descricao = descricao.strip() # Remove espaços extras no início e no fim
    descricao = re.sub(r"\n", " ", descricao) #Substitui quebras de linha por espaço
    return descricao

#3-
conceitos_raw = re.findall(r'@(.*)\n([^@]*)', texto)
#print(conceitos_raw)

conceitos = [(designacao, limpa_descricao(descricao)) for designacao, descricao in conceitos_raw]
print(conceitos)


#gerar html

def gera_html(conceitos):
    html_header = f"""
        <!DOCTYPE html>
        <head>
        <meta charset = "UTF-8">
        </head>
        <body> 
        <h3>Dicionário de conceitos Médicos </h3>
        <p>Este dicionário foi desenvolvido para a aula de PLNEB 2024/
        2025 <p>"""

    html_conceitos = ""

    for designacao, descricao in conceitos:
        html_conceitos += f"""
                    <div>
                    <p><b>{designacao}</b></p> 
                    <p>{descricao}</p> 
                    </div>
                    <hr/>       
            """

    html_footer = """
        </body>
    </html> """

    return html_header + html_conceitos + html_footer

html = gera_html(conceitos)
f_out = open("dicionario_medico.html", "w", encoding = "utf-8")
f_out.write(html)
f_out.close()


file.close()