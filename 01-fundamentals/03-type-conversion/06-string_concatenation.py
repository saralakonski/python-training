# Criação de uma pequena ficha de identificação do usuário.
# Creates a small user identification form.

name = input("Digite seu nome: ")
age = int(input("Digite sua idade: "))
city = input("Digite a sua cidade: ")
occupation = input("Digite sua profissão: ")
str_age = str(age)

print("Seja bem-vindo(a), " + name + "! Confira abaixo os seus dados:")
print("Nome: " + name + "\nIdade: " + str_age + "\nCidade: " + city + "\nProfissão: " + occupation)