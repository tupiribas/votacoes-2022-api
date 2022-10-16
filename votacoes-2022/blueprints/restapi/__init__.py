from flask import Flask
import pandas as pd

app = Flask(__name__)


@app.route('/')
def home_page():
    # Colocar a documentacao da api
    return 'A API esta pronta pra ser usada!'


@app.route('/mostrar_tudo')
def mostrar_todo():
    dados_votacao_partido = pd.read_csv(
        'dados/votacao_partido.csv', sep=';', encoding='latin-1')
    resultado = dados_votacao_partido[[
        'sg_partido', 'ds_cargo', 'qt_votos_validos', 'sg_uf', 'nm_regiao']]
    return resultado.to_json(orient='records')
