Nome: Giovanna Fernandes Lessa
Data: 21/01/2021
Versao: 3

import sys
from estatisticas_pandas_script import valor_minimo, valor_maximo, media_dos_valores,soma,criar_coluna,top_x_paises

def main():
    nome_arquivo = sys.argv[1]

    coluna_minimo = input("Digite o nome da coluna que deseja calcular o valor mínimo: ")
    valor_minimo(nome_arquivo, coluna_minimo)
    coluna_maximo = input("Digite o nome da coluna que deseja calcular o valor máximo: ")
    valor_maximo(nome_arquivo, coluna_maximo)
    coluna_media = input("Digite o nome da coluna que deseja calcular a média: ")
    media_dos_valores(nome_arquivo, coluna_media)
    soma_total_coluna = input("Digite o nome da coluna que você deseja calcular a soma: ")
    soma (nome_arquivo, soma_total_coluna)
    valor_x = int(input("Digite número de linhas que você deseja visualizar: "))
    top_x_paises(nome_arquivo,valor_x)
    criar_coluna(nome_arquivo)

if __name__ == "__main__":
    main()
