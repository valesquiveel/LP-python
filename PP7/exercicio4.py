def fatorial(n):
    if n == 0:
        return 1
    
    resultado = 1

    for i in range(1, n + 1):
        resultado = resultado * i
    return resultado

if __name__ == '__main__':
    numero = int(input("Digite um número inteiro para calcular o fatorial: "))
    
    if numero < 0:
        print("Fatorial não é definido para números negativos.")
    else:
        fat_resultado = fatorial(numero)
        print(f"{numero}! é {fat_resultado}")