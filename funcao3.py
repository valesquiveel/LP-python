def soma_valores(v1,v2):
    soma = v1 + v2
    return soma

def sub_valores(v1, v2):
    sub = v1 - v2
    return sub

if __name__ == '__main__':
    valor1 = int(input('Digite o primeiro valor: '))
    valor2 = int(input('Digite o segundo valor: '))
    operacao = str(input('[+] Somar\n [-]Subtrair\nOpção: '))
    if operacao == '+':
        ## v_retornaSoma = soma_valores(valor1, valor2)
        print(f'Soma dos valores: {soma_valores(valor1, valor2)}')
    elif operacao == '-':
       ## v_retornaSub = sub_valores(valor1,valor2)
        print(f'Subtração dos valores: {sub_valores(valor1,valor2)}')
    else:
        print('Digite uma operação válida')