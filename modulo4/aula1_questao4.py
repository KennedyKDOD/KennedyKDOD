n=int(input('Digite um número: '))
maior=0

while n>0:
    x= int(input('Digite outro número: '))
    if x>maior:
        maior=x
    n= n-1

if not n>0:
    print(maior)
