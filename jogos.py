import forca
import adivinhacao
import charada

def escolhe_jogo():
    print("*********************************")
    print("*******Escolha o seu jogo!*******")
    print("*********************************")

    continua = False
    while(not continua):
        print("(1) Forca (2) Adivinhação (3) Charadas (0) Sair")
        jogo = int(input("Qual a Opção Escolhe? :"))
        if(jogo == 1):
            print("Jogando forca")
            forca.jogar()
        elif(jogo == 2):
            print("Jogando adivinhação")
            adivinhacao.jogar()
        elif (jogo == 3):
            print("Jogando adivinhação")
            charada.jogar()
        elif(jogo == 0):
            continua = True
            print('Obrigado por Jogar !!!')
            continue
        escolhe = int(input('Quer continuar jogando ? (1) Sim (2) Não'))
        if escolhe == 2:
            continua = True
            print('Obrigado por Jogar !!!')
        elif escolhe == 1:
            print('Continue Jogando')


if(__name__ == "__main__"):
    escolhe_jogo()
