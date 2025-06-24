# O python possui funções built-in que podem ser usadas para realizar operações matemáticas básicas, como soma, subtração, multiplicação e divisão. 
# Além disso, existem módulos como `math` e `numpy` que oferecem funções matemáticas avançadas.

import math  # Importa o módulo math para usar funções matemáticas avançadas


#------------------------------------------------------------------------------------------------------------------------------------------------------------------


# #funções built-in

# valores = [2,5,8,-1,0,11,7,-6]
# print(max(valores))  # Retorna o maior valor da lista
# print(min(valores))  # Retorna o menor valor da lista

# a = -5
# b = 4

# # Valor absoluto
# print(abs(a))  # Retorna o valor absoluto de -5, que é 5


# #Exponenciação
# print(pow(a, b))  # Retorna -5 elevado a 4, que é 625 (a base, b o expoente)


# c = 2.789011 # Valor com muitas casas decimais

# print(round(c, 2))  # Arredonda o número 2.789011 para duas casas decimais, resultando em 2.79


#------------------------------------------------------------------------------------------------------------------------------------------------------------------


#funções do módulo math

x = 8
y = 100

# raiz_quadrada = math.sqrt(x)  # Calcula a raiz quadrada de 8

# print(math.ceil(raiz_quadrada))  # Arredonda para cima, resultando em 3

# print(math.floor(raiz_quadrada))  # Arredonda para baixo, resultando em 2

# print(round(raiz_quadrada, 2))  # Arredonda para duas casas decimais, resultando em 2.83



# # logaritmo
# logaritmo = math.log10(y) # Calcula o logaritmo de 100 na base 10

# print(logaritmo)  # Exibe o logaritmo de 100 na base 10, que é 2.0



#pi

# print(math.pi)  # Exibe o valor de pi, que é aproximadamente 3.141592653589793
# print(round(math.pi, 2))  # Arredonda o valor de pi para duas casas decimais, resultando em 3.14


print(math.factorial(x)) # Calcula o fatorial de 8, resultando em 40320

print(x / math.inf) # Divide 8 por infinito, resultando em 0.0