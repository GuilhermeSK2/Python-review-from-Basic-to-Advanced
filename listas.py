# #Sequencias são coleções de elementos ordenados, como listas, tuplas e strings. Elas permitem acessar os elementos por meio de índices, que começam em 0.
# #São parecidas com arrays em outras linguagens de programação, mas possuem algumas diferenças importantes, como a mutabilidade e a possibilidade de conter 
# # elementos de diferentes tipos.

# #Listas em Python são coleções ordenadas e mutáveis de elementos. Elas podem conter elementos de diferentes tipos, como números, strings e até outras listas. 
# # As listas são definidas usando colchetes `[]` e os elementos são separados por vírgulas.

# #Sintaxe: nome_lsita = [valores]
# # Cada item da lista pode ser acessado por meio de um índice, que começa em 0.

# n1 = [4,6,7,8,0,3]
# n2 = [1,6,3,0,12,4]

# valores = n1 + n2  # Concatena as duas listas

# #-----------------------------------------------------------------------------------------------------------------------------------------------------

# #print(valores)  # Exibe a lista resultante da concatenação

# #print(type(valores))  # Exibe o tipo da variável valores, que é uma lista

# #print(valores[0])  # Acessa o primeiro elemento da lista (índice 0)

# #print(valores[-1])  # Acessa o último elemento da lista (índice -1)

# #-----------------------------------------------------------------------------------------------------------------------------------------------------

# #valores[0] = 9  # Modifica o primeiro elemento da lista para 9

# #print(valores)  # Exibe a lista após a modificação do primeiro elemento

# #print(valores[0]) # Exibe o primeiro elemento da lista após a modificação

# #-----------------------------------------------------------------------------------------------------------------------------------------------------

# #Slice (fatiamento) é uma técnica para acessar uma parte da lista, tupla ou string.

# #print(valores[3:4]) # Exibe os elementos da lista do índice 0 ao 3 (o último índice não é incluído)


# #-----------------------------------------------------------------------------------------------------------------------------------------------------


# #Funções para manipular a lista

# # print(len(valores))  # Exibe o tamanho da lista (número de elementos)


# # print(sorted(valores))  # Exibe a lista ordenada (não modifica a lista original)


# # print(sorted(valores, reverse=True))  # Exibe a lista ordenada em ordem decrescente (não modifica a lista original)


# # print(sum(valores))  # Exibe a soma dos elementos da lista


# # print(min(valores))  # Exibe o menor elemento da lista


# # print(max(valores))  # Exibe o maior elemento da lista


# #-----------------------------------------------------------------------------------------------------------------------------------------------------

# #Métodos para modificar a lista

# valores.append(13)  # Adiciona o elemento 10 ao final da lista
# print(valores)  # Exibe a lista após adicionar o elemento 13

# valores.pop(3)  # Remove o último elemento da lista
# print(valores)  # Exibe a lista após remover o último elemento

# valores.insert(3, 21) # Insere o elemento 21 na posição 3 da lista e empurra os outros elementos para a direita
# print(valores)  # Exibe a lista após inserir o elemento 21 na posição 3

# print(17 in valores)  # Verifica se o elemento 12 está presente na lista e exibe True ou False

#-----------------------------------------------------------------------------------------------------------------------------------------------------

planetas = ['Mercúrio', 'Vênus', 'Terra', 'Marte', 'Júpiter', 'Saturno', 'Urano', 'Netuno']

for planeta in planetas:
    print(planeta)  # Exibe o nome de cada planeta na lista