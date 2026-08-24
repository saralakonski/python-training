# Solicita uma palavra ou frase curta ao usuário e utiliza índices negativos para acessar e exibir caracteres a partir do final da string.
# Requests a word or short phrase from the user and uses negative indexing to access and display characters starting from the end of the string.

word = input("Insira uma palavra ou frase curta a ser analisada: ")

print("A palavra ou frase inserida foi: " + word)
print("Primeiro caractere: " + word[0] + "\nÚltimo caractere: " + word[-1] + "\nPenúltimo caractere: " + word[-2] + "\nAntepenúltimo caractere: " + word[-3])
