# Gera credenciais de acesso para colaboradores a partir de informações como nome, sobrenome, 
# ano de admissão, departamento e unidade, utilizando string indexing para extrair e combinar caracteres específicos.
# Generates employee access credentials from information such as first name, last name, 
# admission year, department, and unit, using string indexing to extract and combine specific characters.

name = input("Digite o nome do colaborador: ")
last_name = input("Digite o sobrenome do colaborador: ")
admission_year = input("Informe o ano de admissão do colaborador: ")
department = input("Informe o código de departamento do colaborador: ")
unit =  input("Informe a unidade/filial de trabalho do colaborador: ")

print("=" * 50)
print("\t\t ACCESS CREDENTIAL GENERATOR")
print("=" * 50)
print("\nEMPLOYEE INFORMATION")
print("\nNome: " + name)
print("Sobrenome: " + last_name)
print("Departamento: " + department)
print("Unidade: " + unit)
print("Ano de admissão: " + admission_year)
print("\nCREDENTIAL INFORMATION")
print("\nCódigo do colaborador: " + name[0] + last_name[0] + department[-1] + admission_year[-2] + admission_year[-1])
print("Unidade de Referência: " + unit[0] + unit[1] + unit[-2] + unit[-1])
print("Credencial Temporária: " + name[0] + last_name[-1] + department[0] + department[-1] + unit[-1] + admission_year[-1])
print("\n")
print("=" * 50)
