# TPC7

Neste TPC foi implementada uma tabela interativa utilizando DataTables, uma biblioteca JavaScript que permite exibir e filtrar dados de forma dinâmica. A tabela exibe uma lista de conceitos e suas descrições, permitindo pesquisas avançadas com expressões regulares.

## Funcionalidades implementadas
- Pesquisa com expressões regulares
- Estilização personalizada da tabela 

## Pesquisa com expressões regulares

A pesquisa foi configurada para possibilitar expressões regulares, através da utilização da opção 'search.regex: true' na inicialização do DataTables. Esta opção permite que o utilizador utilize padrões regex na barra de pesquisa.

```python
$(document).ready( function () {
    $('#tabela_conceitos').DataTable({
        search: {
            regex: true
        },
    });     //o id (#) da tabela é tabela_conceitos
} );
```

## Estilização da tabela

Foi utilizado o CSS do DataTables importado no ‘layout.html’, juntamente com um arquivo personalizado style_tabela.css armazenado na pasta /static/styles.css/style_tabela.css para melhorar a aparência da tabela.

#### layout.html:
```python
<link rel="stylesheet" href="https://cdn.datatables.net/2.2.2/css/dataTables.dataTables.css" />
```

#### tabela.html:
```python
<link rel="stylesheet" href="/static/styles.css/style_tabela.css">
```

## Acesso à tabela

É possível aceder à tabela de pesquisa através de um botão na página inicial ‘Home’ ou através de uma opção no menu de navegação.

Para conseguir aceder através do botão inicial, adicionou-se na página ‘home.html’ o seguinte:
```python
       <a href="/conceitos/tabela" class="btn btn-outline-secondary btn-lg px-4">Tabela Conceitos</a>
```


Para conseguir aceder através do menu de navegação, adicionou-se na página layout.html’ o seguinte:
```python
           <li class="nav-item">
              <a class="nav-link" href="/conceitos/tabela">Tabela Conceitos</a>
            </li>
```
