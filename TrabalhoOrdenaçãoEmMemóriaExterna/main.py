'''@package TrabalhoOrdenacaoEmMemoriaExterna
Este codigo faz a intercalacao balanceada de 3 caminhos, utilizando:
- 1 fita com dados de entrada
- 6 fitas auxiliares

O codigo eh dividido em tres partes:

Parte 1:
O arquivo com os dados de entrada eh divido em blocos de 3 e colocado nas 3 primeiras fitas, sendo que cada bloco esta ordenado

A parte 2 e parte 3 estao em um loop no qual eh chamado de passada, esse loop eh executado enquanto o numero de passadas nao alcanca o resultado de um calculo de log

Parte 2:
Os registros ate o separador de cada arquivo (que no nosso caso eh " - "), eh considerado um bloco, esses blocos sao ordenados e colocado nos proximos 3 arquivos

Parte 3:
Os blocos sao ordenados e colocados nos 3 primeiros arquivos, assim como na parte 2.

O programa termina com todos os registros ordenados em uma fita
'''

import math  # Importa biblioteca matematica

def main():
    chegou = False                                                      # Variavel para verificar o fim da parte 1
    cont = 0                                                            # Contador para limitar a parte 1
    i = 0                                                               # Indice
    bolaDaVez = ["Arquivo1-1.txt", "Arquivo1-2.txt", "Arquivo1-3.txt"]  # Vetor com o nome dos 3 primeiros arquivos
    a = ["Arquivo2-1.txt", "Arquivo2-2.txt", "Arquivo2-3.txt"]          # Vetor com o nome dos 3 segundos arquivos
    vetAux = []                                                         # VETOR AUXILIAR PARA ORGANIZAR
    # ABRE TODOS OS PRIMEIROS ARQUIVOS AUXILIARES EM BRANCO
    arq1 = open(bolaDaVez[0], 'w')
    arq2 = open(bolaDaVez[1], 'w')
    arq3 = open(bolaDaVez[2], 'w')
    # FECHA
    arq1.close()
    arq2.close()
    arq3.close()
    """
            ## PARTE 1

    """
    arquivoOriginal = open("Arquivo Primario.txt")                      # Abre o arquivo a ser organizado

    while chegou == False:
        linha = arquivoOriginal.readline()                              # Le cada linha do arquivo original
        # Caso um bloco nao fique com exatos 3 registros, esse if o trata
        if linha == '':                                                 # Se a linha eh o final, pare
            chegou = True                                               # Chegou recebe true para sair do loop
            vetAux.sort()                                               # Ordena o vetor a ser escrito no arquivo
            arq = open(bolaDaVez[i], 'a')                               # Abre o arquivo para escrever os registros
            arq.writelines(vetAux)                                      # Escreve o vetor no arquivo aberto
            arq.close()                                                 # Fecha o arquivo
            print("CHEGOU NO FINAL DO 1")                               # Print para dizer que acabou o primeiro passo
        else:
            if cont < 2:
                vetAux.append(linha)
                cont += 1
            else:
                vetAux.append(linha)
                vetAux.sort()                                           # Ordena o vetor auxiliar depois de os registros inseridos
                arq = open(bolaDaVez[i], 'a')                           # Abre o arquivo para atualizar
                vetAux.append('-\n')                                    # Insere um separador de blocos
                arq.writelines(vetAux)                                  # Escreve o vetor auxiliar no final do arquivo
                arq.close()
                cont = 0                                                # Cont recebe 0 para preencher outro bloco
                vetAux = []                                             # Limpa o vetor auxiliar
                if i == 2:                                              # Muda o indice para mudar de arquivo
                    i = 0
                else:
                    i += 1

    arquivoOriginal.close()

    '''
            ## INICIO DAS PASSADAS

    '''

    n = 720                                                             # Numero total de registros
    m = 3                                                               # Numero de registros no primeiro bloco
    f = 6                                                               # Numero de fitas

    passada = 0                                                         # Comeco das passadas

    while passada <= math.ceil(math.log(n / m) / math.log(f)):          # Enquanto as passadas nao alcancarem o calculo, faca:
        '''
                ## PARTE 2

        '''

        # Abre os arquivos para leitura
        arq1 = open(bolaDaVez[0], 'r')
        arq2 = open(bolaDaVez[1], 'r')
        arq3 = open(bolaDaVez[2], 'r')
        # Abre e fecha as 3 primeiras fitas para zera-las
        arq21 = open(a[0], 'w')
        arq22 = open(a[1], 'w')
        arq23 = open(a[2], 'w')
        arq21.close()
        arq22.close()
        arq23.close()

        arq1Fechado = 0
        arq2Fechado = 0
        arq3Fechado = 0

        # Se arqFechado = 0 - A variavel percorre o arquivo
        # Se arqFechado = 1 - A variavel encontrou um separador de blocos, entao ela tera que esperar as outras chegarem tambem para voltarem a ser 0
        # Se arqFechado = 2 - A variavel chegou no final do arquivo

        # LinhaDo1 - Variavel que percorre o arquivo 1 dos 3 a ser comparados
        # LinhaDo2 - Variavel que percorre o arquivo 2 dos 3 a ser comparados
        # LinhaDo3 - Variavel que percorre o arquivo 3 dos 3 a ser comparados

        i = 0                                                           # Setando o indice para 0
        while arq1Fechado != 2 and arq2Fechado != 2 and arq3Fechado != 2:
            arq21 = open(a[i], 'a')

            linhaDo1 = arq1.readline()                                  # Le a linha do primeiro arquivo
            if linhaDo1 == '-\n':                                       # Tratamento caso a linha seja igual a um separador de blocos
                linhaDo1 = arq1.readline()
            if linhaDo1 != '':                                          # Se for igual a '' quer dizer que chegou no final do arquivo
                linhaDo1 = int(linhaDo1)
                arq1Fechado = 0
            else:
                arq1.close()
                arq1Fechado = 2
                linhaDo1 = 9000                                         #LinhaDo1 recebe um valor muito alto para que nao seja comparado menor que nenhuma das outras linhas
            #####
            linhaDo2 = arq2.readline()                                  # Le a linha do segundo arquivo
            if linhaDo2 == '-\n':                                       # Tratamento caso a linha seja igual a um separador de blocos
                linhaDo2 = arq2.readline()
            if linhaDo2 != '':                                          # Se for igual a '' quer dizer que chegou no final do arquivo
                linhaDo2 = int(linhaDo2)
                arq2Fechado = 0
            else:
                arq2.close()
                arq2Fechado = 2
                linhaDo2 = 9000                                         #LinhaDo2 recebe um valor muito alto para que nao seja comparado menor que nenhuma das outras linhas
            ####
            linhaDo3 = arq3.readline()                                  # Le a linha do terceiro arquivo
            if linhaDo3 == '-\n':                                       # Tratamento caso a linha seja igual a um separador de blocos
                linhaDo3 = arq3.readline()
            if linhaDo3 != '':                                          # Se for igual a '' quer dizer que chegou no final do arquivo
                linhaDo3 = int(linhaDo3)
                arq3Fechado = 0
            else:
                arq3.close()
                arq3Fechado = 2
                linhaDo3 = 9000                                         #LinhaDo3 recebe um valor muito alto para que nao seja comparado menor que nenhuma das outras linhas

            while arq1Fechado == 0 or arq2Fechado == 0 or arq3Fechado == 0:
                # Se linhaDo1 for menor que linhaDo2 e linhaDo3:
                if arq1Fechado == 0 and linhaDo1 < linhaDo2 and linhaDo1 < linhaDo3:
                    linhaDo1 = str(linhaDo1) + '\n'                     # Converte para string e pula uma linha
                    arq21.writelines(linhaDo1)                          # Escreve a linha no final do arquivo
                    linhaDo1 = arq1.readline()                          # Le outra linha
                    if linhaDo1 == '':                                  # Se chegar no final do arquivo, nao abri-lo
                        arq1.close()
                        arq1Fechado = 2
                        linhaDo1 = 999
                    if linhaDo1 == "-\n":                               # Se chegar no final do bloco
                        arq1Fechado = 1                                 # ArqFechado = 1, para nao entrar mais nesse bloco
                        linhaDo1 = 999                                  # Atribui um valor alto a linha, para continuar as comparacoes
                    else:
                        linhaDo1 = int(linhaDo1)                        # Se nao, converta para inteiro, para continuar as comparacoes
                # Se linhaDo2 for menor que linhaDo1 e linhaDo3:
                if arq2Fechado == 0 and linhaDo2 < linhaDo1 and linhaDo2 < linhaDo3:
                    linhaDo2 = str(linhaDo2) + '\n'                     # Converte para string e pula uma linha
                    arq21.writelines(linhaDo2)                          # Escreve a linha no final do arquivo
                    linhaDo2 = arq2.readline()                          # Le outra linha
                    if linhaDo2 == '':                                  # Se chegar no final do arquivo, nao abri-lo
                        arq2.close()
                        arq2Fechado = 2
                        linhaDo2 = 999
                    if linhaDo2 == '-\n':                               # Se chegar no final do bloco
                        linhaDo2 = 999                                  # Atribui um valor alto a linha, para continuar as comparacoes
                        arq2Fechado = 1                                 # ArqFechado = 1, para nao entrar mais nesse bloco
                    else:
                        linhaDo2 = int(linhaDo2)                        # Se nao, converta para inteiro, para continuar as comparacoes
                # Se linhaDo3 for menor que linhaDo1 e linhaDo2:
                if arq3Fechado == 0 and linhaDo3 < linhaDo1 and linhaDo3 < linhaDo2:
                    linhaDo3 = str(linhaDo3) + '\n'                     # Converte para string e pula uma linha
                    arq21.writelines(linhaDo3)                          # Escreve a linha no final do arquivo
                    linhaDo3 = arq3.readline()                          # Le outra linha
                    if linhaDo3 == '':                                  # Se chegar no final do arquivo, nao abri-lo
                        arq3.close()
                        arq3Fechado = 2
                        linhaDo3 = 999
                    if linhaDo3 == "-\n":                               # Se chegar no final do bloco
                        linhaDo3 = 999                                  # Atribui um valor alto a linha, para continuar as comparacoes
                        arq3Fechado = 1                                 # ArqFechado = 1, para nao entrar mais nesse bloco
                    else:
                        linhaDo3 = int(linhaDo3)                        # Se nao, converta para inteiro, para continuar as comparacoes
            # Se nao estiver chegado no final dos 3 arquivos:
            if arq1Fechado != 2 and arq2Fechado != 2 and arq3Fechado != 2:
                arq21.writelines('-\n')                                 # Escreva o separador do bloco
                arq21.close()
            if i == 2:                                                  # Mudanca de indice para mudar de arquivo destino
                i = 0
            else:
                i += 1

        print("CHEGOU NO FINAL DO 2")

        '''
            ## PARTE 3

        '''
        # Abre os arquivos para leitura
        arq21 = open(a[0], 'r')
        arq22 = open(a[1], 'r')
        arq23 = open(a[2], 'r')
        # Abre e fecha as 3 primeiras fitas para zera-las
        arq11 = open(bolaDaVez[0], 'w')
        arq12 = open(bolaDaVez[1], 'w')
        arq13 = open(bolaDaVez[2], 'w')

        arq11.close()
        arq12.close()
        arq13.close()

        arq1Fechado = 0
        arq2Fechado = 0
        arq3Fechado = 0
    i = 0                                                               # Setando o indice para 0

        # Mesma logica da parte 2
        while arq1Fechado != 2 and arq2Fechado != 2 and arq3Fechado != 2:
            arq = open(bolaDaVez[i], 'a')

            linhaDo1 = arq21.readline()
            if linhaDo1 != '':
                linhaDo1 = int(linhaDo1)
                arq1Fechado = 0
            else:
                arq1.close()
                arq1Fechado = 2
                linhaDo1 = 9000
            #####
            linhaDo2 = arq22.readline()
            if linhaDo2 != '':
                linhaDo2 = int(linhaDo2)
                arq2Fechado = 0
            else:
                arq2.close()
                arq2Fechado = 2
                linhaDo2 = 9000
            ####
            linhaDo3 = arq23.readline()
            if linhaDo3 != '':
                linhaDo3 = int(linhaDo3)
                arq3Fechado = 0
            else:
                arq3.close()
                arq3Fechado = 2
                linhaDo3 = 9000

            while arq1Fechado == 0 or arq2Fechado == 0 or arq3Fechado == 0:
                if arq1Fechado == 0 and linhaDo1 < linhaDo2 and linhaDo1 < linhaDo3:
                    linhaDo1 = str(linhaDo1) + '\n'
                    arq.writelines(linhaDo1)
                    linhaDo1 = arq21.readline()
                    if linhaDo1 == '':
                        arq1.close()
                        arq1Fechado = 2
                        linhaDo1 = 999
                    if linhaDo1 == "-\n":
                        arq1Fechado = 1
                        linhaDo1 = 999
                    else:
                        linhaDo1 = int(linhaDo1)
                if arq2Fechado == 0 and linhaDo2 < linhaDo1 and linhaDo2 < linhaDo3:
                    linhaDo2 = str(linhaDo2) + '\n'
                    arq.writelines(linhaDo2)
                    linhaDo2 = arq22.readline()
                    cont = 0
                    if linhaDo2 == '-\n':
                        linhaDo2 = 999
                        arq2Fechado = 1
                    if linhaDo2 == '':
                        arq2.close()
                        arq2Fechado = 2
                        linhaDo2 = 999
                    else:
                        linhaDo2 = int(linhaDo2)
                if arq3Fechado == 0 and linhaDo3 < linhaDo1 and linhaDo3 < linhaDo2:
                    linhaDo3 = str(linhaDo3) + '\n'
                    arq.writelines(linhaDo3)
                    linhaDo3 = arq23.readline()
                    if linhaDo3 == "-\n":
                        linhaDo3 = 999
                        arq3Fechado = 1
                    if linhaDo3 == '':
                        arq3.close()
                        arq3Fechado = 2
                        linhaDo3 = 999
                    else:
                        linhaDo3 = int(linhaDo3)
            if arq1Fechado != 2 and arq2Fechado != 2 and arq3Fechado != 2:
                arq.writelines('-\n')
                arq.close()
            if i == 2:
                i = 0
            else:
                i += 1
        ##

        print("CHEGOU NO FINAL DO 3\n")

        passada += 1  # Incrementa +1  na passada
if __name__ == "__main__":
    main()
