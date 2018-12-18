from random import choice

print('###############################################')
print('BEM VINDO AO JOGO DE ADIVINHAÇÃO')
print('TENDE ADIVINHAR AS RESPOSTAS DAS PERGUNTAS')
print('SERÃO 4 DESAFIOS PARA TESTAR SEU CONHECIMENTO')
print('VAMOS COMEÇAR')
print('###############################################')

arquivo = open('charada.txt','r').readlines()
perguntas = [linha.strip().split('-') for linha in arquivo]

def escolhe_charada(perguntas):
    charada = choice(perguntas)
    return charada

def jogar():
    tentativas = 3
    ganhou = 0
    rodadas = len(perguntas)
    charada = escolhe_charada(perguntas)
    while(tentativas > 0):
        print(charada[0])
        resposta = input('QUAL A RESPOSTA? (RESPOSTA EM INTEIRO ):  ')
        if str(charada[1]) == resposta:
            print('VOCÊ ACERTOU !!!!')
            print('VAMOS PARA PROXIMA PERGUNTA !!!!')
            tentativas = 3
            rodadas -= 1
            charada = escolhe_charada(perguntas)
        else:
            tentativas = tentativas - 1
            print('VOCÊ ERROU !!!!')
            print('VOCÊ AINDA TEM',tentativas,'CHANCES !!!')

        if rodadas < 0:
            print('AS PERGUNTAS ACABARAM VOCÊ É O VENCEDOR PARABENS !!!!')
            ganhou = 1
            tentativas = 0

    if tentativas == 0 and ganhou == 0:
        print('SUAS CHANCES ACABARAM, QUEM SABE NA PROXIMA !!!!')


if __name__ == "__main__":
    jogar()