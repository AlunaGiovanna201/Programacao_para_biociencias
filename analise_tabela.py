import sys
from estatisticas_script import valor_maximo, valor_minimo, media , razao

nome_do_arquivo = sys.argv[1]

coluna_minimo = int(input("Número da coluna que deseja para calcular o valor mínimo: "))
valor_minimo(nome_do_arquivo, coluna_minimo)
coluna_maximo = int(input("Número da coluna que deseja para calcular o valor máximo: "))
valor_maximo(nome_do_arquivo, coluna_maximo)
coluna_media = int(input("Número da coluna que deseja para calcular a média: "))
media(nome_do_arquivo, coluna_media)
razao_valores = input("Digite o número da coluna com o identificador das linhas e os números das duas colunas que você deseja calcular a razão separados por um espaço: ")
razao(nome_do_arquivo, int(razao_valores[0]), int(razao_valores[2]), int(razao_valores[4]))
