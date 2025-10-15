#Desenvolva um programa que leia o comprimento de três retas
#e diga ao usuário se elas podem ou não formar um triângulo.

print('-=-' * 10)
print('Analisador de triângulos')
print('-=-' * 10)

a = float(input('Informe o primeiro segmento: '))
b = float(input('Informe o segundo segmento: '))
c = float(input('Informe o terceiro segmento: '))

if a + b > c and a + c > b and b + c > a:
    print('Os segmentos FORMAM um triângulo!')
else:
    print('Os segmentos NÃO FORMAM um triângulo!')
