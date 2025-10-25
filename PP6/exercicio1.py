def mostrar_dados(mensagem, numero):
    print("\n--- Função foi chamada ---")
    print(f"A mensagem digitada foi: {mensagem}")
    print(f"O número digitado foi: {numero}")

if __name__ == '__main__':
    msg_usuario = input("Digite uma mensagem: ")
    num_usuario = float(input("Digite um número: "))
    mostrar_dados(msg_usuario, num_usuario)
