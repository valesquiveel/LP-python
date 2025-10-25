def verificar_maioridade(idade):
    if idade >= 18:
        return "Maior de idade"
    else:
        return "Menor de idade"

if __name__ == '__main__':
    idade_usuario = int(input("Digite a sua idade: "))
    status = verificar_maioridade(idade_usuario)
    print(f"Status: {status}")