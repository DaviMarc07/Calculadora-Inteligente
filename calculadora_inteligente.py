import math

def calculadora_inteligente():
    """
    Calculadora Inteligente com 10 operações matemáticas diferentes.
    Desenvolvida para praticar conceitos básicos de Python.
    """
    while True:
        print("\n--- Calculadora Inteligente ---")
        print("Escolha a operação desejada ou digite 'sair' para encerrar:")
        print("1. Soma (+)")
        print("2. Subtração (-)")
        print("3. Multiplicação (*)")
        print("4. Divisão (/)")
        print("5. Potenciação (**)")
        print("6. Raiz Quadrada (√)")
        print("7. Resto da Divisão (%)")
        print("8. Divisão Inteira (//)")
        print("9. Logaritmo (base 10)")
        print("10. Fatorial (!)")

        opcao = input("Digite o número da operação ou 'sair': ").strip().lower()

        if opcao == 'sair':
            print("Encerrando a calculadora. Até mais!")
            break

        if opcao not in [str(i) for i in range(1, 11)]:
            print("Opção inválida. Tente novamente.")
            continue

        try:
            # Operações que precisam de dois números
            if opcao in ['1', '2', '3', '4', '5', '7', '8']:
                num1 = float(input("Digite o primeiro número: "))
                num2 = float(input("Digite o segundo número: "))

                if opcao == '1':
                    print(f"Resultado: {num1} + {num2} = {num1 + num2}")
                elif opcao == '2':
                    print(f"Resultado: {num1} - {num2} = {num1 - num2}")
                elif opcao == '3':
                    print(f"Resultado: {num1} * {num2} = {num1 * num2}")
                elif opcao == '4':
                    if num2 == 0:
                        print("Erro: Divisão por zero não é permitida.")
                    else:
                        print(f"Resultado: {num1} / {num2} = {num1 / num2}")
                elif opcao == '5':
                    print(f"Resultado: {num1} ** {num2} = {num1 ** num2}")
                elif opcao == '7':
                    print(f"Resultado: {num1} % {num2} = {num1 % num2}")
                elif opcao == '8':
                    if num2 == 0:
                        print("Erro: Divisão por zero não é permitida.")
                    else:
                        print(f"Resultado: {num1} // {num2} = {num1 // num2}")

            # Raiz Quadrada
            elif opcao == '6':
                num = float(input("Digite o número para calcular a raiz quadrada: "))
                if num < 0:
                    print("Erro: Não existe raiz quadrada de número negativo.")
                else:
                    print(f"Resultado: √{num} = {math.sqrt(num)}")

            # Logaritmo
            elif opcao == '9':
                num = float(input("Digite o número para calcular o logaritmo (base 10): "))
                if num <= 0:
                    print("Erro: O logaritmo só é definido para números positivos.")
                else:
                    print(f"Resultado: log10({num}) = {math.log10(num)}")

            # Fatorial
            elif opcao == '10':
                num = int(input("Digite um número inteiro para calcular o fatorial: "))
                if num < 0:
                    print("Erro: Fatorial não é definido para números negativos.")
                else:
                    print(f"Resultado: {num}! = {math.factorial(num)}")

        except ValueError:
            print("Entrada inválida. Por favor, insira números válidos.")

if __name__ == "__main__":
    calculadora_inteligente()
