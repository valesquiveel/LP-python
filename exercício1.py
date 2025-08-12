nome = str(input("Qual é o seu nome? digite: "))
print("Olá", nome, ", prazer em te conhecer!")

ano_nasc = int(input(f"Em que ano você nasceu, {nome}? irei calcular sua idade. Digite: "))
ano_atual = int(input("Em que ano estamos? Digite: "))
idade = ano_atual - ano_nasc

print("Você tem ou fará", idade, "anos em", ano_atual)