from flask import Flask

from votacoes_2022.ext import configuration


# Impedir que quem utilizar esse codigo nao utilize o 'app'
def minimal_app():
    app = Flask(__name__)
    configuration.init_app(app)
    return app


def create_app():
    app = minimal_app()
    configuration.init_app(app)
    return app
