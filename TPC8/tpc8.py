from bs4 import BeautifulSoup
import requests
import json

url="https://www.atlasdasaude.pt/doencasaaz/"
url_base="https://www.atlasdasaude.pt/"
response = requests.get("https://www.atlasdasaude.pt/doencasaaz/")
html_content= response.text
soup = BeautifulSoup(html_content, 'html.parser')

doencas={}

def adquirir_letras():
    for letter in soup.find_all("div", class_="views-summary views-summary-unformatted"):
        contador += 1
        letra=letter.text.strip().lower()
        #print(letra)
        extrair_desc_desig(letra)

def doenca_info(url):
    response = requests.get(url)
    html_content = response.text
    soup = BeautifulSoup(html_content, 'html.parser')


    conteudo_palavra = {
            "InformaçãoInicial": "",
            "Causas": "",
            "sintomas": ["",[]],
            "Diagnóstico": "",
            "Tratamento": "",
            "ArtigosRelacionados": {},
            "Site": "",
            "Nota": "",
            "Fonte":"" 
        }
    
    div_content= soup.find("div", class_="node-doencas") #todas as informações
    if not div_content:
        return conteudo_palavra 
    
    #todas as informações exceto site, fonte e nota
    div_body = div_content.find("div", class_="field-name-body")
    if div_body:
        field_item = div_body.find("div", class_="field-item even")
        if not field_item:
            return conteudo_palavra
    else:
        return conteudo_palavra
    

    #informação inicial - quando encontra o 1º h2 significa que já existe um titulo
    info_clinica_texto = []
    for element in field_item.children:
        if element.name == 'h2': 
            break
        if element.name == 'p':
            info_clinica_texto.append(element.get_text(strip=True)) 
    conteudo_palavra["InformaçãoInicial"] = ' '.join(info_clinica_texto).strip()


        #para percorrer todas as secções
    ocorrencias_h2 = field_item.find_all('h2')
    for h2 in ocorrencias_h2:
        titulo = h2.get_text(strip=True).lower()
        next_sibling = h2.find_next_sibling()  # Próximo elemento após o título <h2>
        elementos = []

        # Recolher os elementos subsequentes até o próximo título <h2>
        while next_sibling and next_sibling.name != 'h2':
            elementos.append(next_sibling)
            next_sibling = next_sibling.find_next_sibling()

        if 'causas' in titulo:
            causas = []
            for elemento in elementos:
                if elemento.name == 'p':
                    causas.append(elemento.get_text(strip=True))
                elif elemento.name == 'ul':
                    causas.extend([li.get_text(strip=True) for li in elemento.find_all('li')])
            conteudo_palavra["Causas"] = ' '.join(causas).strip()

        elif 'sintomas' in titulo:
            sintomas = [] #guardar parágrafos (<p>) de texto descritivo
            lista_sintomas = [] #guardar os itens que aparecem em listas do HTML (<ul><li>)
            for elemento in elementos:
                if elemento.name == 'p':
                    sintomas.append(elemento.get_text(strip=True))
                elif elemento.name == 'ul':
                    lista_sintomas.extend([li.get_text(strip=True) for li in elemento.find_all('li')])
            conteudo_palavra["sintomas"] = [' '.join(sintomas).strip(), lista_sintomas]

        elif 'diagnostico' in titulo or 'diagnóstico' in titulo:
            diagnostico = []
            for elemento in elementos:
                if elemento.name == 'p':
                    diagnostico.append(elemento.get_text(strip=True))
                elif elemento.name == 'ul':
                    diagnostico.extend([li.get_text(strip=True) for li in elemento.find_all('li')])
            conteudo_palavra["Diagnóstico"] = ' '.join(diagnostico).strip()

        elif 'tratamento' in titulo:
            tratamento = []
            for elemento in elementos:
                if elemento.name == 'p':
                    tratamento.append(elemento.get_text(strip=True))
            conteudo_palavra["Tratamento"] = ' '.join(tratamento).strip()

        elif 'artigos relacionados' in titulo:
            artigos = {}
            for elemento in elementos:
                if elemento.name == 'h3':
                    a = elemento.find('a')
                    if a:
                        artigos[a.get_text(strip=True)] = a.get('href', '')
            conteudo_palavra["ArtigosRelacionados"] = artigos
            
    #Extração do site--------------------------------------------------
    div_site = div_content.find("div", class_="field-name-field-site")
    if div_site:
        field_item_site = div_site.find("div", class_="field-item even")
        if field_item_site:
            site_content = field_item_site.get_text(strip=True)
            conteudo_palavra["Site"] = site_content  # Armazena o site no dicionário

    # Extração da nota---------------------------------------------
    div_nota = div_content.find("div", class_="field-name-field-nota")
    if div_nota:
        field_item_nota = div_nota.find("div", class_="field-item even")
        if field_item_nota:
            nota_content = field_item_nota.get_text(strip=True)
            conteudo_palavra["Nota"] = nota_content  # Armazena a nota no dicionário

    # Extração da Fonte-------------------------------------------------
    div_fonte = div_content.find("div", class_="field-name-field-fonte")
    if div_fonte:
        field_item_fonte = div_fonte.find("div", class_="field-item even")
        if field_item_fonte:
            fonte_content = field_item_fonte.get_text(strip=True)
            conteudo_palavra["Fonte"] = fonte_content  # Armazena a fonte no dicionário

    return conteudo_palavra
    

def extrair_desc_desig(letter):
    url_letra = url + str(letter)
    response = requests.get(url_letra)
    html_content = response.text
    soup = BeautifulSoup(html_content, 'html.parser')

    for elemento in soup.find_all("div", class_="views-row"):
        designacao_div = elemento.find("div", class_="views-field-title")
        link_tag = designacao_div.find("a") #link para a página da doença
        designacao = designacao_div.get_text(strip=True) #designação da doença
        href = link_tag["href"] if link_tag else None

        url_palavra = url_base + href # link para a página da doença

        # Uso da função anterior para obter os detalhes de cada palavra/doença
        conteudo_palavra = doenca_info(url_palavra)

        descricao_div = elemento.find("div", class_="views-field-body")
        if descricao_div and descricao_div.div:
            if descricao_div.div.p:
                descricao = descricao_div.div.p.text.strip().replace("\n", " ")
            else:
                descricao = descricao_div.div.text.strip().replace("\n", " ")


        # Guardar tudo no dicionário
        doencas[designacao] = {
            "Resumo": descricao,
            "URL": url_palavra,
            "InformaçãoInicial": conteudo_palavra["InformaçãoInicial"],
            "Causas": conteudo_palavra["Causas"],
            "Sintomas": conteudo_palavra["sintomas"],
            "Diagnóstico": conteudo_palavra["Diagnóstico"],
            "Tratamento": conteudo_palavra["Tratamento"],
            "ArtigosRelacionados": conteudo_palavra["ArtigosRelacionados"],
            "Site": conteudo_palavra["Site"],
            "Nota": conteudo_palavra["Nota"],
            "Fonte": conteudo_palavra["Fonte"]
        }


adquirir_letras()

print(doencas)
f_out = open("doencas.json", "w", encoding="utf-8")
json.dump(doencas, f_out, indent=4, ensure_ascii=False)
f_out.close()


