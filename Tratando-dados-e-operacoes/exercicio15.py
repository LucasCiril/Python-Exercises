#Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado 
# e a quantidade de dias pelos quais ele foi alugado. 
# Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

def func(x, y):
    day = x*60
    km = y*0.15
    plus = day+km
    print(f'O carro foi usado por {x} dias, percorrendo {y:.02f} Km/h.\nO valor a ser pago é R${plus:.02f}')

days = int(input('Informe quantos dias o carro foi usado: '))
km = float(input('Informe quantos kilômetros foram percorridos: '))

func(days, km)