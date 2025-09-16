#Escreva um programa que leia um valor em metros
#E o exiba convertido em centímetros e milímetros.

def covers():
    metros = int(input('Informe uma quantidade em metros: '))
    cent = metros *100
    mil= cent *100

    print(f'O valor em metros escolhido foi: {metros} m.\nConvertido em centímetros: {cent} cm\nConvertido em milimetros: {mil} ml')

covers()