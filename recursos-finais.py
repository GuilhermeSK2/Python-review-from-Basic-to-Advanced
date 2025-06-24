#Trocar valores entre duas variáveis

var1 = 12
var2 = 31

# #Em outras linguagens, poderíamos fazer algo como:
# #aux = var1
# #var1 = var2
# #var2 = aux

# #em python podemos fazer assim:
# var1, var2 = var2, var1

# print(f'var1: {var1}, var2: {var2}')  # Exibe os valores de var1 e var2 após a troca


#-------------------------------------------------------------------------------------------------------------------------------------------------------------------

# #Operador Condicional ternário

# menor = var1 if var1 < var2 else var2
# print(f'O menor valor é: {menor}')  # Exibe o menor valor entre var1 e var2 usando o operador condicional ternário


# #Usando tupla

# print(f'Menor valor: {(var2, var1)[var1 < var2]}')  # Exibe o menor valor entre var1 e var2 usando uma tupla

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------

#Generators

#Generator é parecido com compreensão de listas, mas não cria uma lista completa na memória. Em vez disso, ele gera os valores sob demanda, economizando memória.

# valores = [1,3,5,7,9,11,13,15]
# quadrados = (item**2 for item in valores)  # Cria um gerador que calcula o quadrado de cada item na lista valores
# print(quadrados)
# for valor in quadrados:
#     print(valor)  # Exibe cada quadrado gerado pelo generator

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------

#Função enumerate

#É uma função embutida que permite iterar sobre uma sequência (como uma lista ou tupla) e obter o índice de cada elemento junto com o próprio elemento.
# bebidas = ['água', 'suco', 'refrigerante', 'cerveja']
# for i, item in enumerate(bebidas):  # Itera sobre a lista bebidas, obtendo o índice e o item
#     print(f'Índice: {i}, Bebida: {item}')  # Exibe o índice e o item da lista bebidas


temperaturas = [-1, 10, 5, -3, 8, 4, -2, -5, 7]
total = 0

for i, t in enumerate(temperaturas):
    if t < 0:
        print(f'A temperatura em {i} é negativa, com {t}°C.')  # Exibe o total de temperaturas negativas na lista temperaturas

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------

#Gerenciamento de contexto com with
#O gerenciamento de contexto é uma maneira de garantir que recursos sejam adquiridos e liberados corretamente, 
# mesmo em caso de erros. O bloco with é usado para criar um contexto onde os recursos são gerenciados automaticamente.


try:
    a = open('frutas.dat', 'r', encoding='utf-8')  # Abre o arquivo frutas.dat em modo de leitura
    print(a.read())  # Lê e exibe o conteúdo do arquivo frutas.dat
except IOError:
    print("Não foi possível abrir o arquivo frutas.dat")  # Exibe uma mensagem de erro se o arquivo não puder ser aberto
else:
    a.close()  # Fecha o arquivo após a leitura

#Usando o gerenciador de contexto with para abrir e ler o arquivo frutas.dat

with open('frutas.dat', 'r', encoding='utf-8') as a:
    for linha in a:
        print(linha, end='')  # Lê e exibe cada linha do arquivo frutas.dat, sem adicionar uma nova linha extra