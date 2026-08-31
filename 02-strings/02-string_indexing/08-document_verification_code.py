# Gera referências e um código de verificação para documentos a partir de informações como código do documento, 
# cliente, ano de emissão e categoria, utilizando string indexing para extrair e combinar caracteres específicos.
# Generates references and a verification code for documents based on information such as document code, 
# client code, issue year, and category, using string indexing to extract and combine specific characters.

document_code = input("Informe o código do documento: ")
client_code = input("Informe o código do cliente: ")
issue_year = input("Informe o ano de emissão do documento: ")
category = input("Informe o código da categoria do documento: ")

print("=" * 50)
print("\t\tSISTEMA DE VERIFICAÇÃO DE DOCUMENTO")
print("=" * 50)
print("\nInformações do documento")
print("\nCódigo do documento: " + document_code)
print("Código do cliente: " + client_code)
print("Ano de emissão: " + issue_year)
print("Categoria: " + category)
print("\nVerificação de Informações")
print("\nReferência do Documento: " + document_code[0] + document_code[2] + client_code[-2] + client_code[-1] + issue_year[-1])
print("Identificador da Categoria: " + category[0] + category[-1] + client_code[0] + client_code[1] + issue_year[-2]) 
print("Código de Verificação: " + document_code[-1] + client_code[0] + category[1] + issue_year[0] + document_code[2] + category[-1] + client_code[-2] + issue_year[-1])
print("\n")
print("=" * 50)
