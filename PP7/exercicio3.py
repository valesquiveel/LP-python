def somar(v1, v2):
    resultado = v1 + v2
    print(f"O resultado de {v1} + {v2} é: {resultado}")

def subtrair(v1, v2):
    resultado = v1 - v2
    print(f"O resultado de {v1} - {v2} é: {resultado}")

def multiplicar(v1, v2):
    resultado = v1 * v2
    print(f"O resultado de {v1} x {v2} é: {resultado}")

def dividir(v1, v2):
    if v2 == 0:
        print("Não é possível dividir por zero.")
    else:
        resultado = v1 / v2
        print(f"O resultado de {v1} / {v2} é: {resultado}")

if __name__ == '__main__':
    
    operador = input("Digite a operação [+, -, x, /]: ")
    valor1 = float(input("Digite o primeiro valor: "))
    valor2 = float(input("Digite o segundo valor: "))
    
    if operador == '+':
        somar(valor1, valor2)
    elif operador == '-':
        subtrair(valor1, valor2)
    elif operador == 'x': 
        multiplicar(valor1, valor2)
    elif operador == '/':
        dividir(valor1, valor2)
    else:
        print("Operação inválida. Use +, -, x ou /.")