# Programa que lê um número inteiro e mostra seu antecessor e sucessor.
# Programm that reads an integer and shows its predecessor and successor.

number = int(input("Digite um número inteiro: "))

print(f"""
O número digitado é {number}
Antecessor: {number - 1}
Sucessor: {number + 1}
""")