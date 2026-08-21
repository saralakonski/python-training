# Solicita informações profissionais básicas e exibe um cartão de identificação organizado.
# Requests basic professional information and displays an organized identification card.

full_name = input("Informe seu nome completo: ")
job_title = input("Informe seu job_title: ")
company = input("Informe sua empresa: ")
email = input("Informe seu e-mail: ")

print("""
==========================================
            IDENTIFICAÇÃO
==========================================
""")
print("Nome: " + full_name + "\njob_title: " + job_title + "\nEmpresa: " + company + "\nE-mail: " + email)
