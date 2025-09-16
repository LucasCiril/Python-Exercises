#Faça um programa que leia um número inteiro qualquer
#E mostre na tela a sua tabuada.

def tabu():
    num = int(input('Escolha um número: '))
    print(f'O número escolhido foi: {num}. Sua tabuada até dez a seguir:')

    for i in range(1,11):
        mult = num *i
        print(mult)

tabu()