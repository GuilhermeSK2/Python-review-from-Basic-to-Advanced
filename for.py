# O laço for é usado para iterar sobre uma sequência (como uma lista, tupla ou string) ou um objeto iterável. É útil quando sabemos quantas vezes precisamos repetir o código.




# Exemplo de uso do laço for com uma lista
#lista = [2,6,9,4,0,12,3,7]

#for item in lista:
#    print(item)  # Exibe cada item da lista


#-----------------------------------------------------------------------------------------------------------------------------------------------------


# Exemplo de uso do laço for com uma string

#palavra = 'Python'

#for letra in palavra:
#    print(letra)  # Exibe cada letra da palavra 'Python'


#-----------------------------------------------------------------------------------------------------------------------------------------------------


# Exemplo de uso do laço for com a função range(faixa de valores)
#for numero in range(1, 11): # Itera de 1 a 10 (o último valor não é incluído ele é o limite onde o loop para)
#    print(numero)  # Exibe cada número de 1 a 10


#-----------------------------------------------------------------------------------------------------------------------------------------------------


#for numero in range(10): # Itera de 0 a 9 (o último valor não é incluído ele é o limite onde o loop para)
#    print(numero)  # Exibe cada número de 0 a 9 (o último valor não é incluído ele é o limite onde o loop para)


#nome = input("Digite seu nome: ")  # input para receber o nome do usuário
#for x in range(10):
#    print(f'{x+1} {nome}')


#------------------------------------------------------------------------------------------------------------------------------------------------------


#range(valor_inicial, valor_final, incremento):

#for x in range(2, 20, 2):  # Itera de 2 a 20 com incremento de 2
#    print(x)  # Exibe cada número par de 2 a 18


#------------------------------------------------------------------------------------------------------------------------------------------------------


pedras = ('Rubi', 'Esmeralda', 'Quartzo', 'Safira', 'Diamante', 'Turmalina') #Tupla de pedras preciosas

for pedra in pedras:  # Itera sobre cada pedra na tupla
    if pedra == 'Quartzo':  # Verifica se a pedra é Quartzo
        continue # Se for Quartzo, pula para a próxima iteração do loop
    print(pedra)  # Exibe o nome de cada pedra

