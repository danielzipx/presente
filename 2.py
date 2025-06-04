import random

numero_secreto = random.randint(1,6)

i = 0
arma = 5
tentativa = 0
roleta_russa = ''

for i in range(0,5):
    roleta_russa = input('Quer jogar? S/N: ')
    if roleta_russa == '':
        print('carregando...')
        if roleta_russa == 'N':
            print('Por que você está aqui ainda então?')
            break
            
        if roleta_russa == 'S':
            roleta_russa = random.randint(1,6)
            
            if roleta_russa == numero_secreto:
                print('deletando, \nC:\Windows\System32')
                print('tchauzinho...')
                break
            
            if roleta_russa != numero_secreto:
                print('Você sobreviveu tente novamente...')    
    else:
        print('Não foi dessa vez :( \nNa proxima eu sei que você consegue :)')



