# Solicita informações de um produto e mostra o valor total da compra.
# Requests product information and displays the total purchase amount.


product_name = input("Informe o produto: ")
price = float(input("Informe o preço do produto: R$ "))
quantity= int(input("Informe a quantidade do produto: "))

total_purchase = price * quantity

print(f"""
Produto: {product_name}
Preço unitário: R$ {price:.2f}
Quantidade: {quantity}
O valor total de sua compra é: R$ {total_purchase:.2f}
""")