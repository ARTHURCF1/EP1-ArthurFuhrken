#Jogo de Craps por Arthur Correa Fuhrken:

#Importando número randômico inteiro:

from random import randint

#Função para a aposta em Pass Line na dase Come Out:

def comeout(apostaPL,soma,fase):
    lucroPL=0
    if soma==7 or soma==11:
        lucroPL=apostaPL*2
    elif soma!=2 and soma!=3 and soma!=12:
        fase="Point"
    return lucroPL,fase

#Função para a aposta em Pass Line na fase Point:

def point(apostaPL,soma,npoint,fase):
    lucroPL=0
    if soma==npoint:
        lucroPL=apostaPL*2
        fase="Come Out"
    elif soma==7:
        fase="Come Out"
    else:
        fase="Point"
            
    return lucroPL,fase
                
#Função para a aposta em Field:
                
def field(apostaF,soma):
    if soma==5 or soma==6 or soma==7 or soma==8:
        lucroF=0
    elif soma==2:
        lucroF=apostaF*3
    elif soma==12:
        lucroF=apostaF*4
    else:
        lucroF=apostaF*2
    return lucroF

#Função para a aposta em Any Craps:
    
def anycraps(apostaAC,soma):
    lucroAC=0
    if soma==2 or soma==3 or soma==12:
        lucroAC=apostaAC*8
    
    return lucroAC
        
#Função para a aposta em Twelve:
        
def twelve(apostaT,soma):
    lucroT=0
    if soma==12:
        lucroT=apostaT*31

    return lucroT

#Código para o jogo de Craps:
    
    #Função que define as apostas:
    
def jogo(tipoaposta,fichas):
    while True:
        print("Quantas fichas você deseja apostar em ",tipoaposta,"? ")
        fichasapostadas=int(input())
        if fichasapostadas>=0 and fichasapostadas<=fichas:
            break
        else:
            print("Erro! Você só pode apostar um valor menor que ",fichas," e maior ou igual a zero.\n")
    return fichasapostadas

    #Função que define se a pessoa deseja continuar o jogo ou não:
    
def continuar():
    while True:
        desejo=input("Deseja continuar?(sim ou não)\n")
        if desejo=="sim" or desejo=="não":
            break
    return desejo

  #Define se a pessoa deseja ou não jogar Craps:

while True:
    desejo=input("Olá, você deseja jogar Craps(sim ou não)? \n")
    if desejo=="sim" or desejo=="não":
        break

    #Corpo principal do programa:
    
fichas=randint(100,999)
npoint=0

if desejo=="sim":
    nome=input("Ótimo, qual o seu nome? \n")
    while fichas>0:
        print(nome,", você tem ",fichas,"fichas.\n")
        print("Você está na fase Come Out")
        desejo=continuar()
        if desejo=="sim":
            fase="Come Out"
            apostaPL=jogo("Pass Line",fichas)
            fichas-=apostaPL
            while True:
                apostaF=jogo("Field",fichas)
                fichas-=apostaF
                apostaAC=jogo("Any Craps",fichas)
                fichas-=apostaAC
                apostaT=jogo("Twelve",fichas)
                fichas-=apostaT
                dado1=randint(1,6)
                dado2=randint(1,6)
                soma=dado1+dado2
                print("A soma dos dados resultou em",soma,"(dado1=",dado1,"e dado2=",dado2,")\n")
                
                if apostaPL>0:
                    if fase=="Come Out":
                        resultadoPL,fase=comeout(apostaPL, soma, fase)
                        if resultadoPL!=0:
                            print("Você ganhou",resultadoPL,"fichas em Pass Line.")
                        elif fase=="Point":
                                npoint=soma
                                print("Você mudou de fase e sua aposta em Pass Line foi mantida, agora está na fase Point e seu número point é",npoint,".\n")
                        else:
                            print("Você perdeu",apostaPL,"fichas em Pass Line.")
                    else:
                        resultadoPL,fase=point(apostaPL, soma, npoint, fase)
                        if resultadoPL!=0 and fase=="Come Out":
                            print("Você ganhou",resultadoPL-apostaPL,"fichas em Pass Line.")
                        elif fase=="Come Out":
                            print("Você perdeu",apostaPL,"fichas em Pass Line.")
                        else:
                            print("Você continuou na fase Point.")
                else:
                    resultadoPL=0
                
                resultadoF=field(apostaF, soma)
                if resultadoF!=0:
                        print("Você ganhou",resultadoF-apostaF,"fichas em Field.")
                else:
                        print("Você perdeu",apostaF,"fichas em Field.")
     
                resultadoAC=anycraps(apostaAC, soma)
                if resultadoAC!=0:
                        print("Você ganhou",resultadoAC-apostaAC,"fichas em Any Craps.")
                else:
                        print("Você perdeu",apostaAC,"fichas em Any Craps.")

                resultadoT=twelve(apostaT, soma)
                if resultadoT!=0:
                        print("Você ganhou",resultadoT-apostaT,"fichas em Twelve.")
                else:
                        print("Você perdeu",apostaT,"fichas em Twelve.\n")

                fichas+=resultadoPL+resultadoF+resultadoAC+resultadoT
                
                if fase=="Come Out":
                    break
                print(nome,", você tem ",fichas,"fichas.\n")
                print("Você está na fase point. O seu número point é",npoint,".\n")
                
        else:
            print ("Obrigado e volte sempre!")
            break
    if fichas==0:
        print("Suas fichas acabaram, obrigado por jogar e volte sempre!")
    else:
        print("Adeus, você terminou o jogo com",fichas,"fichas.")
else:
   print("Obrigado e volte sempre!")
        
        
        
        
        
        
        
        
        
        
        
        