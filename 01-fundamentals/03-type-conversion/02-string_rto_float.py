# Solicita o preço de um produto, converte para float e exibe os resultados.
# Requests the product price, converts it to a float, and displays the results.

product_price = input("Informe o preço do produto: R$ ")
quantity = input("Informe a quantidade do produto: ")
float_price_product = float(product_price)
int_quantity = int(quantity)
total_product = float_price_product * int_quantity

print(f"""
Preço do produto: R$ {product_price}
Preço convertido: R$ {float_price_product:.2f}
Quantidade do produto: {int_quantity}
Preço total: R$ {total_product:.2f}
""")

