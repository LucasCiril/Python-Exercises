#Faça um programa que leia um ângulo qualquer e mostre na tela 
# o valor do seno, cosseno e tangente desse ângulo.

from math import radians, sin, cos, tan

def function(x):
    gr = radians(x)
    sen = sin(gr)
    coss = cos(gr)
    tang = tan(gr)
    
    if x == 90:
        print(f'Seno: {sen:.4f}\nCosseno: {coss:.4f}\nTangente: Não existe.')
    else:
        print(f'Seno: {sen:.4f}\nCosseno: {coss:.4f}\nTangente: {tang:.4f}')
    
number = float(input('Informe um ângulo para ser calculado: '))
function(number)