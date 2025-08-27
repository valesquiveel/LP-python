ct = 0
soma = 0
ct20 = 0
print('Digite [-1] para sair')

while True:
    valor = int(input('Digite um número: '))
    if valor == -1:
        break
    ct += 1
    soma += valor
    if valor >= 20:
        ct20 += 1

media = soma / ct
print(f'Quantidade de valores digitados: {ct}')
print(f'Soma dos valores digitados: {soma}')
print(f'Média dos valores digitados: {media:.2f}')  
print (f'Quantidade de valores digitados maior do que 20: {ct20}')      