# Calcula o valor de compra de um determinado produto.
# Calculates the total price of a specific product.

product_name = input("Informe o produto: ")
unit_price = input("Informe o preço unitário do produto: R$ ")
quantity = input("Informe a quantidade do produto: ")
float_price = float(unit_price)

decimal_float_price = format(float_price, ".2f")
# Tive dúvidas ao deixar o preço com duas casas decimais. Inicialmente utilizei = float_price:.2f, o que não funciona fora de uma f-string
# I had some doubts about displaying the price with two decimal places. Initially, I used = float_price:.2f, which does not work outside an f-string.

int_quantity = int(quantity)
total_buy = float_price * int_quantity

print("Resumo da compra:")
print("Produto selecionado: " + product_name + "\nPreço unitário: R$ " + decimal_float_price + "\nQuantidade: " + str(int_quantity) + "\nTotal da compra: R$ " + str(total_buy))

