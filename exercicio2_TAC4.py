#Nome: Giovanna Fernandes Lessa
#Data: 25/02/2021
#Versão: 1

#Importando as bibliotecas externas
import sys
from Bio import SeqIO

codigo_desconhecido = sys.argv[1]

criar_pasta = 0
for i in SeqIO.parse(open(codigo_desconhecido),"fasta"):
    criar_pasta += 1
    nomeArquivo = str("sequencia_{}.fasta").format(criar_pasta)
    refArquivoSaida = open(nomeArquivo,"w")
    SeqIO.write(i, refArquivoSaida, "fasta")
    refArquivoSaida.close()
print ("Pastas criadas")