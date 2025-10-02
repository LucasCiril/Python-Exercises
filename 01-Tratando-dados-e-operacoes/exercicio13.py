#Faça um algoritmo que leia o salário de um funcionário
#e mostre seu novo salário, com 15% de aumento.

def gromp(batata):
    mult = (batata * 15) /100
    n_aum = batata + mult
    print(f'Parabéns! Você recebeu um aumento de 15%!\nSeu novo salário é R$ {n_aum:.02f}')

sal_ini = float(input('Informe seu salário atual: '))
gromp(sal_ini)