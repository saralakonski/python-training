# Solicita um número inteiro, converte para inteiro e string, e exibe os resultados e os tipos.
# Requests an integer, converts it to a string, and displays the conversion results and data types.

number = input("Digite um número inteiro: ")
int_number = int(number)
str_number = str(int_number)

print(f"""
Número informado: {number}
Tipo do número informado: {type(number)}
Número convertido para inteiro: {int_number}
Tipo no número convertido para inteiro: {type(int_number)}
Número convertido para string: {str_number}
Tipo do número convertido para string: {type(str_number)}
""")
