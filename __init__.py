from bottle import Bottle, template, request, static_file, redirect, run
import os

# ----------------------------------------------------------------------
# Instância da aplicação
# ----------------------------------------------------------------------
app = Bottle()

# Credenciais simuladas (somente para demonstração)
USERS = {
    "user1": "python",
    "user2": "java",
    "user3": "go",
}


def check_login(username: str, password: str) -> bool:
    """Verifica se usuário e senha correspondem às credenciais cadastradas."""
    return USERS.get(username) == password


# ----------------------------------------------------------------------
# Rotas
# ----------------------------------------------------------------------
@app.get("/login")
def login_form():
    """Exibe o formulário de login."""
    return template("login", sucesso=True)


@app.post("/login")
def login_submit():
    """Recebe os dados do formulário e valida o login."""
    username = request.forms.get("username")
    password = request.forms.get("password")
    sucesso = check_login(username, password)
    if sucesso:
        return template("verificacao_login", sucesso=True, name=username)
    return template("login", sucesso=False)


@app.get("/")
def root():
    """Redireciona a rota raiz para a tela de login."""
    return redirect("/login")


@app.get("/static/<filepath:path>")
def server_static(filepath):
    """Serve arquivos estáticos (CSS, JS, imagens, etc.)."""
    return static_file(filepath, root="static")


# ----------------------------------------------------------------------
# Tratamento de erros
# ----------------------------------------------------------------------
@app.error(404)
def error404(_):
    """Página personalizada para erros 404."""
    return template("page404")


# ----------------------------------------------------------------------
# Execução
# ----------------------------------------------------------------------
if __name__ == "__main__":
    # Se a variável APP_LOCATION == 'heroku', lê a porta definida pela plataforma
    if os.environ.get("APP_LOCATION") == "heroku":
        run(app=app, host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
    else:
        run(app=app, host="localhost", port=8080, debug=True, reloader=True)
