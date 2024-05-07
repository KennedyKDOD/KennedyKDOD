idade= int(input('Digite sua idade: '))
ja_jogou= bool(input('Já jogou pelo menos 3 jogos de tabuleiro? '))
quant_vitorias= int(input('Quantos jogos já venceu? '))

print(f'Apto para ingressar no clube de jogos de tabuleiro: {(idade>=16 and idade<=18) and (ja_jogou==True) and (quant_vitorias>=1)}')
