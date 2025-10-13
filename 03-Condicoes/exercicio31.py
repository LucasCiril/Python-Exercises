#Desenvolva um programa que pergunte a distância de uma viagem em Km. 
#Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km 
#e R$0,45 parta viagens mais longas.

valor = float(input('Qual a distância da sua viagem em Km? '))

if valor <= 200:
    x = valor * 0.50
    print(f'Sua viagem será de {valor}Km e seu custo será de R${x:.2f} pela viagem.')
else:
    y = valor * 0.45
    print(f'Sua viagem será de {valor}Km e seu custo será de R${y:.2f} pela viagem.')