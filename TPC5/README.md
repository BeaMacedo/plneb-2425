# TPC5 - Flask

Foi utilizado o framework Flask para criar uma aplicação web em que fosse possível listar as designações e as suas respetivas descrições, informações estas que estão armazenadas numa base de dados json. selecionando numa designação, o utilizador é redirecionado para uma página que apresenta a designação e a descrição completa da mesma.

## Rotas desenvolvidas

### /conceitos

Esta rota possibilita a listagem de todas as designações armazenadas na base de dados, que são apresentadas na página conceitos.html.

```python
@app.route('/conceitos')
def adiciona_conceito():
    #por json
    designacoes = list(db.keys())
    return render_template('conceitos.html', designacoes=designacoes, title="Lista de Designações")
```

Na página conceitos.html, cada designação é apresentada como um link que, ao ser clicado, redireciona o utilizador para a URL /conceitos/<designacao>, ou seja é direcionado para a rota que apresenta a descrição da designação selecionada.

```python
    <ul>
        {% for conceito in designacoes %}
            <li>
                <a href="{{ url_for('conceito_descricao', designacao=conceito) }}">{{ conceito }}</a>
            </li>
        {% endfor %}
    </ul>
```

### /conceitos/\<designacao\>
Esta rota exibe a descrição da designação de um conceito que foi selecionado, isto é quando o utilizador seleciona um dos links da página conceitos.html é redirecionado para esta rota. A aplicação retorna a descrição correspondente à designação selecionada e a apresenta-a na página conceito_descricao.html.

```python
@app.route('/conceitos/<designacao>')
def conceito_descricao(designacao):
    descricao = db[designacao]
    return render_template('conceito_descricao.html', designacao=designacao, descricao=descricao)
```
