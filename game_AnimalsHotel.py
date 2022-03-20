#importando a biblioteca do sistema operacional para conseguir limpar a tela.
from os import system 

#Objetivo dessa funcao, limpar a tela a cada fase avançada para n ficar muito poluido
# e reescrever as regras do jogo.
def cabecalhoRegras():
    system('clear')
    print('GAME - HOTEL DOS ANIMAIS')
    print(' C = CÃO | R = RATO | G = GATO | O = OSSO | Q = QUEIJO')
    print('Regras:')
    print('>> 1 - O rato(R) não pode ficar ao lado do gato(G).')
    print('>> 2 - O cão(C) não pode ficar ao lado do osso(O).')
    print('>> 3 - O gato(G) não pode ficar ao lado do cão(C).')
    print('>> 4 - O queijo(Q) não pode ficar ao lado do rato(R).')
    #criando matriz padrão 
    matriz = montaMatriz()
    #mostrando a matriz paddão usuario
    print('Especificando posições:')
    printaMatriz(matriz)

#objetivo dessa funcao, retornar uma nova matriz conforme a fase passada no parametro
def montaMatriz (fase=0):
    if fase==0:
        return [[1,2,3,4],[5,6,7,8]]
    elif fase==1:
        return [['*','*','_','G'],['R','_','*','*']]
    elif fase==2:
        return [['_','*','*','*'],['*','C','_','_']]
    elif fase==3:
        return [['_','*','*','*'],['_','G','_','*']]
    elif fase==4:
        return  [['_','_','_','*'],['*','R','*','*']]

#Pritando a lista em formado de tabela/Matriz
def printaMatriz(lista):
    for x in lista:
        print(x)
    print('\n')

#Validacao de valor digitado inteiro/ saber se o quarto está disponivel ou não, para isso faço uma tupla que recebe
#todos os quartos ocupados por fase.
def validaOpcao(pergunta,*quartosOcupados):
    while True:
        try:
            res = int(input(pergunta))
        except:
            print('Valor digitado inválido...')
            continue    
        if res not in quartosOcupados:
            break
        else:
            print('Quarto ocupado!')
            continue
    return res

#Fases do Jogo
def fases(level):
    global matriz
    if level==1:
        cabecalhoRegras()
        #deixando a matriz conforme a 1ª fase e mostrando
        matriz = montaMatriz(1)
        print('Bem vindo a fase 1!')
        print('Nessa fase você deve hospedar 1 rato e 1 gato.')
        printaMatriz(matriz)
        #recebendo posicoes
        posicaoRato = validaOpcao('Em qual quarto hospedar o rato?\n>>',1,2,4,5,7,8 )    
        posicaoGato =  validaOpcao('Em qual quarto hospedar o gato?\n>>',1,2,4,5,7,8,posicaoRato)
        #Validando posicoes
        if posicaoRato == 6 and posicaoGato == 3:
            print('Fase 2 Desbloqueada!\n')
            return True
        else:
            return False

    elif level==2:
        cabecalhoRegras()
        #deixando a matriz conforme a 2ª fase e mostrando
        matriz = montaMatriz(2)
        print('Bem vindo a fase 2!')
        print('Nessa fase você deve hospedar 2 cães e 1 osso.')
        printaMatriz(matriz)
        #recebendo posicoes
        posicaoCao1 = validaOpcao('Em qual quarto hospedar o primeiro cão?\n>>',2,3,4,5,6)    
        posicaoCao2 = validaOpcao('Em qual quarto hospedar o segundo cão?\n>>',2,3,4,5,6,posicaoCao1)
        posicaoOsso = validaOpcao('Em qual quarto hospedar o osso?\n>>',2,3,4,5,6,posicaoCao1,posicaoCao2)
        #se a posicao do osso for igual a 1, ja está correto, pois cachorro pode ficar do lado do cachorro
        if posicaoOsso == 1:
            return True
        else:
            return False

    elif level==3:
        cabecalhoRegras()
        #deixando a matriz conforme a 3ª fase e mostrando
        matriz = montaMatriz(3)
        print('Bem vindo a fase 3!')
        print('Nessa fase você deve hospedar 1 gato, 1 rato e 1 osso.')
        printaMatriz(matriz)
        #recebendo posicoes
        posicaoGato = validaOpcao('Em qual quarto hospedar o gato?\n>>',2,3,4,8)
        posicaoRato = validaOpcao('Em qual quarto hospedar o rato?\n>>',2,3,4,8,posicaoGato)    
        posicaoOsso = validaOpcao('Em qual quarto hospedar o osso?\n>>',2,3,4,8,posicaoGato,posicaoRato)    
        #se a posicao do rato for igual a 1, ja está correto, pois gato e osso podem ficar do lado do gato existente
        if posicaoRato == 1 and posicaoOsso==5:
            return True
        else:
            return False

    elif level==4:
        cabecalhoRegras()
        #deixando a matriz conforme a 4ª fase e mostrando
        matriz = montaMatriz(4)
        print('Bem vindo a fase 4!')
        print('Nessa fase você deve hospedar 2 queijos e 1 osso.')
        printaMatriz(matriz)
        #recebendo posicoes
        posicaoQueijo1 = validaOpcao('Em qual quarto hospedar o primeiro queijo?\n>>',4,5,6,7,8)
        posicaoQueijo2 = validaOpcao('Em qual quarto hospedar o segundo queijo?\n>>',4,5,6,7,8,posicaoQueijo1)
        posicaoOsso = validaOpcao('Em qual quarto hospedar o primeiro o osso?\n>>',4,5,6,7,8,posicaoQueijo1,posicaoQueijo2)
        #se a posicao do osso for a 2 ja está correto, sem necessidade de validar as demais
        if posicaoOsso==2:
            print('Você ganhou!!!! :)')
            print('Jogo desenvolvido por: Joao Victor Linzmeyer Marszalek\n')
            return True
        else:
            return False
#PROGRAMA PRINCIPAL
fase = 1
while fase and fase<=4:
    resultado = fases(fase)
    if resultado:
        fase+=1
    else:
        print('Você perdeu!')
        break