# Solicita e exibe informações do usuário.
# Requests and displays the user's personal information.

name = input("Digite seu nome: ")
age = int(input("Digite sua idade: "))
city = input("Digite sua cidade: ")
occupation = input("Digite sua profissão: ")

print(f"""
Nome: {name}
Idade: {age}
Cidade: {city}
Profissão: {occupation}
""")