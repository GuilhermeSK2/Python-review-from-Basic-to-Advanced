a = 10
b = 5
c = 11

# Soma
soma = a + b
print(soma)

# Subtração
subtracao = a - b
print(subtracao)

# Multiplicação
multiplicacao = a * b
print(multiplicacao)

# Divisão
divisao = a / b
print(divisao)

# Divisão inteira
divisao_inteira = a // b
print(divisao_inteira)

# Módulo (resto da divisão)
modulo = a % b
print(modulo)

# Exponenciação
exponenciacao = a ** b
print(exponenciacao)


# A precedência de operadores é importante para entender como as expressões são avaliadas.
# A ordem de precedência é a seguinte:
# 1. Parênteses ()
# 2. Exponenciação (**)
# 3. Multiplicação (*) e Divisão (/) e Divisão inteira (//) e Módulo (%)
# 4. Adição (+) e Subtração (-)
# da esquerda para a direita.

# Precedência de operadores
precedencia = a + b * c
print(precedencia)

# Precedência de operadores com parênteses
precedencia_com_parenteses = (a + b) * c
print(precedencia_com_parenteses)



x = y = z = 0

#x = input("Digite um número: ") # input para receber um número passado pelo usuário
x = int(input("Digite um número: "))  # input para receber um número passado pelo usuário e converter para inteiro

#y = input("Digite outro número: ") # input para receber outro número passado pelo usuário
y = int(input("Digite outro número: "))  # input para receber outro número passado pelo usuário e converter para inteiro

z = x + y
print('A soma dos dois valores é:', z) #Concatenando com vírgula
print('A soma dos dois valores é: ' + str(z)) #Concatenando com +, convertendo para string
print('A soma dos dois valores é: {}'.format(z)) #Concatenando com format
print(f'A soma dos dois valores é: {z}') #Concatenando com f-string
print('A soma dos dois valores é: %d' % z) #Concatenando com % (antigo estilo de formatação)