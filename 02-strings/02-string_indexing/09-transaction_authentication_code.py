# Gera referências e um código de autenticação para transações a partir de informações como código da transação,
# conta, cliente, data e tipo de operação, utilizando string indexing para extrair e combinar caracteres específicos.
# Generates references and an authentication code for transactions based on information such as transaction code,
# account, client, date, and operation type, using string indexing to extract and combine specific characters.

transaction_code = input("Informe o código da transação: ")
account_code = input("Informe o código da conta: ")
client_code = input("Informe o código do cliente: ")
transaction_date = input("Informe a data de transação no formato DDMMAAAA: ")
operation_type = input("Informe o tipo de operação: ")

print("=" * 60)
print("\t\tSISTEMA AUTENTICADOR DE TRANSAÇÃO")
print("=" * 60)
print("\nInformações da Transação")
print("\nCódigo da transação: " + transaction_code)
print("Código da conta: " + account_code)
print("Código do cliente: " + client_code)
print("Data: " + transaction_date)
print("Tipo de operação: " + operation_type)
print("\nInformação de Autenticação")
print("\nReferência de transação: " + transaction_code[0] + transaction_code[2] + account_code[-1] + client_code[0] + transaction_date[-2] + transaction_date[-1])
print("Identificador da conta: " + account_code[0] + account_code[1] + account_code[-1] + client_code[1] + operation_type[0] + operation_type[-1])
print("Data de referência: " + transaction_date[0] + transaction_date[1] + transaction_date[2] + transaction_date[3] + transaction_date[-2] + transaction_date[-1])
print("Código de autenticação: " + transaction_code[-1] + account_code[0] + client_code[-1] + operation_type[1] + transaction_date[0] + transaction_code[2] + account_code[-2]
+ client_code[0] + transaction_date[-1] + operation_type[-1])
print("\n")
print("=" * 60)