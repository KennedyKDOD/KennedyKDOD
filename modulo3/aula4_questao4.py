distancia= int(input('Qual a distância da entrega em quilômetros: '))
peso= float(input('Qual o peso do pacote em quilogramas: '))

if distancia<=100:
    print(f'O valor do frete é R${1.00*peso:.2f}.')

if distancia > 100 and distancia<=300:
    print(f'O valor do frete é R${1.50*peso:.2f}.')

if distancia > 300:
    print(f'O valor do frete é R${2.00*peso:.2f}.')

if peso > 10:
    print('Será cobrada uma taxa de R$10,00 pelo peso do pacote ser superior a 10kg.')