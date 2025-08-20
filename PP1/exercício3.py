print("----------Calculadora de distãncia entre dois pontos----------")
print("Forneça as coordenadas do ponto P:")
x1 = float(input("Digite o valor de x1: "))
y1 = float(input("Digite o valor de y1: "))
 
print("Forneça as coordenadas do ponto Q:")
x2 = float(input("Digite o valor de x2: "))
y2 = float(input("Digite o valor de y2: "))

distancia = ((x2 - x1)**2 + (y2 - y1)**2) ** 0.5

print(f"A distância entre os pontos P({x1}, {y1}) e Q({x2}, {y2}) é: {distancia:.4f}")