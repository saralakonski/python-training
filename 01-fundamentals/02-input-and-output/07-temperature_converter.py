# Solicita a temperatura em Celsius, converte para Fahrenheit e exibe o resultado.
# Requests the temperature in Celsius, converts it to Fahrenheit, and displays the result.

celsius = float(input("Digite a temperatura em Celsius: "))

fahrenheit = (celsius * 9 / 5) + 32

print(f"""
Celsius: {celsius:.1f}°C
Fahrenheit: {fahrenheit:.1f}°F
""")