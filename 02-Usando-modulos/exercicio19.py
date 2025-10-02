# Um professor quer sortear um dos seus quatro alunos para apagar o quadro. 
# Faça um programa que ajude ele,
# lendo o nome dos alunos e escrevendo na tela o nome do escolhido.

import random

def sorteio(x):
    sort = random.choice(x)
    print(f'O nome aluno sorteado foi: {sort}')

a1 = str(input('Informe o nome do aluno: '))
a2 = str(input('Informe o nome do aluno: '))
a3 = str(input('Informe o nome do aluno: '))
a4 = str(input('Informe o nome do aluno: '))
nome = [a1, a2, a3, a4]

sorteio(nome)