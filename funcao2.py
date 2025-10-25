def soma_dois(v1, v2):
    soma = v1 + v2
    return soma

if __name__ == '__main__':
    valor1 = int(input('Digite um valor: '))
    valor2 = int(input('Digite outro valor: '))
    v_retorna = soma_dois(valor1, valor2)
    print(f'Soma dos valores: {v_retorna}')