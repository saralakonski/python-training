# Gera uma assinatura profissional de e-mail a partir de informações fornecidas pelo usuário, utilizando operações com strings, concatenação, organização de texto e análise da quantidade de caracteres.
# Generates a professional email signature from user-provided information, using string operations, concatenation, text organization, and character count analysis.

full_name = input("Insira seu nome completo: ")
occupation = input("Informe o seu cargo: ")
company = input("Informe o nome da empresa: ")
professional_email = input("Informe seu e-mail profissional: ")
phone = input("Informe seu telefone: ")
city = input("Informe sua cidade: ")
linkedin = input("Insira o link do seu perfil no LinkedIn: ")
portfolio = input("Insira o link do seu portfólio profissional: ")
professional_bio = input("Insira uma pequena biografia profissional para o seu perfil: ")

print("=" * 50)
print("\t\t" + full_name)
print("=" * 50)
print("\n")
print("Cargo: " + occupation + "\t | Empresa: " + company + "\nCidade: " + city + "\t | Telefone: " + phone + "\nE-mail: " + professional_email + "\nLinkedIn: " + 
linkedin + "\nPortfólio: " + portfolio)
print("\n")
print(professional_bio)
print("=" * 50)
print("\n")
print("Análise de caracteres")
print("\n")
print("Nome: " + str(len(full_name)) + " caracteres" + "\nCargo: " + str(len(occupation)) + " caracteres" + "\nEmpresa: " + str(len(company)) + " caracteres" "\nBiografia: "
+ str(len(professional_bio)) + " caracteres" + "\nTotal: " + str(len(full_name + occupation + company + professional_bio)) + " caracteres")
print("=" * 50)

