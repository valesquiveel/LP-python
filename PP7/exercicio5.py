def calcular_inss(salario_bruto):
    if salario_bruto <= 2000:
        desconto = salario_bruto * 0.07  # 7%
    else:
        desconto = salario_bruto * 0.10  # 10%    
    return desconto

if __name__ == '__main__':
    nome = input("Nome do funcionário: ")
    sal_bruto = float(input(f"Salário bruto de {nome}: R$ "))
    valor_desconto = calcular_inss(sal_bruto)
    sal_liquido = sal_bruto - valor_desconto
    print("\n--- Holerite ---")
    print(f"Funcionário: {nome}")
    print(f"Salário Bruto: R$ {sal_bruto:.2f}")
    print(f"Desconto INSS:  R$ {valor_desconto:.2f}")
    print(f"Salário Líquido: R$ {sal_liquido:.2f}")