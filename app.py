from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
SECRET_KEY = "pudim"
app.config.from_object(__name__)

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
# USER MOCKS
USERNAME = "admin"
PASSWORD = "admin"

@app.route('/')
def exibir_entradas():
    return render_template("exibir_entradas.html", entradas=posts)

@app.route('/login', methods=["GET", "POST"])
def login():
    erro = ""
    if request.method == "POST":
        if request.form['username'] == USERNAME and request.form['password'] == PASSWORD:
            session['logado'] = True
            return redirect(url_for('exibir_entradas'))
        erro = "Usuário ou senha inválidos"
    return render_template("login.html", erro=erro)