# Solicita uma palavra e uma posição ao usuário, utilizando string indexing para acessar e exibir caracteres específicos, incluindo o primeiro, o último e o caractere correspondente à posição informada.
# Requests a word and a position from the user, using string indexing to access and display specific characters, including the first, last, and character corresponding to the given position.

word = input("Digite uma palavra a ser analisada: ")
position = input("Informe qual posição da palavra deseja verificar: ")
position = int(position)

print("A palavra informada é: " + word)
print("A letra correspondente à primeira posição é: " + word[0])
print("A letra correspondente à última posição é: " + word[-1])
print("Você informou a posição " + str(position) + " da palavra " + word)
print("A posição " + str(position) + " é a letra " + word[position])

# Inicialmente, utilizei o índice como string, pois o valor recebido por input() é uma string.
# Foi necessário convertê-lo para int antes de utilizá-lo no indexing.
# Initially, I used the index as a string because values received by input() are strings.
# I needed to convert it to int before using it for indexing.