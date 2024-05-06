#entradas
comprimento= int(input("Qual o comprimento do terreno em metros? "))
largura= int(input("Qual a largura do terreno em metros? "))
preco_metro2= float(input("Qual o preço do metro quadrado da região? "))

#conversão
area_m2= comprimento * largura
preco_total= preco_metro2 * area_m2

#saída
print(f'O terreno possui {area_m2}m2 e custa R${preco_total:,.2f}')

