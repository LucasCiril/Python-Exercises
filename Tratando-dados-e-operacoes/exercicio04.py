#Crie um programa que leia algo do teclado e mostre na tela o seu
#tipo primitivo e demais informações.

info = input('Digite qualquer coisa: ')
print(f'O tipo primitivo do que foi digitado é: {type(info)}' )
print(f'Existem espaços? {info.isspace()}')
print(f'É um número? {info.isnumeric()}')
print(f'É alfabético? {info.isalpha()}')
print(f'É alfanumérico? {info.isalnum()}')
print(f'Está em maiusculas? {info.isupper()}')
print(f'Está em minúsculas? {info.islower()}')
print(f'Está capitalizada? {info.istitle()}')