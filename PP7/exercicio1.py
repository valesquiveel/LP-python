def positivo_nulo_negativo(numero):
    if numero > 0:
        print("Valor Positivo")
    elif numero == 0:
        print("Valor Nulo")
    else:
        print("Valor Negativo")

if __name__ == '__main__':
    valor = float(input("Digite um número: "))
    positivo_nulo_negativo(valor)