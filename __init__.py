from bottle import route, run
from bottle import template, request
from bottle import static_file, get
from bottle import error
import os
""" @route("/")
@route("/user/<nome>")
def index(nome="Desconhecido"):
    return "<h1>Olá " + nome + " </h1>"


@route("/artigo/<id>")
def artigo(id):
    return "<h1>Você está lendo o artigo" + id + " </h1>"


@route("/pagina/<id>/<nome>")
def pagina(id, nome):
    return "<h1>Você está vendo a página " + id + " com o nome " + nome + " </h1 >" """

# STATIC ROUTES


@get('/<filename:re:.*\.css>')
def stylesheets(filename):
    return static_file(filename, root='static/css')


@get('/<filename:re:.*\.js>')
def javascripts(filename):
    return static_file(filename, root='static/js')


@get('/<filename:re:.*\.(jpg|png|gif|ico)>')
def images(filename):
    return static_file(filename, root='static/imgs')


@get('/<filename:re:.*\.(eot|ttf|woff|svg)>')
def fonts(filename):
    return static_file(filename, root='static/fonts')


@route("/login")
def login():
    return template("login")


def check_login(username, password):
    d = {"user1": "python", "user2": "java", "user3": "go"}
    if username in d.keys() and d[username] == password:
        return True
    return False


@route("/")
def index():
    return template("login")


@route("/", method="POST")
def acao_login():
    username = request.forms.get("username")
    password = request.forms.get("password")
    sucesso = check_login(username, password)
    return template("verificacao_login", sucesso=check_login(username, password))


@error(404)
def error404(error):
    return template("page404")


if __name__ == '__main__':
    if os.environ.get('APP_LOCATION') == "heroko":
        run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
    else:
        run(host="localhost", port=8080, debug=True, reloader=True)
