# Calcula o reajuste e o desconto de um salário e exibe o salário líquido.
# Calculates a salary increase and deduction and displays the net salary.

current_gross_salary = float(input("Informe o salário bruto: R$ "))
increase_percentage = int(input("Informe o percentual de reajuste: "))
discount_percentage = int(input("Informe o percentual de desconto: "))

increase_amount = (increase_percentage / 100) * current_gross_salary
salary_after_increase = current_gross_salary + increase_amount
discount_amount = salary_after_increase * (discount_percentage / 100)
net_salary = salary_after_increase - discount_amount

print(f"""
Salário bruto atual: R$ {current_gross_salary:.2f}
Percentual do reajuste: {increase_percentage}%
Valor do reajuste: R$ {increase_amount:.2f}
Salário após reajuste: R$ {salary_after_increase:.2f}
Percentual de desconto: {discount_percentage}%
Valor do desconto: {discount_amount:.2f}
Salário Líquido: {net_salary:.2f}
""")