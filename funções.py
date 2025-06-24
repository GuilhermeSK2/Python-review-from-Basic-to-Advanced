#Funções são blocos de código reutilizáveis que realizam uma tarefa específica. Elas podem receber parâmetros e retornar valores.
# Em Python, as funções são definidas usando a palavra-chave `def`, seguida pelo nome da função e parênteses que podem conter parâmetros.
# São importantes para a modularização do código, permitindo que você escreva código mais organizado e reutilizável, além de melhorar a legibilidade do programa.

#Fluxo: Entrada de dados -> Processamento -> Saída de dados

#Sintaxe:
# def nome_funcao(parametros):
# def de define, definir a função

# def mensagem():
#     print('Treinamento de Python')
#     print('Curso completo de Python')

# mensagem()  # Chama a função mensagem para exibir a mensagem


# #Função com argumentos:
# def soma(a, b):
#     return a + b  # Retorna a soma dos dois números, o return encerra a função e retorna o valor para quem chamou

# #Recebendo os dados para a função:
# valor1 = int(input("Digite o primeiro número: "))  # Solicita o primeiro número ao usuário
# valor2 = int(input("Digite o segundo número: "))  # Solicita o segundo número ao usuário
# s = soma(valor1, valor2)  # Chama a função soma com os valores fornecidos pelo usuário

# # Chama a função soma com os valores fornecidos pelo usuário e exibe o resultado
# print(f'A soma de {valor1} e {valor2} é: {s}')  # Exibe o resultado da soma


# def div(k, j):
#     if j != 0: 
#         return k / j  # Retorna o resultado da divisão se o divisor não for zero
#     else:
#         return "Impossível dividir por zero"  # Retorna uma mensagem de erro se o divisor for zero
    
# if __name__ == "__main__":  # Verifica se o script está sendo executado diretamente
#     a = int(input("Digite um número: "))  # Solicita um número ao usuário
#     b = int(input("Digite outro número: "))  # Solicita outro número ao usuário
#     r = div(a, b)  # Chama a função div com os números fornecidos pelo usuário
#     print(f'O resultado da divisão de {a} por {b} é: {r}')  # Exibe o resultado da divisão


# def quadrado(val):
#     quadrados = []  # Cria uma lista vazia para armazenar os quadrados
#     for x in val:
#         quadrados.append(x ** 2) # Calcula o quadrado de cada valor e adiciona à lista
#     return quadrados  # Retorna a lista de quadrados


#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# def contar(num=11, caractere='+'):
#     for i in range(1, num):
#         print(caractere)

# if __name__ == "__main__":  # Verifica se o script está sendo executado diretamente
#     contar(caractere='&')  # Chama a função contar com o caractere '&' e o número padrão 11, se não passase nada em caractere seria o padrão '+'
#     contar(num=6)  # Chama a função contar com o número 5 e o caractere padrão '+'
#     contar(num=8, caractere='@') # Chama a função contar com o número 8 e o caractere '@'
#     contar(6, '*') # Chama a função contar com o número 6 e o caractere '*' sem ter que nomear os parâmetros, pois a ordem é respeitada
    
    
# #É interessante definir o(s) primeiro(s) parâmetro(s) como obrigatórios e os demais como opcionais, 
# # para que o usuário possa escolher se deseja ou não passar os parâmetros opcionais.


#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#Exemplo de de função que realiza soma ou multiplicação dependendo do valor de um terceiro parâmetro:

x = 5
y = 6
z = 3

def soma_mult(a,b,c = 0):
    if c == 0:
        return a * b
    else:
        return a + b + c
    
if __name__ == "__main__":
    res = soma_mult(x,y)
    print(res)  # Exibe o resultado da multiplicação de x e y
    res = soma_mult(x,y,z)
    print(res)  # Exibe o resultado da soma de x, y e z