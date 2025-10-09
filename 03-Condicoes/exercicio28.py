# Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 
# e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. 
# O programa deverá escrever na tela se o usuário venceu ou perdeu.
import random
from time import sleep

print('-=-' * 15)
print('Bem vindo ao Jogo da Adivinhação!\nTente adivinhar um número entre 0 e 5!')
print('-=-' * 15)
num = int(input('Em que número eu pensei? '))
print('Processando...')
sleep(3)
x = random.randint(0,5)

if num == x:
    print(f'Parabéns! Você adivinhou o mesmo número que eu! Eu pensei no número {x}')

else:
    print(f'Parabén! Você errou! O número que eu pensei foi o {x}')