#Quando queremos exibir algo na tela usamos a função print().
# A função print() pode receber vários parâmetros separados por vírgula e exibir todos eles
# na mesma linha, separados por espaço.

#Sintaxe:
# print(objetos, argumentos)


#-----------------------------------------------------------------------------------------------------------------------------------------------------


#Exemnplo Básico:

#mensagem = "Função print()"
#print(mensagem)  # Exibe a mensagem na tela

#print("Aula de Python")  # Exibe uma string diretamente


#-----------------------------------------------------------------------------------------------------------------------------------------------------


# Exemplo com argumentos posicionais:

#nome = 'Guilherme Freitas'
#cargo  = 'Desenvolvedor de Software'
#print(cargo, '-', nome)


#Concatenação de strings:
#nome = input("Digite seu nome: ")  # input para receber o nome do usuário
#msg = 'Olá ' + nome + '! Bem Vindo ao curso de Python!'
#print(msg)  # Concatena a string com o nome do usuário
#print('Outro texto')

#-----------------------------------------------------------------------------------------------------------------------------------------------------

#Exemplo quebra de linha:

#print('Imprime a mensagem e muda de linha') # A função print() por padrão adiciona uma quebra de linha ao final da mensagem
#print('Imprime a mensagem e não muda de linha', end='') # O parâmetro end='' faz com que a próxima impressão não mude de linha
#print(' Continua na mesma linha')


#-----------------------------------------------------------------------------------------------------------------------------------------------------

# Exemplo de formatação de string com o método format():

#nome = 'Maria'
#idade = 30
#msg_formatada = 'O nome dela é {0} e ela tem {1} anos.'.format(nome, idade)  # Formatação de string com o método format()
#print(msg_formatada)  # Exibe a mensagem


#-----------------------------------------------------------------------------------------------------------------------------------------------------

#Exemplo de formatação de string com f-strings:

#nome = 'João'
#peso = 73.50
#msg = f'Olá meu nome é {nome} e meu peso é {peso}kg.' # Formatação de string com f-strings
#print(msg)  # Exibe a mensagem formatada com f-strings

#-----------------------------------------------------------------------------------------------------------------------------------------------------

#Exemplo de formatação de string com f-strings para soma:

#a = 10
#b = 5
#res = f'A soma de {a} + {b} é igual a {a + b}'  # Formatação de string com f-strings
#print(res)  # Exibe a mensagem formatada com f-strings


#-----------------------------------------------------------------------------------------------------------------------------------------------------

#Exemplo de formatação de string com f-strings e casas decimais:

#valor = 125.579637
#print(f'O valor é {valor:.2f}')  # Exibe o valor formatado com duas casas decimais


#-----------------------------------------------------------------------------------------------------------------------------------------------------

#Exemplo de formatação de string com f-strings e caractere de escape:

#Dertermindados caracteres podem dar conflito com a formatação de strings, como o caractere de aspas simples ou duplas.
#por isso, podemos usar o caractere de escape \ para evitar esse conflito.

#valor = 125.573637
#print(f'O valor é \'{valor:.2f}\'')  #Usando o caractere de escape para evitar conflito com as aspas simples


#-----------------------------------------------------------------------------------------------------------------------------------------------------

#Exemplo de formatação de string com f-strings e tabulação:

nome = 'João'
idade = 32
print(f'Nome: {nome}\t Idade: {idade}') # Exibe o nome e a idade formatados com tabulação (\t) entre eles


