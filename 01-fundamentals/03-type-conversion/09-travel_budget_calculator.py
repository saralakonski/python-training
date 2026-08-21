# Simula um orçamento de viagem, calcula os custos por categoria, o custo total e o custo médio por pessoa e por dia.
# Simulates a travel budget, calculates costs by category, the total cost, and the average cost per person and per day.

# Travel Data
destination = input("Informe o destino desejado: ")
days_count = input("Informe a quantidade estimada de dias da viagem: ")
people_count = input("Informe a quantidade de pessoas: ")
accommodation = input("Informe o valor da diária da hospedagem por pessoa: R$ ")
food = input("Informe o custo médio estimado diário de alimentação por pessoa: R$ ")
flight = input("Informe o custo médio de passagens aéreas por pessoa, considerando ida e volta: R$")
transport = input("Informe o custo médio diário estimado de transporte por pessoa: R$")
quantity_tour = input("Informe a quantidade de passeios a serem realizados:")
price_tour = input("Informe o custo médio estimado por passeio por pessoa: R$ ")

# Após compreender o processo de conversão de tipos, reutilizarei o mesmo nome de variável após a conversão,
# evitando criar variáveis diferentes apenas para indicar o tipo do dado.
# After understanding the type conversion process, I will reuse the same variable name after conversion,
# avoiding different variables solely to indicate the data type.

# Data conversion
days_count = int(days_count)
people_count = int(people_count)
accommodation = float(accommodation)
food = float(food)
flight = float(flight)
transport = float(transport)
quantity_tour = int(quantity_tour)
price_tour = float(price_tour)

# Calculate
total_accommodation = accommodation * people_count * days_count
total_food = food * people_count * days_count
total_flight = flight * people_count
total_transport = transport * people_count * days_count
total_tour = quantity_tour * people_count * price_tour
total_travel = total_accommodation + total_food + total_flight + total_transport + total_tour
average_cost_person = total_travel / people_count
average_cost_person_by_day = average_cost_person / days_count

print("""
===========================================
        CUSTOS DA VIAGEM
""")
print("Destino da Viagem: " + destination)
print("Quantidade de pessoas: " + str(people_count) + "\nDuração da viagem: " + str(days_count) + "\nCustos com hospedagem: R$ " + format(total_accommodation,".2f") + 
"\nCustos com alimentação: R$ " + format(total_food,".2f") + "\nCustos com passagem aérea: R$ " + format(total_flight,".2f") + "\nCustos com transporte: R$ " + 
format(total_transport,".2f") + "\nCustos com passeios: R$ " + format(total_tour,".2f") + "\nCusto total da viagem: R$ " + format(total_travel,".2f")
+ "\nCusto total por pessoa: R$ " + format(average_cost_person,".2f") + "\nCusto médio diário por pessoa: R$ " + format(average_cost_person_by_day,".2f"))
print("""
===========================================
""")

# Melhoria futura: validar valores iguais a zero em campos utilizados como divisores, evitando erros de divisão.
# Future improvement: validate zero values in fields used as divisors to prevent division errors.