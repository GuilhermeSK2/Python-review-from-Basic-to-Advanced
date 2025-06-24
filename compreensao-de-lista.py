#Compreensão de lista é uma maneira concisa e eficiente de criar listas em Python. 
# Ela permite gerar uma nova lista aplicando uma expressão a cada item de uma sequência existente, como uma lista ou um iterável.

numeros = [1, 4, 7, 9, 10, 12, 21]

#Com map, list e lambda

# quadrados = list(map(lambda num: num ** 2, numeros))
# print(quadrados)  # Exibe os quadrados dos números da lista


#Com compreensão de lista
# quadrados = [num ** 2 for num in numeros] # Cria uma nova lista com os quadrados dos números
# print(quadrados)  # Exibe os quadrados dos números da lista

# #Criar uma lista de numeros pares
# pares = [n for n in range(1200) if n % 2 == 0]  # Cria uma lista com números pares de 0 a 10
# print(pares) # Exibe a lista de números pares 


# frase = 'A lógica é apenas o princípio da sabeoria, e não o seu fim.'
# vogais = ['a', 'e', 'i', 'o', 'u', 'á', 'é', 'í', 'ó', 'ú']  # Lista de vogais

# lista_vogais = [v for v in frase if v in vogais]  # Cria uma lista com as vogais presentes na frase
# print(f'A frase possui {len(lista_vogais)} vogais: {lista_vogais}')  # Exibe a quantidade de vogais e a lista de vogais encontradas


#Distributiva entre valores de duas listas
distributiva = [k * m for k in [2,3,5] for m in [10,20,30]]
print(distributiva)  # Exibe o resultado da distributiva entre os valores das duas listas


#Se começar a ficar complexa é melhor não usar compreensão de lista
# Exemplo complexo que pode ser difícil de ler