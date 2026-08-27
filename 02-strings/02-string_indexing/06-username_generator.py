# Gera uma sugestão de nome de usuário corporativo a partir de informações básicas de um funcionário, utilizando posições específicas das strings.
# Generates a suggested corporate username from basic employee information by using specific string positions.

full_name = input("Insira seu nome completo: ")
birth_year = input("Informe o ano do seu nascimento: ")
department = input("Insira o código do seu setor: ")

print("=" * 50)
print("\t\tUSERNAME GENERATOR")
print("=" * 50)
print("\nNome: " + full_name)
print("Ano de nascimento: " + birth_year)
print("Departamento: " + department)
print("\nUsername sugerido: " + full_name[0] + full_name[-1] + department[0] + department[-1] + birth_year[-1] + birth_year[-2])