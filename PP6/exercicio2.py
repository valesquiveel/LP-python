def somar_tres_valores(v1, v2, v3):

    soma = v1 + v2 + v3
    return soma

if __name__ == '__main__':
    print("Digite três valores inteiros:")
    val1 = int(input("1º valor: "))
    val2 = int(input("2º valor: "))
    val3 = int(input("3º valor: "))
    resultado = somar_tres_valores(val1, val2, val3)
    print(f"O resultado da soma é: {resultado}")