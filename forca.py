from random import choice


def ler_arquivo():
    arquivo = open('palavras.txt', 'r').readlines()
    palavras = [linha.strip() for linha in arquivo]
    palavra = choice(palavras)
    array = [letra for letra in palavra]
    return array


def acertei(array, chute, forca):
    for x in range(len(array)):
        if array[x].upper() == chute.upper():
            forca[x] = (array[x])
    return forca


def cria_forca(array):
    forca = ['__'] * len(array)
    return forca


def sera_ganhou(array, forca):
    if array == forca:
        print("Palavra com {} letras escolha uma letra para completar? {} {}".format(len(array),
                                                                                     ' '.join(map(str, forca)), ' : '))
        print('Você acertou a palavra é: {}'.format(''.join(map(str, forca))))
        print("Fim do jogo")
        return True
    else:
        return False


def sera_enforcou(enforcou, jogadas_restantes):
        print('Você ainda tem {} tetativas!!'.format(jogadas_restantes))
        if enforcou:
            print('Você perdeu, tente novamente depois !!')
            return True
        else:
            return False


def jogar():

    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")

    enforcou = False
    ganhou = False

    array = ler_arquivo()
    forca = cria_forca(array)

    print(forca)

    errou = 0
    tentativas = len(array)
    while not enforcou and not ganhou:
        chute = input("Palavra com {} letras escolha uma letra para completar? {} {}".format(len(array),
                                                                                             ' '.join(map(str, forca)),
                                                                                             ' : '))
        chute = chute.strip()
        forca = acertei(array, chute, forca)

        if chute.lower() in array:
            ganhou = sera_ganhou(array, forca)
        else:
            errou += 1
            enforcou = sera_enforcou(errou == tentativas, tentativas - errou)


if __name__ == "__main__":
    jogar()
