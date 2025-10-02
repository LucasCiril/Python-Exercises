#Crie um programa que leia um número Real qualquer pelo teclado 
#E mostre na tela a sua porção Inteira.

from math import trunc

def inteiro(x):
    conver = trunc(x)
    print(f'O valor digitado foi {x} e sua porção inteira é {conver} ')

any = float(input('Insira qualquer número: '))
inteiro(any)