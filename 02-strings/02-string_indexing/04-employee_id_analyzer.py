# Analisa um ID de funcionário e utiliza diferentes posições da string para extrair e combinar informações relevantes.
# Analyzes an employee ID and uses different string positions to extract and combine relevant information.

employee_id = input("Informe o ID do funcionário: ")

print("=" * 50)
print("\t\tID ANALYZER")
print("=" * 50)
print("\nID informado: " + employee_id)
print("\nAnálise")
print("Dois primeiros caracteres: " + employee_id[0] + employee_id[1])
print("4º caractere: " + employee_id[3])
print("5º caractere: " + employee_id[4])
print("Dois últimos caracteres: " + employee_id[-1] + employee_id[-2])
print("\nEmployee Reference: " + employee_id[0] + employee_id[1] + employee_id[3] + employee_id[-1] + employee_id[-2])
print("=" * 50)
