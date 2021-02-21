import pandas as pd
# Não estava conseguindo abrir o arquixo em formato xlsx (excel), mas quando baixei o arquivo em formato csv o programa aceitou
##Por essa razão fiz o meu trabalho em formato csv


def valor_minimo (filename: str, coluna):
    arquivo = pd.read_csv (filename, encoding=False)
    coluna_min = arquivo[coluna]
    min_value = coluna_min.min()
    print("Valor mínimo:",min_value)

def valor_maximo(filename: str, coluna):
    arquivo = pd.read_csv(filename, encoding=False)
    coluna_max = arquivo[coluna]
    max_value = coluna_max.max()
    print("Valor máximo: ",max_value)


def media_dos_valores(filename: str, coluna):
    arquivo = pd.read_csv(filename, encoding=False)
    coluna_media = arquivo[coluna]
    media = coluna_media.mean()
    print("Média:", media)


def soma (filename: str, coluna):
    arquivo = pd.read_csv(filename, encoding=False)
    coluna_soma = arquivo[coluna]
    soma_coluna = coluna_soma.sum()
    print("Soma da coluna escolhida:",soma_coluna)


def top_x_paises(filename: str, x: int):
    arquivo = pd.read_csv(filename)
    ordem_decrescente = arquivo.sort_values(by= ['Total_cases'],ascending=False)  # para tornar em ordem decrescente ascending= False
    print(ordem_decrescente.iloc[:x])


def criar_coluna(filename):
    # criar coluna chamada “Total_cases_per_100mil”
    # normalização por 100.000 habitantes.
    arquivo = pd.read_csv(filename)
    pop_normalizada = arquivo['Population'] / 100
    arquivo['Total_cases_per_100mil'] = arquivo['Total_deaths'] / pop_normalizada
    print ("Quantidade de casos por 100.000 habitantes:")
    print(arquivo)
