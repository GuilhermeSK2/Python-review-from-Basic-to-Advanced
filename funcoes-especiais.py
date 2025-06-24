#Funçoes lambdas (anônimas) são funções que recebem outras funções como argumentos ou retornam funções como resultado. Elas são úteis para criar código mais flexível e reutilizável.
#São conhecidas como funcões anônimas, pois não possuem um nome definido. Elas são definidas usando a palavra-chave `lambda`, 
#seguida por uma lista de parâmetros e uma expressão que representa o corpo da função.

#Sintaxe:
# lambda parametros: expressao



#Exemplo 1:

# quadrado = lambda x: x**2 # Define uma função lambda que calcula o quadrado de um número

# for i in range(1, 11):
#     print(f'O quadrado de {i} é: {quadrado(i)}')  # Chama a função lambda para calcular o quadrado de cada número de 1 a 10



#Exemplo 2:

# par = lambda x: x % 2 == 0  # Define uma função lambda que verifica se um número é par
# print(par(2))  # Exibe True, pois 2 é par
# print(par(3))  # Exibe False, pois 3 não é par


#Exemplo 3:

# f_c = lambda f: (f - 32) * 5/9  # Define uma função lambda que converte Fahrenheit para Celsius
# print(f_c(32))


#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#Função map é usada para aplicar uma função a todos os itens de um iterável (como uma lista) e retornar um novo iterável com os resultados.
# Sintaxe:
# map(funcao, iteravel)

# Exemplo 1:

# num = [1,2,3,4,5,6,7,8]  # Lista de números de 1 a 8
# dobro = list(map(lambda x: x * 2, num)) # Aplica a função lambda que multiplica cada número por 2
# print(num) # Exibe a lista original
# print(dobro)  # Exibe o objeto map, que é um iterável

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# palavras = ['Python', 'é', 'uma', 'linguagem', 'de', 'programação']  # Lista de palavras
# maiusculas = list(map(str.upper, palavras)) # Aplica a função str.upper a cada palavra da lista
# print(palavras)  # Exibe a lista original
# print(maiusculas)  # Exibe a lista com todas as palavras em maiúsculas


#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#Função filter é usada para filtrar elementos de um iterável com base em uma função que retorna True ou False.
# Sintaxe:
# filter(funcao, iteravel)

# # Exemplo 1:

# def numeros_pares(n):
#     return n % 2 == 0  # Retorna True se o número for par, False caso contrário

# numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]  # Lista de números de 1 a 13
# num_par = list(filter(numeros_pares, numeros))  # Filtra os números pares da lista
# print(numeros)  # Exibe a lista original
# print(num_par)  # Exibe a lista com os números pares filtrados

#Exemplo 2 com lambda:

# numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]  # Lista de números de 1 a 13
# num_impar = list(filter(lambda x: x % 2 != 0, numeros))  # Filtra os números ímpares da lista
# print(numeros)  # Exibe a lista original
# print(num_impar)  # Exibe a lista com os números ímpares filtrados


#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#Função reduce é usada para aplicar uma função cumulativa a todos os itens de um iterável, reduzindo-o a um único valor.
# É necessário importar a função reduce do módulo functools.
# Sintaxe:
# from functools import reduce
# reduce(funcao, sequencia, valor_inicial)
from functools import reduce

# def mult(x, y):
#     return x * y  # Retorna o produto de x e y

# #Exemplo operação cumulativa de multiplicação
# numeros = [1, 2, 3, 4, 5, 6]  # Lista de números de 1 a 6
# total = reduce(mult, numeros) # Aplica a função mult cumulativamente aos números da lista
# print(numeros)  # Exibe a lista original
# print(total) # Exibe o resultado da multiplicação cumulativa



#Exemplo soma cumulativa dos quadrados de valores, usando expressão lambda:

numeros = [1, 2, 3, 4]  # Lista de números de 1 a 4
# ((1² + 2²)² + 3²)² + 4²

total = reduce(lambda x, y: x**2 + y**2, numeros)  # Aplica a função lambda cumulativamente aos números da lista
print(numeros)  # Exibe a lista original
print(total)  # Exibe o resultado da soma cumulativa dos quadrados




