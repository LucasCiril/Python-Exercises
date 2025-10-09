# Escreva um programa que leia a velocidade de um carro. 
# Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. 
# A multa vai custar R$7,00 por cada Km acima do limite.
import sys
velocidade = int(input('Informe a velocidade do carro: '))
if velocidade > 80:
    x = [str(i) for i in range(81, velocidade+1)]
    z = len(x)
    calculo = 7 * z
    print('-=-' * 23)
    print(f'PARADO! Você excedeu a velocidade permitida! Você foi multado em R${calculo}')
    print('-=-' * 23)
else:
    print('-=-' * 19)
    print('Muito bem! Você está no limite de velocidade permitido!')
    print('-=-' * 19)
