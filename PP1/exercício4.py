print("----------Ordem crescente de dois valores----------")
valor1 = int(input('Digite o primeiro número: '))
valor2 = int(input('Digite o segundo número: '))

if valor1 > valor2: 
    print(f"Os números em ordem crescente: {valor2} e {valor1}")
elif valor1 < valor2:
    print(f'Os números em ordem crescente: {valor1} e {valor2}')
else:
    print('Os numeros são iguais')