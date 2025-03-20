from flask import Flask, request, render_template
import json


app = Flask(__name__)

db_file = open('Aula4/conceitos.json', encoding = "utf8")   #onde vai buscar os dados
db = json.load(db_file)        
db_file.close()

@app.route("/")
def home():
    return render_template('home.html')


@app.route('/api/conceitos')
def conceitos_api():
    return (db)


@app.route("/api/conceitos/<designacao>")
def api_conceitos(designacao):

    return{"designacao":designacao, "descricao":db[designacao]}     #retorna um conceito específico

'''@app.post("/conceitos")
def adicionar_conceito():
    data = request.get_json()   #espera que a informação venha no body em formato json
    #{"designacao":"vida","descricao":"a vida é...."} - é o que vem dentro do data
    db[data["designacao"]] = data["descricao"]  #adiciona ao dicionario
    f_out = open("conceitos_.json","w")  
    json.dump(db,f_out, indent=4, ensure_ascii=False)
    f_out.close()
    return data'''

@app.route("/conceitos")
def conceitos():
    designacoes = list(db.keys())
    return render_template('conceitos.html',designacoes = designacoes, title = "Lista de Conceitos")

@app.route('/conceitos/<designacao>')
def conceito_descricao(designacao):
    if designacao in db:
        return render_template('conceito_descricao.html', designacao=designacao, descricao=db[designacao])
    else:
        return render_template('conceito_descricao.html', designacao="Erro", descricao="nao deu")


@app.post("/conceitos") #para receber o pedido de inserção do conceito e da descrição, espera os dados vindos de um formulário e não de um json
def novo_adicionar_conceito():
    descricao = request.form.get("descricao")
    designacao = request.form.get("designacao")
    
    db[designacao] = descricao 
    f_out = open("conceitos_.json","w")  
    json.dump(db,f_out, indent=4, ensure_ascii=False)
    f_out.close()
    #form data
    
    designacoes = list(db.keys())
    
    return render_template("conceitos.html", designacoes=designacoes, title="Lista de Conceitos")

import re
@app.route("/pesquisar", methods=["GET", "POST"])
def pesquisar_conceito():
    resultado_pesquisa = {}
    termo_pesquisa = ""

    if request.method == "POST":
        termo_pesquisa = request.form.get("termo", "").lower()
        pesquisa_exata = "pesquisa_exata" in request.form  # Verifica se o checkbox foi marcado

        for designacao, descricao in db.items():
            if pesquisa_exata:
                # Vai pesquisar se aparece exatamente a palavra no 
                pattern = re.compile(r'\b' + re.escape(termo_pesquisa) + r'\b', re.IGNORECASE)
                if re.search(pattern, designacao.lower()) or re.search(pattern, descricao.lower()):
                    designacao_destacado = re.sub(pattern, r'<span class="text-bg-success fw-bold">\g<0></span>', designacao)
                    descricao_destacado = re.sub(pattern, r'<span class="text-bg-success fw-bold">\g<0></span>', descricao)

                    resultado_pesquisa[designacao_destacado] = descricao_destacado

            else:
                # Vai verificar se a palavra está na designacao ou na descricao (texto todo em minusculas)
                if termo_pesquisa in designacao.lower() or termo_pesquisa in descricao.lower():
                    # Vamos destacar
                    designacao_destacado = re.sub(f"({termo_pesquisa})", r'<span class="text-bg-success fw-bold">\1</span>',designacao, flags=re.IGNORECASE)      
                    descricao_destacado = re.sub(f"({termo_pesquisa})", r'<span class="text-bg-success fw-bold">\1</span>', descricao, flags=re.IGNORECASE)
                    resultado_pesquisa[designacao_destacado] = descricao_destacado
    return render_template("pesquisa.html", termo_pesquisa=termo_pesquisa, resultado_pesquisa=resultado_pesquisa, title="Resultados da Pesquisa")

app.run(host="localhost",port=4002,debug=True)