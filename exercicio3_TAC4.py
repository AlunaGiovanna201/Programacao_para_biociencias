#Nome: Giovanna Fernandes Lessa
#Data: 25/02/2021
#Versão: 1

import sys
from Bio import SeqIO
from Bio.Blast.Applications import NcbiblastxCommandline


codigo_desconhecido = sys.argv[1]
dataBase = sys.argv[2]
meuOutput = open(r"C:/Users/Giovanna/Desktop/pythonProject/meuOutput.txt", 'w')

#abrir arquivo que vai ser lido
for i in SeqIO.parse(open(codigo_desconhecido),"fasta"):
    arquivo = str("{}.fasta").format(i.id)
    refArquivoSaida = open(arquivo,"w")
    SeqIO.write(i, refArquivoSaida, "fasta")
    refArquivoSaida.close()
    sequencia = arquivo
    meuOutput = r"C:/Users/Giovanna/Desktop/pythonProject/meuOutput.txt"
    refArquivoSaida.close()
    blastx_path = r"C:\Program Files\NCBI\blast-2.10.1+\bin\blastx.exe"

    linha_de_comando_blastx = NcbiblastxCommandline(cmd=blastx_path, query=sequencia,subject=dataBase, outfmt=6,out=meuOutput, evalue=0.05)
    stdout, stderr = linha_de_comando_blastx()

    print("Executando busca local:")


    print("Fim da busca local...")
    print("__" * 25)

    # Abrindo resultado
    blast_result = open(meuOutput, "r")

    qseqid = 0 #query sequence id
    sseqid = 1 # subject sequence id
    pident = 2
    length = 3
    mismatch = 4
    gapopen = 5
    qstart = 6
    qend = 7
    sstart = 8
    send = 9
    evalue = 10 # expect value
    bitscore = 11 # bit score

    results = blast_result.read()
    s = results.split('\n')
    melhorscore = '0'
    Evalue = 0
    encontrada = '0'

    for linha in s:
        hit = linha.split('\t')
        if len(hit) != 12:
            break
        if float(melhorscore) < float(hit[bitscore]):
            busca = hit[qseqid]
            melhorscore = hit[bitscore]
            Evalue = hit[evalue]
            encontrada = hit[sseqid]
            print("Sequência de busca: %s" % i.id)
            print("Sequência encontrada: %s" % encontrada)
            print("Score = %s" % melhorscore)
            print("E-value = %s" % Evalue)
            print("__" * 25)