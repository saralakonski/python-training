# Simula a geração de um recibo de compra, utilizando operações com strings, concatenação, formatação de valores e análise da quantidade de caracteres.
# Simulates the generation of a purchase receipt using string operations, concatenation, value formatting, and character count analysis.

store_name = input("Informe o nome do estabelecimento: ")
customer_name = input("Informe o nome do cliente: ")
product_name = input("Informe o nome do produto: ")
quantity = input("Informe a quantidade do produto: ")
product_price = input("Informe o preço do produto: ")
observation = input("Informações adicionais da compra: ")

product_price = float(product_price)
total_purchase = (product_price) * int(quantity)

print("=" * 50)
print("\t\t" + store_name)
print("_" * 50)
print("\t\tRECIBO")
print("\n")
print("Informações da Compra:")
print("\n")
print("Cliente: " + customer_name + "\nProduto: " + product_name + "\nQuantidade: " + quantity + "\t| Valor unitário: " + "R$ " + format(product_price,".2f") + "\nValor total: R$ " + format(total_purchase,".2f") + "\nInformações Adicionais: " + observation)
print("_" * 50)
print("Análise do texto:\n\nCaracteres do cliente: " + str(len(customer_name)) + " caracteres\nCaracteres do Produto: " + str(len(product_name)) + " caracteres\nCaracteres de Informações Adicionais: "
+ str(len(observation)) + " caracteres\nTotal de caracteres: " + str(len(customer_name + product_name + observation)) + " caracteres")
print("_" * 50)
print("\t\tOBRIGADO PELA COMPRA\n\t\tVOLTE SEMPRE!")
print("=" * 50)