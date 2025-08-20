print("----------Calculadora de peso ideal----------")
sexo = str(input("Digite seu sexo *femimino ou masculino*: "))
altura = float(input('Digite sua altura em cm: '))

pesoIdeal_homem = (0.727 * altura) - 58

pesoIdeal_mulher = (0.621 * altura) - 44.7

if sexo == "feminino":
    print(f"Seu peso ideal é de {pesoIdeal_mulher:.2f}kg ")
elif sexo == "masculino":
    print(f'Seu peso ideal é de {pesoIdeal_homem:.2f}kg')
else:
    print("sexo diferente dos citados")