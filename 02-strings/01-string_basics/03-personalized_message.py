# Solicita informações pessoais e exibe uma mensagem personalizada e organizada.
# Requests personal information and displays a personalized and organized message.

name = input("Digite seu nome: ")
city = input("Digite sua cidade: ")
hobby = input("Qual é o seu hobby favorito? ")
favorite_food = input("Qual é a sua comida preferida? ")

print("Olá, " + name + "! Confira suas informações abaixo:")
print("=" * 40)
print("Nome: " + name + "\nCidade: " + city + "\nHobby: " + hobby + "\nComida preferida: " + favorite_food)
print("=" * 40)

