#Faça um programa que leia uma frase pelo teclado 
#e mostre quantas vezes aparece a letra “A”, 
#em que posição ela aparece a primeira vez 
#e em que posição ela aparece a última vez.

frase = str(input('Digite qualquer frase: ')).upper().strip()

print(f'A letra A aparece na frase {frase.count('A')} vez(vezes)')
print(f'A primeira aparição da letra na frase: {frase.find('A')+1}')
print(f'A última aparição da letra na frase: {frase.rfind('A')+1}')