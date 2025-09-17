#Faça um programa que leia a largura e a altura de uma parede em metros
#Calcule a sua área e a quantidade de tinta necessária para pintá-la.
#Obs: Sabe-se que cada 1l de tinta pinta uma área de 2m²


def cal():
    area = lar * alt
    print(f'A área da parede é {area}m².')
    litros = area / 2
    print(f'São necessários {litros:.02f} litros para pintar a parede.')

lar = float(input('Informe a largura da parede: '))
alt = float(input('Informe a altura da parede: '))

cal()