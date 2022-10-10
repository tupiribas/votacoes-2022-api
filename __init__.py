import pandas as pd


class Eleicoes_2022():
    def requisicao_api():
        dados = pd.read_csv('dados/votacao_candidato.csv',
                            sep=';', encoding='latin-1')
        print(dados['sg_partido'])


Eleicoes_2022.requisicao_api()
