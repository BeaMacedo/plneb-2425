from flask import Flask, request, render_template
import json


app = Flask(__name__)

db_file = open('Aula4/conceitos.json', encoding = "utf8")   #onde vai buscar os dados
db = json.load(db_file)        
db_file.close()

@app.route("/")
def hello_world():
    return '<p>Hello World!</p>'


@app.route('/api/conceitos')
def conceitos_api():
    return (db)


@app.route("/api/conceitos/<designacao>")
def api_conceitos(designacao):

    return{"designacao":designacao, "descricao":db[designacao]}     #retorna um conceito específico


@app.post("/conceitos")
def adicionar_conceito():
    data = request.get_json()   #espera que a informação venha no body em formato json
    #{"designacao":"vida","descricao":"a vida é...."} - é o que vem dentro do data
    db[data["designacao"]] = data["descricao"]  #adiciona ao dicionario
    f_out = open("conceitos_.json","w")  
    json.dump(db,f_out, indent=4, ensure_ascii=False)
    f_out.close()
    return data


@app.route("/conceitos")
def conceitos():
    designacoes = list(db.keys())
    return render_template('conceitos.html',designacoes = designacoes, title = "Lista de Conceitos")

@app.route('/conceitos/<designacao>')
def conceito_descricao(designacao):
    descricao = db[designacao]
    return render_template('conceito_descricao.html', designacao=designacao, descricao=descricao)


app.run(host="localhost",port=4002,debug=True)