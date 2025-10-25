
def calcular_idade(ano_nascimento, ano_atual):
    idade = ano_atual - ano_nascimento
    return idade


if __name__ == '__main__':
    nasc = int(input("Digite o seu ano de nascimento (ex: 1990): "))
    atual = int(input("Digite o ANO ATUAL (ex: 2025): "))
    idade_calculada = calcular_idade(nasc, atual)
    print(f"Você completa (ou completou) {idade_calculada} anos.")