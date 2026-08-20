# Programa de cadastro de colaborador.
# Employee registration program.

# Personal Information
full_name = input("Digite o nome do colaborador: ")
age = int(input("Informe a idade do colaborador: "))
city = input("Informe a cidade do colaborador: ")
state = input("Informe o estado do colaborador: ")

# Professional Information
job_title = input("Informe o cargo do colaborador: ")
department = input("Informe o departamento do colaborador: ")
years_of_experience = int(input("Anos de experiência do colaborador na função: "))

# Financial Information
current_salary = float(input("Informe o salário atual do colaborador: R$ "))
desired_increase_percentage = int(input("Informe o percentual de reajuste desejado: "))

# Benefits
meal_allowance = float(input("Informe o valor do vale-alimentação mensal: R$ "))
transport_allowance = float(input("Informe o valor do vale transporte mensal: R$ "))

# Calculate
increase_amount = (desired_increase_percentage / 100 ) * current_salary
salary_after_increase = increase_amount + current_salary
monthly_compensation = salary_after_increase + meal_allowance + transport_allowance

print(f"""
=========== REGISTRO DE COLABORADOR ===========

INFORMAÇÕES PESSOAIS
Nome: {full_name}
Idade: {age}
Cidade: {city}
Estado: {state}

INFORMAÇÕES PROFISSIONAIS
Cargo: {job_title}
Departamento: {department}
Experiência: {years_of_experience} anos

INFORMAÇÕES FINANCEIRAS
Salário atual: R$ {current_salary:.2f}
Reajuste desejado: {desired_increase_percentage}%
Valor do reajuste: R$ {increase_amount:.2f}
Salário após o reajuste: R$ {salary_after_increase:.2f}
Vale-alimentação: R$ {meal_allowance:.2f}
Vale-transporte: R$ {transport_allowance:.2f}
Remuneração mensal: R$ {monthly_compensation:.2f}
===============================================
""")