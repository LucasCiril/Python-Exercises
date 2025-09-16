#Desenvolva um programa que leia duas notas de um aluno
#Calcule e mostre a média das notas.

import sys

print('Esse programa calcula sua média.')

def media():
    n1 = int(input('Informe sua primeira nota: '))
    n2 = int(input('Informe sua segunda nota: '))
    soma = n1 + n2
    med = soma /2

    if med < 6:
        print(f'Sua média é {med} e está abaixo do ideal!')
    elif med >10:
        print('Média impossível! Tente novamente.')
        sys.exit()
    elif med == 6:
        print(f'Sua média é {med} e está no limite do ideal!')
    else:
        print(f'Sua média é {med} e está acima do mínimo! ')

media()