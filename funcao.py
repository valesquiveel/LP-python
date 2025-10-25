def mostra_valor(valor):
    print(f'Valor recebido {valor}')

if __name__ == '__main__':
    print('Sem return (sem viariável):')
    mostra_valor(f': {5}')
    mostra_valor(f': {23.5}')

    print('Sem return (Com viariável)')
    v_inteiro = 43
    mostra_valor(v_inteiro)
    v_real = 37.5
    mostra_valor(v_real)