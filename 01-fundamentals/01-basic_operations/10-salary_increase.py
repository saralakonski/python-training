# Programa que solicita o salário, calcula um aumento de 10% e 20%, exibe o valor dos aumentos, o novo salário e a diferença entre eles.
# Program that requests the salary, calculates 10% and 20% increases, and displays the increase amounts, new salaries, and the difference between them.
salary = float(input("Digite seu salário: R$ "))

salary_increase_10 = salary * 0.10
# Em Python, números decimais utilizam ponto. 0,10 é interpretado como uma tupla (0, 10).
# In Python, decimal numbers use a dot. 0,10 is interpreted as a tuple (0, 10).
new_salary_10 = salary + salary_increase_10
salary_increase_20 = salary * 0.20
new_salary_20 = salary + salary_increase_20
difference = new_salary_20 - new_salary_10

print(f"""
O salário informado é: R$ {salary:.2f}
10% de aumento: {salary_increase_10:.2f}
Novo salário: {new_salary_10:.2f}
20% de aumento: {salary_increase_20:.2f}
Novo salário: {new_salary_20:.2f}
Diferença: {difference:.2f}
""")

