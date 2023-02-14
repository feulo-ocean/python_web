from flask import Flask, render_template

app = Flask(__name__)

# POSTS MOCK
posts = [
    {
        "titulo": "Post 1",
        "texto": "Meu primeiro Post"
    },
    {
        "titulo": "Post 2",
        "texto": "Olha eu aqui de novo"
    },
       {
        "titulo": "Post 3",
        "texto": "Novo Post"
    }
]

@app.route('/')
def exibir_entradas():
    return render_template("exibir_entradas.html", entradas=posts)