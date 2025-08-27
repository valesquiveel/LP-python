ct = 0
soma = 0
ctAprovado = 0
ctReprovado = 0
print('Digite [-1] para sair')

while True:
    notas = float(input(f'Digite a nota do aluno Nº{ct + 1}: '))
    if notas == - 1:
        break
    ct += 1
    soma += notas
    if notas >= 5:
        ctAprovado += 1
    else:
        ctReprovado += 1
media = soma / ct
print(f'Quantidade de alunos que fizeram a prova: {ct}')
print(f'Quantidade de alunos aprovados: {ctAprovado}')
print(f'Quantidade de alunos reprovados: {ctReprovado}')
print (f'Média da turma: {media:.2f}')