#Faça um programa que leia um número de 0 a 9999 
#E mostre na tela cada um dos dígitos separados.

def ls(x): 
    x = x.zfill(4)
    print(f'Unidade: {x[3]}')
    print(f'Dezena: {x[2]}')
    print(f'Centena: {x[1]}')
    print(f'Milhar: {x[0]}')
    
entry = str(input('Informe um número entre 0 e 9999: '))

print(f'Analisando o número {entry}:')

ls(entry)