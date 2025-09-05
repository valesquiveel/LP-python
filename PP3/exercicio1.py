ct = 0
cti = 0
ctp = 0
somai = 0
somap = 0
print('Digite [0] para sair da repetição')
while True:
    valor = float(input(f'Digite o {ct + 1}º número: '))
    if valor == 0:
        break
    if valor % 2 == 0:
        ctp += 1
        somap += valor
        mediaP = somap / ctp
    else:
        cti += 1
        somai += valor
        mediaI = somai / cti
        
mediaP = somap / ctp
mediaI = somai / cti
print(f'Média dos números pares: {mediaP}')
print(f'Média dos números ímpares: {mediaI}')