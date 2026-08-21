# Simula o planejamento financeiro mensal de uma pessoa, calculando receitas, despesas, reserva de investimentos e projeções financeiras.
# Simulates a person's monthly financial planning by calculating income, expenses, investment savings, and financial projections.

# Personal Information
full_name = input("Informe seu nome completo: ")
age = input("Informe sua idade: ")
city = input("Informe sua cidade: ")
occupation = input("Informe sua profissão: ")
#Conversion
age = int(age)

# Financial Information
monthly_salary = input("Informe seu salário líquido mensal: R$ ")
extra_monthly_income = input("Informe o valor da renda extra (caso tenha): R$ ")
#Conversion
monthly_salary = float(monthly_salary)
extra_monthly_income = float(extra_monthly_income)

# Fixed Expenses
rent = input("Informe o valor do aluguel: R$ ")
electricity = input("Informe o custo com energia elétrica: R$ ")
water = input("Informe o custo do consumo de água: R$ ")
internet = input("Informe o custo com internet: R$")
telephone = input("Informe o custo com plano de telefone: R$ ")
transportation = input("Informe custos com transporte: R$ ")
food = input("Informe custos com alimentação: R$ ")
#Conversion
rent = float(rent)
electricity = float(electricity)
water = float(water)
internet = float(internet)
telephone = float(telephone)
transportation = float(transportation)
food = float(food)

# Variable expenses
leisure_average_monthly = input("Informe o custo mensal com lazer: R$ ")
shopping_average_monthly = input("Informe o custo mensal com compras: R$ ")
streaming_average_monthly = input("Informe o custo mensal com assinaturas de streamming e outros: R$ ")
other_expenses_monthly = input("Informe o custo com outras despesas: R$ ")
#Conversion
leisure_average_monthly = float(leisure_average_monthly)
shopping_average_monthly = float(shopping_average_monthly)
streaming_average_monthly = float(streaming_average_monthly)
other_expenses_monthly = float(other_expenses_monthly)

# Financial planning
percentage_to_invest = input("Informe o percentual que deseja investir mensalmente: ")
months_investment = input("Informe a quantidade de meses que deseja investir: ")
#Conversion
percentage_to_invest = int(percentage_to_invest)
months_investment = int(months_investment)

#Calculate
total_income = monthly_salary + extra_monthly_income
total_fixed_expenses = rent + electricity + water + internet + telephone + transportation + food
total_variable_expenses = leisure_average_monthly + shopping_average_monthly + streaming_average_monthly + other_expenses_monthly
total_expenses_monthly = total_fixed_expenses  + total_variable_expenses
net_value = total_income - total_expenses_monthly
percentage_expenses = (total_expenses_monthly / total_income) * 100
investment_reserve = (percentage_to_invest / 100) * total_income
available_balance = net_value - investment_reserve
total_investment_reserve = investment_reserve * months_investment

print("""
========================================
        Planejador Financeiro
""")
print("""
________________________________________
DADOS PESSOAIS
""")
print("Nome: " + full_name + "\nIdade: " + str(age) + "\nCidade: " + city + "\nProfissão: " + occupation)
print("""
________________________________________
DESPESAS
\n

Despesas Fixas:
""")
print("- Aluguel: R$ " + format(rent,".2f") + "\n- Energia Elétrica: R$ " + format(electricity,".2f") + "\n- Água: R$ " + format(water,".2f")
+ "\n- Internet: R$ " + format(internet,".2f") + "\n- Telefone: R$ " + format(telephone,".2f") + "\n- Transporte: R$ " + format(transportation,".2f")
+ "\n- Alimentação: R$ " + format(food,".2f"))
print("""
Despesas Variáveis:
""")
print("- Custo médio mensal - Lazer: R$ " + format(leisure_average_monthly,".2f") + "\n- Custo médio mensal - Compras: R$ " + format(shopping_average_monthly,".2f") +
"\n- Custo médio mensal - Assinaturas: R$ " + format(streaming_average_monthly,".2f") + "\n- Custo médio mensal - Outros gastos: R$ " + format(other_expenses_monthly,".2f"))
print("""
________________________________________
PLANEJAMENTO FINANCEIRO
""")
print("- Percentual de reserva de investimentos: " + format(percentage_to_invest,".1f") + "%" + "\n- Valor mensal da reserva de investimentos: R$ " + format(investment_reserve)
+ "\n- Período de investimento: " + format(months_investment) + " meses.")
print("""
________________________________________
RESULTADO FINANCEIRO
""")
print("- Renda total: R$ " + format(total_income,".2f") + "\n- Despesas totais: R$ " + format(total_expenses_monthly,".2f") + "\n- Percentual de despesas: " + 
format(percentage_expenses,".1f") + "%" + "\n- Valor líquido: R$ " + format(net_value,".2f") + "\n- Valor mensal da reserva de investimentos: R$ "
+ format(investment_reserve,".2f") + "\n-Saldo Disponível: R$ " + format(available_balance,".2f") + "\n- Projeção acumulada de investimentos: R$ "
+ format(total_investment_reserve,".2f"))
print("""
========================================
""")
# Melhoria futura: - adicionar validações para impedir valores negativos ou percentuais fora de uma faixa válida.
#                  - validar a renda total antes de realizar cálculos que envolvam divisão, evitando divisão por zero.
# Future improvement: - add validations to prevent negative values or percentages outside a valid range.
#                     - validate total income before performing calculations involving division to prevent division-by-zero errors.