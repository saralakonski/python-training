# Solicita ao usuário que digite dois números inteiros e exibe o resultado das operações aritméticas entre eles
# Requests the user to input two integer numbers and displays the result of arithmetic operations between them

first_number = int(input("Digite o primeiro número: "))
second_number = int(input("Digite o segundo número: "))

print(f"""
Confira o resultado das operações entre {first_number} e {second_number}:
Soma: {first_number + second_number}
Subtração: {first_number - second_number}
Multiplicação: {first_number * second_number}
Divisão: {first_number / second_number}
""")