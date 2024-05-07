genero= str(input('Qual o seu gênero (F ou M? '))
idade= int(input('Qual a sua idade? '))
anos_servico= int(input('Quantos anos de serviço? '))

print(f'{(genero=='F' and idade>60) or (genero=='M' and idade>=65) or (anos_servico>=30) or (idade>=60 and anos_servico>=25)}') 