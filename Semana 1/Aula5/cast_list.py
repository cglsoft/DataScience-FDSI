# Quiz: Lista do elenco de Flying Circus
# Você criará uma lista dos atores que apareceram no programa de televisão Monty Python's Flying Circus.

# Escreva uma função chamada create_cast_list, que recebe um nome de arquivo como entrada e retorna uma 
# lista de nomes de atores.
# Ela será executada no arquivo flying_circus_cast.txt (essas informações foram coletadas de imdb.com). 
# Cada linha desse arquivo consiste no nome de um ator, uma vírgula e, depois, algumas informações
#  (desordenadas) sobre os papéis que eles desempenharam no programa. Você precisará extrair somente 
# o nome e adicioná-lo a uma lista. Você pode usar o método .split() para processar cada linha.


def create_cast_list(filename):
    cast_list = []
    # usar with para abrir o arquivo filename
    with open(filename) as f:
    # use a sintaxe do laço for para processar cada linha
    # e adicione o nome do ator a cast_list
        for line in f:
            line_data = line.split(',')
            cast_list.append(line_data[0])
    return cast_list