#Faça um programa que leia o comprimento 
#do cateto oposto e do cateto adjacente de um triângulo retângulo. 
#Calcule e mostre o comprimento da hipotenusa.

import math
def function(co,ca):

    hi = math.hypot(co,ca)
    print(f'Hipotenusa: {hi:.2f}')

x = float(input('Informe o cateto oposto: '))
y = float(input('informe o cateto adjacente: '))

function(x,y)