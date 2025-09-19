#Faça um algoritmo que leia o preço de um produto
#e mostre o seu novo preço, com 5% de desconto.

def n_preço(n1):
    desc = (n1 * 5) / 100
    r_pre = n1 - desc
    print(f'O preço com desconto fica {r_pre:.02f}')

b = float(input('Insira o preço original do produto: '))
n_preço(b)