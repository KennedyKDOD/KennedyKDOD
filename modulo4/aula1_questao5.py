N= int(input('Digite a quantidade de respondentes: '))
n=N
idade_total= 0

while n>=1:
    idade= int(input('Digite a idade: '))
    idade_total= idade_total+idade
    n= n-1

print(f'A média das idades é: {idade_total/N}')
