import random

numero_secreto = random.randint(1,6)

i = 0
arma = 5
tentativa = 0
roleta_russa = ''

for i in range(arma):
    roleta_russa = float(input('Escolha um numero de 1 a 6:'))
    
    if roleta_russa != numero_secreto:
        print(input('Você sobreviveu tente novamente...'))
    if roleta_russa == numero_secreto:
        print('deletando, \nC:\Windows\System32')
        print('tchauzinho...')
        break
