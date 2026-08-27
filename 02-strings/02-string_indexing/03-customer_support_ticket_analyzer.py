# Uma pequena ferramenta interna para equipe de atendimento ao cliente
# A small intern tool to a customer support team

ticket_code = input("Informe o número do Ticket de atendimento: ")

print("=" * 50)
print("\t\tTICKET ANALYZER")
print("=" * 50)
print("\nTicket de Atentimento informado: ", ticket_code)
print("\nAnálise")
print("Primeiro caractere: " + ticket_code[0])
print("Segundo caractere: " + ticket_code[1])
print("Terceiro caractere: " + ticket_code[2])
print("\nAnálise Reversa")
print("Último caractere: " + ticket_code[-1])
print("Penúltimo caractere: " + ticket_code[-2])
print("Antepenúltimo caractere: " + ticket_code[-3])
print("\nIdentificação do setor: " + ticket_code[0] + ticket_code[1] + ticket_code[2])
# Ao utilizar vírgulas no print(), os caracteres são tratados como argumentos separados,
# e o print() adiciona espaços entre eles. Por isso, a concatenação com + é mais adequada neste caso.
# when using commas in print(), the characters are treated as separate arguments,
# and print() adds spaces between them. Therefore, concatenation with + is more appropriate in this case.
print("=" * 50)
