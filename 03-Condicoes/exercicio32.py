#Faça um programa que leia um ano qualquer e mostre se ele é bissexto.
import sys

ano = str(input('Olá! Eu verifico se o ano é bissexto.\n' \
'Me informe um ano qualquer: ')).strip()

n = [str(i)for i in ano]
if n[4]:
    print('Ano não suportado! Informe apenas 4 dígitos!')
    sys.exit()

if n[2:] == ['0', '0']:
    nn = ''.join(n)
    ina = int(nn) % 400
    if ina != 0:
        print(f'O ano {ano} não é bissexto!')
    else:
        print(f'O ano {ano} é bissexto!')
else:
    nn = ''.join(n)
    ina = int(nn) % 4
    if ina != 0:
        print(f'O ano {ano} não é bissexto!')
    else:
        print(f'O ano {ano} é bissexto!')