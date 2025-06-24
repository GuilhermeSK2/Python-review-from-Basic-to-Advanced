#Os operadores de comparação são usados para fazer comparações entre valores. Eles retornam um valor booleano (True ou False).

x = 10
y = 5


# == Igual a
print(x == y)  # False, porque 10 não é igual a 5

# Comparando com o mesmo valor mas com operação no meio
print(x == (x + 5))  # False, porque 10 não é igual a 15


# != Diferente de
print(x != y)  # True, porque 10 é diferente de 5

# > Maior que
print(x > y)   # True, porque 10 é maior que 5

# < Menor que
print(x < y)   # False, porque 10 não é menor que 5

# >= Maior ou igual a
print(x >= y)  # True, porque 10 é maior ou igual a 5

# <= Menor ou igual a
print(x <= y)  # False, porque 10 não é menor ou igual a 5


x = y = z = False
n1 = n2 = 0

print("Digite um número:")
n1 = int(input())  # input para receber um número passado pelo usuário e converter para inteiro
n2 = int(input("Digite outro número: "))  # input com mensagem para receber outro número passado pelo usuário e converter para inteiro

x = n1 == n2  # Verifica se os números são iguais
print("Os números são iguais:", x, '\n' ) # "\n" equivale a pular uma linha

z = n1 > n2
print("O número", n1, "é maior que", n2, "?", z, '\n') # Verifica se o primeiro número é maior que o segundo

y = n1 != n2
print('São diferentes? ' + str(y)) #Com sinal de "+" a concatenação deve ser feita com strings, então é necessário converter o booleano para string2