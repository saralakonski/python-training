# Solicita um número, converte para inteiro e flutuante, exibe os tipos e os resultados de conversão.
# Requests a number, converts it to an integer and a float, and displays the conversion results and data types.

number = input("Digite um número inteiro: ")
int_number = int(number)
float_number = float(int_number)

print(f"""
Número informado: {number}
Tipo do número informado: {type(number)}
Número convertido para inteiro: {int_number}
Tipo no número convertido para inteiro: {type(int_number)}
Número convertido para flutuante: {float_number}
Tipo do número convertido para flutuante: {type(float_number)}
""")