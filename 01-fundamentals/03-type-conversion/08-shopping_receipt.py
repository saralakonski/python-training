# Simula uma compra, calcula o desconto, o valor final e o troco do cliente.
# Simulates a purchase, calculates the discount, the final amount, and the customer's change.

# Product Data
product_name = input("Informe o produto: ")
unit_price = input("Informe o preço unitário do produto: R$ ")
product_quantity = input("Informe a quantidade do produo: ")

discount = input("Informe o percentual de desconto: ")


# Conversions 
float_unit_price = float(unit_price)
int_product_quantity = int(product_quantity)
int_discount = int(discount)

purchase_subtotal = float_unit_price * int_product_quantity
discount_value = (int_discount / 100) * purchase_subtotal
final_value = purchase_subtotal - discount_value

print("O subtotal de sua compra é de R$: " + format(purchase_subtotal, ".2f"))
print("Você recebeu um desconto de: " + str(int_discount) + "%" + "\nValor total da compra: " + format(final_value,".2f"))

amount_customer = input("Informe o valor a ser pago: R$ ")
float_amount_customer = float(amount_customer)
change = float_amount_customer - final_value

print("""======================================
            CUPOM FISCAL 
""")
print("Produto: " + product_name + "\nQuantidade: " + str(int_product_quantity) + "\nSubtotal da Compra: R$ " + format(purchase_subtotal, ".2f") +
"\nDesconto: " + str(int_discount) + "%" + "\nValor do desconto: R$ " + format(discount_value,".2f") + "\nVALOR TOTAL: R$ " + format(final_value,".2f") +
"\nValor Recebido: " + format(float_amount_customer,".2f") + "\nTroco: R$ " + format(change,".2f"))
print("""
            VOLTE SEMPRE!
======================================
""")

# Melhoria futura: adicionar uma verificação para pagamentos insuficientes.
# Future improvement: add a check for insufficient payments.