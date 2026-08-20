# Solicita ao usuário que digite dois números inteiros e exibe a divisão deles
# Requests the user to input two integer numbers and displays their division

first_number = int(input("Digite o primeiro número: "))
second_number = int(input("Digite o segundo número: "))

print(f"O resultado da divisão entre {first_number} e {second_number} é {first_number / second_number}.")

'''A divisão por zero não é permitida. Ponto de melhoria para o futuro:
adicionar uma verificação para garantir que o segundo número não seja zero antes de realizar a divisão.

The division by zero is not allowed. A point of improvement for the future: 
add a check to ensure that the second number is not zero before performing the division.'''