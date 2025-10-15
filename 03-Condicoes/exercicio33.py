#Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

x = int(input('Informe um valor: '))
y = int(input('Informe um valor: '))
z = int(input('Informe um valor: '))

if x > y and x > z:
    print(f'O maior número é {x}')
elif y > x and y > z:
    print(f'O maior número é {y}')
elif z > x and z > y:
    print(f'O maior número é {z}')

if x < y and x < z:
    print(f'O menor número é {x}')
elif y < x and y < z:
    print(f'O menor número é {y}')
elif z < x and z < y:
    print(f'O menor número é {z}')
