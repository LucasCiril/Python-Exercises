# Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome “SANTO”.

cidade = str(input('Me diga o nome da cidade do seu nascimento: ')).strip()

print(cidade[:5].upper() == 'SANTO')