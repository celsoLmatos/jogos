import forca
import adivinhacao

def escolhe_jogo():
    print("*********************************")
    print("*******Escolha o seu jogo!*******")
    print("*********************************")

    continua = False
    while(not continua):
        print("(1) Forca (2) Adivinhação")
        jogo = int(input("Qual jogo? "))
        if(jogo == 1):
            print("Jogando forca")
            forca.jogar()
        elif(jogo == 2):
            print("Jogando adivinhação")
            adivinhacao.jogar()
        escolhe = int(input('Quer continuar jogando ? (1) Sim (2) Não'))
        if escolhe == 2:
            continua = True
            print('Obrigado por Jogar !!!')
        elif escolhe == 1:
            print('Continue Jogando')


if(__name__ == "__main__"):
    escolhe_jogo()
