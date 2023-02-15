from flask import Flask, render_template, request, redirect, url_for, session, flash

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
    #pegar posts no banco
    return render_template("exibir_entradas.html", entradas=posts)

@app.route('/inserir', methods=["POST"])
def inserir_entradas():
    novo_post = {
        "titulo": request.form['titulo'],
        "texto": request.form['texto']
    }
    posts.append(novo_post)  
    return redirect(url_for('exibir_entradas'))


@app.route('/login', methods=["GET", "POST"])
def login():
    erro = ""
    if request.method == "POST":
        if request.form['username'] == USERNAME and request.form['password'] == PASSWORD:
            session['logado'] = True
            flash("Login efetuado com sucesso!")
            return redirect(url_for('exibir_entradas'))
        erro = "Usuário ou senha inválidos"
    return render_template("login.html", erro=erro)

@app.route('/logout')
def logout():
    session.pop('logado', None)
    flash("Logout efetuado com sucesso!")
    return redirect(url_for('exibir_entradas'))