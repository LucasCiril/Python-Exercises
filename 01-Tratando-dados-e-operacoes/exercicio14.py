#Escreva um programa que converta uma temperatura 
#Digitando em graus Celsius e converta para graus Fahrenheit.

def temp(x):
    c_f = (x*1.8) + 32
    print(f'A temperatura em graus é {x} Graus, e {c_f:.02f} em Farenheit.')

graus = float(input("Informe a temperatura em graus: "))
temp(graus)