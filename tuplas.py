#Tuplas são estruturas de dados que permitem armazenar múltiplos valores em uma única variável.
# Elas são semelhantes às listas, mas possuem algumas diferenças importantes:
# 1. As tuplas são imutáveis, ou seja, uma vez criadas, não podem ser modificadas.
# 2. As tuplas são definidas usando parênteses `()`, enquanto as listas usam colchetes `[]`.
# 3. As tuplas podem conter elementos de diferentes tipos, assim como as listas.

#Para interações as tuplas podem ser mais rápidas que as listas, pois não precisam de alocação de memória dinâmica.

# Sintaxe: nome_tupla = (valores)

# tupla = (1,2,3,4,5)  # Tupla de números inteiros
# print(tupla)  # Exibe a tupla

halogenios = ('F', 'Cl', 'Br', 'I', 'At')  # Tupla de halogênios
gases_nobres = ('He', 'Ne', 'Ar', 'Xe', 'Kr', 'Rn')  # Tupla de gases nobres
elementos = halogenios + gases_nobres  # Concatena as tuplas de halogênios e gases nobres
print(elementos)  # Exibe a tupla resultante da concatenação
t1 = (5,3,6,8,4,5,6,4,3,0,12,22,3,4,5)

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------


# print(halogenios)  # Exibe a tupla de halogênios

# print(len(halogenios))  # Exibe o tamanho da tupla (número de elementos)

# print(halogenios[0])  # Acessa o primeiro elemento da tupla (índice 0)

# print(halogenios[-1])  # Acessa o último elemento da tupla (índice -1)

# print(halogenios[1:3])  # Exibe os elementos da tupla do índice 1 ao 2 (o último índice não é incluído)

# print('Cl' in halogenios)  # Verifica se 'Cl' está presente na tupla de halogênios (retorna True ou False)

# print('Fe' in halogenios)  # Verifica se 'Fe' está presente na tupla de halogênios (retorna True ou False)

# #-------------------------------------------------------------------------------------------------------------------------------------------------------------------------


# print(t1.count(5)) # Conta quantas vezes o número 5 aparece na tupla t1

# print(sum(t1))  # Exibe a soma dos elementos da tupla

# print(min(t1))  # Exibe o menor elemento da tupla

# print(max(t1))  # Exibe o maior elemento da tupla

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------


#Operações não disponíveis para tuplas: .sort(), .append(), .remove(), .insert(), .pop(), .reverse() todos os métodos que alteram a tupla não são permitidos, 
# pois as tuplas são imutáveis.

# for elemento in elementos:  # Itera sobre cada elemento na tupla de elementos
#     print(f'Elemento químico: {elemento}')  # Exibe cada elemento da tupla


#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#Convertento uma tupla em uma lista:

# grupo17 = list(halogenios)  # Converte a tupla de halogênios em uma lista
# grupo17[0] = 'H' # Modifica o primeiro elemento da lista de halogênios
# print(grupo17)  # Exibe a lista de halogênios
# print(type(grupo17))  # Exibe o tipo da variável grupo17, que é uma lista


#Convertendo uma lista em uma tupla:

grupo1 = ['Li', 'Na', 'K', 'Rb', 'Cs', 'Fr']  # Lista de metais alcalinos
alcalinos = tuple(grupo1)  # Converte a lista de metais alcalinos em uma tupla
print(alcalinos)  # Exibe a tupla de metais alcalinos
print(type(alcalinos))  # Exibe o tipo da variável alcalinos, que é uma tupla


print(sorted(alcalinos))  # Exibe a tupla de metais alcalinos ordenada (não modifica a tupla original)