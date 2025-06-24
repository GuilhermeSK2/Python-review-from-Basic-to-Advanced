#Pacotes são baixados ou estão prontos no python
#Modulos são arquivos que podem ser criados pelo usuário ou já existentes no python

#Imports devem estar no início do arquivo antes de qualquer outro código
#import math  # Importa o módulo math para usar funções matemáticas avançadas

#print(math.sqrt(16))  # Exibe a raiz quadrada de 16 usando a função sqrt do módulo math

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#from math import sqrt  # Importa apenas a função sqrt do módulo math

#print(sqrt(16)) # Exibe a raiz quadrada de 16 usando a função sqrt importada diretamente

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------


#Não muito recomendado por que pode causar conflitos de nomes

#from math import * # Importa todas as funções do módulo math
#print(sqrt(16))  # Exibe a raiz quadrada de 16 usando a função sqrt importada diretamente


#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Importa o módulo math com um alias (apelido) m

#import math as m

#print(m.sqrt(16))  # Exibe a raiz quadrada de 16 usando a função sqrt do módulo math com o alias m


#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#Importa um módulo personalizado criado pelo usuário chamado mod_func
# import mod_func as mf

# if __name__ == "__main__":
#     mf.mensagem()  # Chama a função mensagem do módulo mod_func
    
#     num = int(input("Digite um número inteiro: "))
    
#     print(f'\nCalcular o fatorial de {num}:')
#     fat = mf.fatorial(num)  # Chama a função fatorial do módulo mod_func
#     print(f'O fatorial de {num} é: {fat}')

#     print(f'\nCalcular sequência de fibonacci de {num}:')
#     fib = mf.fibonacci(num)  # Chama a função fatorial do módulo mod_func
#     print(f'A sequência de fibonacci de {num} é: {fib}')

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

import numpy as np  # Importa o módulo numpy com o alias np

L = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])  # Cria um array numpy com os números de 1 a 9

print(L)  # Exibe o array numpy