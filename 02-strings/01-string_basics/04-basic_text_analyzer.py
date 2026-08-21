# Solicita uma frase, utiliza len() para calcular a quantidade de caracteres e converte o resultado para string para exibição.
# Requests a phrase, uses len() to calculate the number of characters, and converts the result to a string for display.


name = input("Informe seu nome: ")
user_phrase = input("Escreva uma frase para ser analisada: ")

len(user_phrase)

print("=" * 40)
print("Nome: " + name + "\nFrase a ser analisada: " + user_phrase)
print("Quantidade de caracteres da frase: " + str(len(user_phrase)))
# Inicialmente, tentei usar print("" + len(user_phrase)). Porém, len() retorna um int,
# então ele não pode ser concatenado diretamente com uma str.
# Initially, I tried to use print("" + len(user_phrase)). However, len() returns an int,
# so it cannot be directly concatenated with a str.

print("=" * 40) 