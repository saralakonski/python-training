# Solicita informações básicas de uma pessoa e exibe uma mensagem de apresentação.
# Requests basic personal information and displays a presentation message.

name = input("Digite seu nome: ")
city = input("Digite a sua cidade: ")
occupation = input("Digite sua profissão: ")

print("Olá, " + name + "! Seja bem-vindo(a)!")
print("Confira abaixo as informações fornecidas:")
print("Nome: " + name + "\nCidade: " + city + "\nProfissão: " + occupation)