# Programa que lê três notas de um aluno, calcula e mostra a sua média, alterando o tipo de dado para float.
# Programm that reads three grades of a student, calculates and shows the average, changing the data type to float.

note1 = int(input("Digite a primeira nota: "))
note2 = int(input("Digite a segunda nota: "))
note3 = int(input("Digite a terceira nota: "))

media = (note1 + note2 + note3) / 3

print(f"""
Nota 1: {float(note1)}
Nota 2: {float(note2)}
Nota 3: {float(note3)}
Sua média final é: {float(media)}
""")