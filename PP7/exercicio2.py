def valor_absoluto(numero):
    if numero < 0:
        return numero * -1
    else:
        return numero

if __name__ == '__main__':
    num = float(input("Digite um número: "))
    v_abs = valor_absoluto(num)
    print(f"O valor absoluto de {num} é {v_abs}")