# TPC6 - Flask, Bootstrap e Regex


Foi utilizado o framework Flask para a criação da aplicação web, como já foi mencionado no TPC anterior. Foi adicionada a funcionalidade de pesquisar conceitos armazenados na base de dados, sendo possível o utilizador inserir uma palavra e obter resultados que correspondam à palavra pesquisada, com a opção de realizar uma pesquisa exata da palavra introduzida ou então parcial (onde serão também dadas correspondências quando o termo se encontra “dentro” de uma palavra).

## Funcionalidades

- Pesquisa de palavras com correspondência exata ou parcial.
- Destaque dos termos encontrados nos resultados da pesquisa.
- Interface desenvolvida com Bootstrap.

## Rotas Desenvolvidas

### /pesquisar
Esta rota possibilita ao utilizador inserir um termo de pesquisa e obter os resultados correspondentes. Caso haja correspondências com a palavra pesquisada, quer esta corresponda a uma designação ou a uma palavra presente em descrições,  a mesma será exibida com o termo destacado. É utilizado Regex para a pesquisa avançada e o destaque das palavras.

#### Implementação da Rota:
```python

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
```

## Página pesquisa.html
A página de pesquisa apresenta um formulário onde o user pode inserir a palavra que quer pesquisar e escolher se quer uma pesquisa exata ou não. Se houver resultados, as correspondências com essa palavra ficarão destacadas.

