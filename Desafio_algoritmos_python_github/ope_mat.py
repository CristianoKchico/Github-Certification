# Calculadora das 4 operações matemáticas básicas

def calculadora():
    # Coleta dois números do usuário
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))

    # Exibe o menu de operações
    print("\nEscolha a operação:")
    print("[1] Adição (+)")
    print("[2] Subtração (-)")
    print("[3] Multiplicação (*)")
    print("[4] Divisão (/)")

    # Solicita a escolha do usuário
    operacao = input("Digite o número da operação desejada (1/2/3/4): ")

    # Realiza a operação com base na escolha
    if operacao == "1":
        resultado = num1 + num2
        print(f"\nResultado: {num1} + {num2} = {resultado:.2f}")
    elif operacao == "2":
        resultado = num1 - num2
        print(f"\nResultado: {num1} - {num2} = {resultado:.2f}")
    elif operacao == "3":
        resultado = num1 * num2
        print(f"\nResultado: {num1} * {num2} = {resultado:.2f}")
    elif operacao == "4":
        if num2 != 0:  # Verifica se o divisor é diferente de zero
            resultado = num1 / num2
            print(f"\nResultado: {num1} / {num2} = {resultado:.2f}")
        else:
            print("\nErro: Divisão por zero não é permitida.")
    else:
        print("\nOperação inválida. Tente novamente.")

# Chama a função
calculadora()
