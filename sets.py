#Sets são conjuntos de elementos únicos, ou seja, não permitem duplicatas. Eles são úteis quando precisamos garantir que não haja valores repetidos em uma coleção.
# Sets são mutáveis, mas não ordenados, e não suportam indexação ou fatiamento como listas ou tuplas.
# Eles são definidos usando chaves `{}` ou a função `set()`.
# Sets são úteis para operações matemáticas como união, interseção e diferença.

# Sintaxe: nome_set = {valor1, valor2, ...} ou nome_set = set([valor1, valor2, ...])

planetas_anoes = {
    'Plutão',
    'Ceres',
    'Eris',
    'Haumea',
    'Makemake',
}

# print(planetas_anoes)  # Exibe o conjunto de planetas anões

# print(len(planetas_anoes))  # Exibe o tamanho do conjunto (número de elementos)

# print('Ceres' in planetas_anoes)  # Verifica se 'Ceres' está presente no conjunto (retorna True ou False)
# print('Terra' in planetas_anoes)  # Verifica se 'Terra' está presente no conjunto (retorna True ou False)
# print('Terra' not in planetas_anoes)  # Verifica se 'Terra' não está presente no conjunto (retorna True ou False)

# for astro in planetas_anoes:  # Itera sobre cada elemento no conjunto de planetas anões
#     print(astro.upper())  # Exibe cada planeta anão do conjunto


#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# astros = ['Lua', 'Venus', 'Sirius', 'Marte', 'Lua'] # Lista de astros, incluindo duplicatas
# print(astros, end=' ') # Exibe a lista de astros

# astros_set = set(astros)  # Converte a lista de astros em um conjunto, removendo duplicatas
# print(astros_set)  # Exibe o conjunto de astros sem duplicatas

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

astros1 = {'Lua', 'Venus', 'Sirius', 'Marte', 'Io'}
astros2 = {'Lua', 'Venus', 'Sirius', 'Marte', 'Cometa de Halley'}
# print(astros1 == astros2)  # Verifica se os dois conjuntos são iguais (retorna True ou False)
# print(astros1 != astros2)  # Verifica se os dois conjuntos são diferentes (retorna True ou False)

# print(astros1 | astros2)  # União dos dois conjuntos (todos os elementos únicos de ambos os conjuntos)
# print(astros1.union(astros2))  # União dos dois conjuntos usando o método `union()`

# #Intersecção
# # A interseção de dois conjuntos é o conjunto de elementos que estão presentes em ambos os
# print(astros1 & astros2)  # Interseção dos dois conjuntos (elementos comuns a ambos os conjuntos)
# print(astros1.intersection(astros2))  # Interseção dos dois conjuntos usando

# print(astros1 ^ astros2)  # Diferença simétrica (elementos que estão em um dos conjuntos, mas não em ambos)
# print(astros1.symmetric_difference(astros2))  # Diferença simétrica usando o método `symmetric_difference()`

astros1.add('Urano') # Adiciona 'Urano' ao conjunto astros1
astros2.add('Sol') # Adiciona 'Sol' ao conjunto astros2
print(astros1)
print(astros2)

#--------------------------------------------------------

astros1.remove('Io')  # Remove 'Io' do conjunto astros1, se estiver presente
astros1.discard('Io')  # Tenta remover 'Io' do conjunto astros1, mas não causará erro se não estiver presente
print(astros1)

#--------------------------------------------------------

#astros1.remove('Terra') # Tenta remover 'Terra' do conjunto astros1, se não estiver presente, causará um erro
astros1.discard('Terra')  # Tenta remover 'Terra' do conjunto astros1, mas não causará erro se não estiver presente
print(astros1)

#--------------------------------------------------------

astros1.pop()  # Remove e retorna um elemento aleatório do conjunto astros1
print(astros1)

#--------------------------------------------------------

astros1.clear()  # Limpa todos os elementos do conjunto astros1, deixando-o vazio
print(astros1)
