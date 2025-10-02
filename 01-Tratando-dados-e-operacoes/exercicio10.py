#Crie um programa que leia quanto dinheiro uma pessoa
#tem na carteira e mostre quantos dólares ela pode comprar
#Obs: Considere 1 US$ 1.00 = R$ 3,27

def calc():
    origin = float(input('Informe quanto de dinheiro você tem na carteira: '))
    dol = float(3.27)
    camb = origin / dol

    print(f'Você tem {origin} reais e pode comprar {camb:.2f} dólares.')
calc()