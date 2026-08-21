# Solicita informações de contato, calcula a quantidade de caracteres e exibe uma ficha organizada.
# Requests contact information, calculates the number of characters, and displays an organized contact form.

full_name = input("Digite seu nome completo: ")
phone = input("Digite seu número de telefone: ")
email = input("Digite seu e-mail: ")
city = input("Digite sua cidade: ")
state = input("Digite seu estado: ")
observation = input("Informações adicionais de contato: ")

print("=" * 50)
print("\t\tREGISTRO DE CONTATO\t\t")
print("=" * 50)
print("\n")
print("INFORMAÇÕES PESSOAIS")
print("\tNome: " + full_name + "\n\tCidade: " + city + "\n\tEstado: " + state)
print("\n")
print("INFORMAÇÕES DE CONTATO")
print("\tTelefone: " + phone + "\n\tE-mail: " + email)
print("\n")
print("NOTAS")
print("\tInformações adicionais: " + observation)
print("\tCaracteres do nome: " + str(len(full_name)) + "\n\tCaracteres de informações adicionais: " + str(len(observation)) + "\n\tTotal de caracteres: " + str(len(full_name + observation)))
print("=" * 50)
