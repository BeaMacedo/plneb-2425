import json
from flask import Flask, request, redirect, url_for, render_template



app = Flask(__name__)
@app.route('/') 
def hello_world():
    return '<p>Hello World!</p>'


db_file=open('Aula4/conceitos.json', "r", encoding="utf-8")
db=json.load(db_file)
db_file.close()
@app.route('/api/conceitos')
def conceitos():
    return (db)


@app.route('/api/conceitos/<designacao>')
def api_conceito(designacao):
    return {"designacao":f'{designacao}', "descricao":db[designacao]}


@app.post("/conceitos")
def adicionar_conceito():
    data = request.get_json()   #espera que a informação venha no body em formato json
    #{"designacao":"vida","descricao":"a vida é...."} - é o que vem dentro do data
    db[data["designacao"]] = data["descricao"]  #adiciona ao dicionario
    f_out = open("conceitos_.json","w")  
    json.dump(db,f_out, indent=4, ensure_ascii=False)
    f_out.close()
    return data

@app.route('/conceitos')
def adiciona_conceito():
    #por json
    designacoes = list(db.keys())
    return render_template('conceitos.html', designacoes=designacoes, title="Lista de Designações")


@app.route('/conceitos/<designacao>')
def conceito_descricao(designacao):
    descricao = db[designacao]
    return render_template('conceito_descricao.html', designacao=designacao, descricao=descricao)


app.run(host="localhost",port=4002,debug=True)