soma = 0
for i in range (0, 500 + 1, 1):
    if i % 3 == 0 and i % 2 != 0:
        soma += i

print(f'A soma de todos os números ímpares e múltiplos de três entre 1 e 500 é: {soma}')