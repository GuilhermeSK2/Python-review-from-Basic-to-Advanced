#Dicionários permitem armazenar pares de chave-valor, onde cada chave é única e associada a um valor. 
# Eles são mutáveis e podem ser usados para armazenar dados de forma estruturada.
#São similares a arrays associativos ou maps em outras linguagens de programação.
#Não permitem itens duplicados, ou seja, cada chave deve ser única.
#chaves são imutáveis e podem ser de qualquer tipo imutável, como strings, números ou tuplas.

#Sintaxe: nome_dicionario = {chave1: valor1, chave2: valor2, ...}

elemento = {
    'Z': 3,
    'nome': 'Lítio',
    'grupo': 'Metais Alcalinos',
    'densidade': 0.534,
}

# print(f'Elemento: {elemento['nome']}') 
# print(f'Grupo: {elemento['grupo']}')
# print(f'O dicionario possui {len(elemento)} elementos.') # Exibe o tamanho do dicionário (número de pares chave-valor)

# #Atualizar uma entrada no dicionário
# elemento['grupo'] = 'Alcalinos' # Atualiza o valor da chave 'grupo'
# print(elemento)


# # Adicionar uma entrada (Adicionar uma nova chave faz ela ser adicionada ao dicionário)
# elemento['período'] = 1 # Adiciona uma nova chave 'período' com o valor 1
# print(elemento)


# #Exclusão de itens em dicionários
# del elemento['período']  # Remove a chave 'período' do dicionário
# print(elemento)


# #Apagar todos os itens do dicionário
# elemento.clear()  # Limpa todos os itens do dicionário
# print(elemento)  # Exibe o dicionário vazio
# #O dicionario continua existindo, mas está vazio

# #Excluindo o dicionário
# del elemento  # Exclui o dicionário completamente
# # print(elemento)  # Isso causaria um erro, pois o dicionário foi excluído


# print(elemento.items()) # Exibe todos os pares chave-valor do dicionário, cada item é uma tupla (chave, valor)
# for i in elemento.items():  # Itera sobre cada par chave-valor no dicionário
#     print(i) # Exibe cada par chave-valor do dicionário



# Apresentar as chaves do dicionário
# print(elemento.keys())  # Exibe todas as chaves do dicionário
# for i in elemento.keys():  # Itera sobre cada chave no dicionário
#     print(i)  # Exibe cada chave do dicionário



# #Apresentar os valores do dicionário
# print(elemento.values())  # Exibe todos os valores do dicionário
# for i in elemento.values():  # Itera sobre cada valor no dicionário
#     print(i)  # Exibe cada valor do dicionário


for i, j in elemento.items():  # Itera sobre cada par chave-valor no dicionário
    print(f'{i}: {j}') # Exibe cada chave e seu respectivo valor no formato "chave: valor"