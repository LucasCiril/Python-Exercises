#Escreva um programa que pergunte o salário de um funcionário e 
#calcule o valor do seu aumento. Para salários superiores a R$1250,00, 
#calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.

salario = int(input('Qual o salário do funcionário? R$ '))

if salario <= 1250:
    aumento1 = (salario * 15 /100)  + salario
    print(f'Quem ganhava R${salario:.2f} agora ganha R${aumento1:.2f}')
else:
    aumento1 = (salario * 10 /100)  + salario
    print(f'Quem ganhava R${salario:.2f} agora ganha R${aumento1:.2f}')
