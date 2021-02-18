Nome: Giovanna Fernandes Lessa 
Data: 17/02/2021
Versao: 1
    
    
import csv

# Função criada para printa o valor mínimo encontrado no arquivo desejado
def valor_minimo(file_name: str, coluna: int):
    minimo = 999999999999
    with open(file_name, "r") as arquivo_csv:
        if file_name[-3:].lower() == "csv":
            delimitador = ","
        else:
            delimitador = "\t"
        arquivo = csv.reader(arquivo_csv, delimiter=delimitador)
        arquivo.__next__()  # Pula a primeira linha, que é o cabeçalho
        for row in arquivo:
            valor = float(row[coluna - 1])
            if valor < minimo:
                minimo = valor
            else:
                pass
    print(minimo)

# Função criada para printa o valor máximo encontrado no arquivo desejado
def valor_maximo(file_name: str, coluna: int):
    maximo = -222  #O número máximo precisa ser o primeiro número grande
    with open(file_name, "r") as arquivo_csv:
        if file_name[-3:].lower() == "csv":
            delimitador = ","
        else:
            delimitador = "\t"
        arquivo = csv.reader(arquivo_csv, delimiter=delimitador)
        arquivo.__next__()  # Pula a primeira linha, que é o cabeçalho
        for row in arquivo:
            valor = float(row[coluna - 1])
            if valor > maximo:
                maximo = valor
            else:
                pass
    print(maximo)

# Função criada para printar a média dos valores encontrados no arquivo desejado
def media(file_name: str, coluna: int):
    soma = 0
    numeros_lidos = 0
    with open(file_name, "r") as arquivo_csv:
        if file_name[-3:].lower() == "csv":
            delimitador = ","
        else:
            delimitador = "\t"
        arquivo = csv.reader(arquivo_csv, delimiter=delimitador)
        arquivo.__next__()  # Pula a primeira linha, que é o cabeçalho
        for row in arquivo:
            valor = float(row[coluna - 1])
            soma += valor
            numeros_lidos += 1
    print(soma / numeros_lidos)

# Função criada para printar a razao entre os valores encontrados nas colunas 1 e 2
def razao(file_name: str, identificador: int, coluna1: int, coluna2: int):
    identificador -= 1
    coluna1 -= 1
    print("Country	Total_cases/Total_deaths")
    coluna2 -= 1
    with open(file_name, "r") as arquivo_csv:
        if file_name[-3:].lower() == "csv":
            delimitador = ","
        else:
            delimitador = "\t"
        arquivo = csv.reader(arquivo_csv, delimiter=delimitador)
        arquivo.__next__()
        for row in arquivo:
            razao = int(row[coluna1]) / float(row[coluna2])
            print(row[identificador] + "\t{}".format(razao))
