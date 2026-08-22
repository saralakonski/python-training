# Gera um perfil profissional organizado a partir de informações fornecidas pelo usuário, utilizando operações com strings, concatenação, formatação de texto e análise da quantidade de caracteres.
# Generates an organized professional profile from user-provided information, using string operations, concatenation, text formatting, and character count analysis.

full_name = input("Infome seu nome completo: ")
occupation = input("Informe seu cargo: ")
professional_area = input("Informe sua área de atuação profissional: ")
company = input("Informe o nome de sua empresa: ")
city = input("Informe sua cidade: ")
state = input("Informe seu estado: ")
country = input("Informe seu país: ")
email = input("Informe seu e-mail: ")
professional_description = input("Digite um breve resumo profissional: ")
primary_skill = input("Informe uma habilidade principal: ")
secondary_skill = input("Informe uma habilidade secundária: ")

print("=" * 50)
print("\t\tPERFIL PROFISSIONAL")
print("=" * 50)
print("\t\tInformações Pessoais")
print("\n")
print("Nome: " + full_name + "\nCargo: " + occupation + "\nÁrea de atuação: " + professional_area + 
"\nEmpresa: " + company + "\nCidade: " + city + "\tEstado: " + state + "\tPaís: " + country + "\nE-mail: " + email)
print("\n")
print("\t\tDescrição profissional" + "\n" + professional_description)
print("\n")
print("\t\tHabilidades\n" + primary_skill + "\n" + secondary_skill)
print("\n")
print("\t\tAnálise de caracteres")
print("Nome Completo: " + str(len(full_name)) + " caracteres" + "\nDescrição Profissional: " + str(len(professional_description)) + " caracteres" +
"\nHabilidade 1: " + str(len(primary_skill)) + " caracteres" "\nHabilidade 2: " + str(len(secondary_skill)) + " caracteres" + "\nTotal: " + str(len(full_name + professional_description + primary_skill + secondary_skill))
+ " caracteres")
print("\n")
print("=" * 50)