# Escreva uma função chamada generate_password() que seleciona três palavras aleatórias de um arquivo fornecido de palavras
#  e os concatena em uma única sequência de caracteres em uma lista (o retorno da função deverá ser uma lista). 
# O código para ler os dados do arquivo já está no código de inicialização, você precisará criar uma senha fora dessas partes.

# Use an import statement at the top
import csv
import random

word_file = "words.txt"
word_list = []

#fill up the word_list
with open(word_file,'r') as words:
	for line in words:
		# remove white space and make everything lowercase
		word = line.strip().lower()
		# don't include words that are too long or too short
		if 3 < len(word) < 8:
			word_list.append(word)

# Add your function generate_password here
# It should return a string consisting of three random words 
# concatenated together without spaces
def generate_password():
    return str().join(random.sample(word_list,3))

#  alternativamente, você pode usar a função random.sample e o método .join para sequências de caracteres:
def generate_password():
    return random.choice(word_list) + random.choice(word_list) + random.choice(word_list)


