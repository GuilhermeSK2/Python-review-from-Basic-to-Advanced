#Numeros aleatorios com random

import random 

# print("Gerar 5 numeros aleatórios entre 1 e 50:")

# for i in range (5):  # Loop para gerar 5 números aleatórios
#     n = random.randint(1, 50)  # Gera um número aleatório entre 1 e 50
#     print(f'Número gerado: {n}')
    

#------------------------------------------------------------------------------------------------------------------------------------------------------------------

#Numero aleatório de ponto flutuante

# valor = random.random()  # Gera um número aleatório de ponto flutuante
# print(f'Numero gerado: {round(valor * 10, 2)}') # Multiplica por 10 e arredonda para 2 casas decimais com round


#------------------------------------------------------------------------------------------------------------------------------------------------------------------


#Gera um valor aleatório de ponto flutuante entre 1 e 100

# valor = random.uniform(1, 100)  # Gera um número aleatório de ponto flutuante entre 1 e 100
# print(f'Número: {round(valor, 4)}')  # Exibe o número com 4 casas decimais


#------------------------------------------------------------------------------------------------------------------------------------------------------------------

L = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  # Lista de números
# n = random.choice(L)  # Seleciona um número aleatório da lista
# print(f'Número aleatório escolhido da lista: {n}')  # Exibe o número escolhido aleatoriamente

# n = random.sample(L, 3)  # Seleciona 3 números aleatórios da lista (amostra)
# print(f'Números aleatórios escolhidos da lista: {n}')  # Exibe os números escolhidos aleatoriamente

# Embaralhar

print(f'Lista original: {L}')  # Exibe a lista original
random.shuffle(L)  # Embaralha a lista
print(f'Lista embaralhada: {L}')  # Exibe a lista embaralhada