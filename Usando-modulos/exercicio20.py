# O mesmo professor do desafio 19 quer sortear a ordem de apresentação de trabalhos dos alunos. 
# Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

import random

def sorteio():

    a1 = str(input('Informe o nome do aluno: '))
    a2 = str(input('Informe o nome do aluno: '))
    a3 = str(input('Informe o nome do aluno: '))
    a4 = str(input('Informe o nome do aluno: '))
    nome = [a1, a2, a3, a4]
    random.shuffle(nome)

    print(f'A sequência de apresentação é {nome} ')

sorteio()