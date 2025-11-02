# analisador-de-filmes

## APLICACAO WEB PARA ANALISE DE DADOS E MACHINE LEARNING

Este projeto e o trabalho final da disciplina, com o objetivo de criar uma aplicacao web em Python que permite ao usuario fazer upload de um arquivo .csv, visualizar analises de dados e realizar predicoes com machine learning.

Esta e a estrutura base (backend) da aplicacao, desenvolvida com Django.

#### TECNOLOGIAS

- Python

- Django

- Pandas

### ESTADO ATUAL

Criacao do projeto Django 'trabalhofinal' e do app 'uploader'.

Configuracao do ambiente e do arquivo 'requirements.txt'.

Estrutura de URLs para 3 paginas principais: Upload, Analise e Predicao.

Implementacao da funcionalidade de Upload de arquivos .csv.

O sistema le o .csv com a biblioteca Pandas, converte o DataFrame para JSON e o armazena na sessao do usuario.

O usuario e redirecionado para a pagina de Analise apos o upload.

Criacao de templates basicos (base.html, upload.html, analysis.html, prediction.html) com navegacao.

### COMO RODAR O PROJETO

O Python e o 'pip' devem estar instalados.

Clone o repositorio.

```python -m venv venv```

(Linux/Mac) ```source venv/bin/activate```

(Windows) ```venv\Scripts\activate```

```pip install -r requirements.txt```

Navega ate a pasta 'trabalhofinal' (onde esta o manage.py).

```python manage.py migrate```

```python manage.py runserver```