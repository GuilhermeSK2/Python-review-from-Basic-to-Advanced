#Variáveis são espaços na memória onde podemos armazenar valores de forma temporária durante a execução.

#Tipos de dados são classificações que definem o tipo de valor que uma variável pode armazenar.

#O Python por padrão não exige a declaração do tipo de dado, ele entende o tipo com base no valor passado, mas é importante entender os tipos para evitar erros.


nome_usuario1 = 'João' # Variável do tipo string (texto)

print(nome_usuario1) # Print é uma função que exibe o dado na tela
#Convenção de nomenclatura: nomes de variáveis devem ser descritivos e utilizar letras minúsculas, com palavras separadas por underscores (snake_case), 
# não pode começar com numero nem com underscore. a nomenclatura também é casesensitive.

media = 30 # Variável do tipo inteiro (número inteiro)

n1 = n2 = n3 = n4 = 10 # Atribuição múltipla de variáveis

nome, idade = 'João', 30 # Atribuição múltipla de variáveis separada por vírgula ja que são tipos de dados diferentes

ativo = True # Variável do tipo booleano (verdadeiro ou falso)

altura = 1.75 # Variável do tipo float (número decimal)


#É possível visualizar o tipo de dado usando uma função específica

#Função type() retorna o tipo de dado da variável
print(type(media)) # Exibe o tipo da variável media

print(type(nome_usuario1)) # Exibe o tipo da variável nome_usuario1

print(type(nome)) # Exibe o tipo da variável nome

print(type(idade)) # Exibe o tipo da variável idade

print(type(ativo)) # Exibe o tipo da variável ativo

print(type(altura)) # Exibe o tipo da variável altura

#Os tipos são chamados de classes em Python.
#Os tipos citados acima são os tipos primitivos, ou seja, os tipos básicos que o Python oferece.

print(type(1+2j)) # Exibe o tipo de um número complexo

# Função isinstance() verifica se uma variável é de um tipo específico (retorna True ou False)
a = 10
b = 'Sol'

print(isinstance(a, int)) # Verifica se a é do tipo inteiro

print(isinstance(a, float)) # Verifica se a é do tipo float

print(isinstance(a, (int, float))) # Verifica se a é do tipo inteiro ou float

print(isinstance(b, str)) # Verifica se b é do tipo inteiro

#Reatribuindo o valor de uma variável
a = 40 # A variável a agora armazena o valor 40, substituindo o valor anterior de 10
c = 3
r = a * c # A variável r agora armazena o resultado da multiplicação de a e c
print(r)



