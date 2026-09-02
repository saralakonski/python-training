# Simula um sistema corporativo de processamento de pedidos, coletando dados de clientes, produtos e vendas,
# realizando cálculos financeiros e gerando referências, códigos de rastreamento e segurança por meio de string indexing e fundamentos de Python.
# Simulates a corporate order processing system by collecting customer, product, and sales data, 
# performing financial calculations, and generating references, tracking codes, and security codes using string indexing and Python fundamentals.

client_name = input("Informe o nome do cliente: ")
client_code = input("Informe o código do cliente: ")
product_code = input("Informe o código do produto: ")
seller_code = input("Informe o código do vendedor: ")
order_year = input("Informe o ano do pedido no formato AAAA: ")
order_number = input("Informe o número do pedido: ")
unit_price = input("Informe o preço unitário do produto: R$ ")
quantity = input("Informe a quantidade do produto: ")
discount = input("Informe o percentual de desconto: ")

#Valor bruto
#Gross amount
gross_amount = float(unit_price) * int(quantity)

#Valor do desconto
#Discount amount
discount_amount = gross_amount * (float(discount) / 100)

#Valor final
#Final amount
final_amount = gross_amount - discount_amount

print("=" * 60)
print("\t\tSISTEMA DE PROCESSAMENTO DE PEDIDOS")
print("=" * 60)
print("\nDADOS DO CLIENTE")
print("\nNome: " + client_name)
print("Código do cliente: " + client_code)
print("\nDADOS DO PEDIDO")
print("\nNúmero do pedido: " + order_number)
print("Produto: " + product_code)
print("Vendedor: " + seller_code)
print("Ano do pedido: " + order_year)
print("Quantidade: " + quantity)
print("\nVALORES")
print("\nPreço unitário: R$ " + unit_price)
print("Valor bruto: R$ " + format(gross_amount,".2f"))
print("Desconto: " + discount + " %")
print("Valor do desconto: R$ " + format(discount_amount,".2f"))
print("Valor final: R$ " + format(final_amount,".2f"))
print("\nDADOS DE REFERÊNCIA")
print("\nReferência do cliente: " + client_name[0] + client_name[-1] + client_code[0] + client_code[1] + client_code[-2] + client_code[-1])
print("Referência do produto: " + product_code[0] + product_code[1] + product_code[2] + product_code[-2] + product_code[-1])
print("Referência do vendedor: " + seller_code[0] + seller_code[-1] + client_name[0] + client_code[-1] + order_year[-1])
print("Referência do pedido: " + order_number[0] + order_number[1] + order_number[2] + order_number[-1] + order_year[-2] + order_year[-1])
print("\nINFORMAÇÕES DE SEGURANÇA")
print("\nCódigo de rastreamento: " + client_code[0] + product_code[-1] + seller_code[0] + order_number[1] + client_code[-1] + product_code[2] + seller_code[-2] + order_number[-1] 
+ order_year[-2] + order_year[-1])
print("Código de segurança: " + order_number[-1] + client_name[0] + product_code[1] + seller_code[-1] + order_year[0] + client_code[-1] + 
order_number[2] + product_code[0] + seller_code[-2] + client_code[-2] + order_year[-2] + order_year[-1])
print("\n")
print("=" * 60)