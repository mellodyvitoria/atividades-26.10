def calculadora():
    print("Escolha a operação:")
    print("1. Soma")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")

    escolha = input("Digite o número da operação (1/2/3/4): ")

    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))

    if escolha == '1':
        resultado = num1 + num2
        operacao = "Soma"
    elif escolha == '2':
        resultado = num1 - num2
        operacao = "Subtração"
    elif escolha == '3':
        resultado = num1 * num2
        operacao = "Multiplicação"
    elif escolha == '4':
        if num2 != 0:
            resultado = num1 / num2
            operacao = "Divisão"
        else:
            return "Erro: Divisão por zero não é permitida."
    else:
        return "Erro: Operação inválida."

    return f"{operacao} de {num1} e {num2} = {resultado}"

print(calculadora())
