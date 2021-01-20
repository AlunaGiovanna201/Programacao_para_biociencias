# Programacao_para_biociencias
Repositório criado para a diciplina de Programação para Biociências 20\1
def homo_poli(dna):
    global indicador_homopolimeros
    dna = dna.upper()  # Deixa todos os caracteres maiusculos para realizar a contagem
    lista_homopolimeros = []
    contido_em_homopolimeros = False  # Essa variável indica se o loop já está dentro de um homopolímero.
    indicador = 0
    if dna == '':
        return 'Isso é invalido para a função'
    else:
        for nt in dna:
            if not contido_em_homopolimeros:
                try:
                    if nt == dna[indicador + 1] and nt == dna[indicador + 2] and nt in 'A, T, C, G':
                        contido_em_homopolimeros = True
                        indicador_homopolimeros = indicador + 1
                        comprimento_homopolimeros = 1
                except:
                    break
            else:
                if nt == dna[indicador - 1]:
                    comprimento_homopolimeros += 1
                else:
                    contido_em_homopolimeros = False
                    lista_homopolimeros.append((dna[indicador - 1], comprimento_homopolimeros, indicador_homopolimeros))
            indicador += 1
        if contido_em_homopolimeros:
            lista_homopolimeros.append((dna[indicador - 1], comprimento_homopolimeros, indicador_homopolimeros))
        else:
            lista_homopolimeros.append((dna[indicador - 1], comprimento_homopolimeros, indicador_homopolimeros))
        return lista_homopolimeros
print(homo_poli(''))
print('lista de homopolímeros:', homo_poli('ACTTTTGTCTAAACCCCCCGTCCTATATATAACT'))
