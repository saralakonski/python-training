# Solicita dados de um produto e exibe os resultados.
# Requests product information and displays the results.

product_price = float(input("Informe o valor do produto: R$ "))
discount_percentage = int(input("Informe o percentual de desconto: "))

discount_amount = (discount_percentage/ 100) * product_price
final_price = product_price - discount_amount

print(f"""
Valor do produto: R${product_price:.2f}
Percentual de desconto: {discount_percentage}%
Valor do desconto: R$ {discount_amount:.2f}
Valor final: R$ {final_price:.2f}
""")