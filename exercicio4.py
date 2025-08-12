nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

media = (nota1 + nota2)/2

if media >= 7:
    print(f"a média do aluno foi {media} e ele está APROVADO")

elif media < 5:
    print (f"a média do aluno foi {media} e ele está REPROVADO")

else:
    print(f"a média do aluno foi {media} e ele está de RECUPERAÇÃO")