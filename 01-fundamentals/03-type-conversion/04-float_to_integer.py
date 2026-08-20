# Solicita um número decimal, converte para float e inteiro, e exibe os resultados e os tipos.
# Requests a decimal number, converts it to a float and an integer, and displays the conversion results and data types.

decimal_number = input("Digite um número decimal: ")
float_number = float(decimal_number)
int_number = int(float_number)

print(f"""
Número informado: {decimal_number}
Tipo do número informado: {type(decimal_number)}
Número convertido para flutuante: {float_number}
Tipo no número convertido para flutuante: {type(float_number)}
Número convertido para inteiro: {int_number}
Tipo do número convertido para inteiro: {type(int_number)}
""")
