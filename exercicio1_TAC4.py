#Nome: Giovanna Fernandes Lessa
#Data: 25/02/2021
#Versão: 1

#Importando o Biopython como sequencia:
from Bio.Seq import Seq
DNA = Seq(str(input("Digite a sequencia de DNA: ")))
DNA = DNA.upper()
complemento_DNA = DNA.complement()
#Trancrevendo a sequencia de DNA
mRNA = complemento_DNA.transcribe ()
#Traduzindo o mRNA para sua proteína correspondente
proteina = mRNA.translate()

print ("A sequencia do mRna é {}".format(mRNA))
print ("A proteína respectiva é {}".format(proteina))
