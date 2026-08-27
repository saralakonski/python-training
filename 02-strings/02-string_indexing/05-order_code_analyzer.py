# Analisa um código de pedido de uma empresa de comércio eletrônico, utilizando diferentes posições da string para extrair informações e criar referências de identificação.
# Analyzes an e-commerce order code by using different string positions to extract information and create identification references.

order_code = input("Digite o cóidigo do pedido: ")

print("=" * 50)
print("\t\tORDER CODE ANALYZER")
print("=" * 50)
print("\nAnálise")
print("Número do pedido: " + order_code)
print("Três primeiros caracteres: " + order_code[0] + order_code[1] + order_code[2])
print("Quarto caractere: " + order_code[3])
print("Quinto e sexto caractere: " + order_code[4] + order_code[5])
print("Dois últimos caracteres: " + order_code[-2] + order_code[-1])
print("\nReferência do pedido: " + order_code[0] + order_code[1] + order_code[2] + order_code[-2] + order_code[-1])
print("\nIdentificação do pedido: " + order_code[0] + order_code[3] + order_code[-1])
