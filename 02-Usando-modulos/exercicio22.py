#Crie um programa que leia o nome completo de uma pessoa e mostre:
#1- O nome com todas as letras maiúsculas e minúsculas.
#2- Quantas letras ao todo (sem considerar espaços).
#3- Quantas letras tem o primeiro nome.

def uper(x):
    plus= x.upper()
    minimun = x.lower()
    print(f'Seu nome maiúsculo: {plus}\nSeu nome minúsculo: {minimun}')

def leter(y):
    sep = y.split()
    carac = ''.join(sep)
    ler = len(carac)
    print(f'O nome inteiro tem {ler} letras.')

def first(z):
    sep = z.split()
    name = sep[0]
    carac = len(sep[0])
    print(f'O primeiro nome é {name} e tem {carac} letras.')
    
nome = str(input('Informe um nome: ')).strip()
uper(nome)
leter(nome)
first(nome)