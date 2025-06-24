#Crie um script que peça para o usuário digitar o nome de 5 bebidas favoritas dele, armazenando esses valores em uma lista.
#Na sequência, exiba na tela os elementos da lista em ordem alfabética, um por linha, usando laço de repetição for.

bebidas = []

while len(bebidas) < 5:
    bebida = input("Digite o nome de uma bebida favorita: ")
    bebidas.append(bebida)
    
bebidas.sort()  # Ordena a lista em ordem alfabética (Um assento pode ser considerado como um caractere especial, 
#então a ordenação pode variar dependendo do idioma e da codificação)

for bebida in bebidas:
    print(bebida)  # Exibe cada bebida em uma nova linha