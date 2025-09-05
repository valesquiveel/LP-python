ct = 0
ctm = 0
soma = 0
menor = 999999
maior = 0
print('Digite [-1] para sair da repetição')
while True:
    valor = float(input(f'Digite o {ct + 1}º valor: '))
    if valor == -1:
        break
    ct += 1
    soma += valor
    media = soma / ct
    if valor > maior:
        maior = valor
    if valor < menor:
        menor = valor
    if valor >= 50:
        ctm += 1

print(f'Quantidade de valores digitados: {ct}')
print(f'Soma: {soma}')
print(f'Média: {media}')
print(f'Maior valor: {maior}')
print(f'Menor valor: {menor}')
print(f'Valores maiores ou igual a 50: {ctm}')