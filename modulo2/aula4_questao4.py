#entrada
quantia= int(input('Digite a quantia em reais: '))

#calculos
notas100= int(quantia/100)
notas50= int((quantia-(notas100*100))/50)
notas20= int((quantia-(notas100*100)-(notas50*50))/20)
notas10= int((quantia-(notas100*100)-(notas50*50)-(notas20*20))/10)
notas5= int((quantia-(notas100*100)-(notas50*50)-(notas20*20)-(notas10*10))/5)
notas2= int((quantia-(notas100*100)-(notas50*50)-(notas20*20)-(notas10*10)-(notas5*5))/2)
notas1= int((quantia-(notas100*100)-(notas50*50)-(notas20*20)-(notas10*10)-(notas5*5)-(notas2*2))/1)

#saida
print(f'{notas100} nota(s) de R$100,00')
print(f'{notas50} nota(s) de R$50,00')
print(f'{notas20} nota(s) de R$20,00')
print(f'{notas10} nota(s) de R$10,00')
print(f'{notas5} nota(s) de R$5,00')
print(f'{notas2} nota(s) de R$2,00')
print(f'{notas1} nota(s) de R$1,00')