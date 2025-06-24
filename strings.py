#String são sequencias de caracteres que podem ser manipuladas de várias maneiras. Elas são usadas para armazenar e manipular texto em Python.
# Strings podem ser definidas usando aspas simples (' ') ou aspas duplas (" ").
# Strings são imutáveis, o que significa que uma vez criadas, não podem ser alteradas. No entanto, é possível criar novas strings a partir de operações com strings existentes.
# As strings podem conter letras, números, espaços e caracteres especiais.
# As strings são indexadas, o que significa que cada caractere tem um índice associado, começando em 0.
# Sintaxe: nome_string = 'texto' ou nome_string = "texto"


#---------------------------------------------------------------------------------------------------------------------------------------------------------------------


# nome = 'Curso de Python'  # Define uma string com o nome do curso
# instrutor = 'João Silva'  # Define uma string com o nome do instrutor
# letra = nome[0]  # Acessa o primeiro caractere da string (índice 0)
# print(letra)  # Exibe o primeiro caractere da string
# print(len(nome))  # Exibe o tamanho da string (número de caracteres)

# #Concatenação de strings:
# print(nome + ' com ' + instrutor)  # Concatena a string com outra string

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------

# frase = 'Vamos aprender Python hoje.'

# palavras = frase.split()  # Divide a string em uma lista de palavras usando o espaço como delimitador
# print(palavras)  # Exibe a lista de palavras resultante da divisão da string


# for palavra in palavras:  # Itera sobre cada palavra na lista de palavras
#     print(palavra)  # Exibe cada palavra da lista


# for letra in frase:  # Itera sobre cada caractere na string
#     print(letra)  # Exibe cada caractere da string


#Slice(fatiamento) é uma técnica para acessar uma parte da string, tupla ou lista.
# print(frase[7:19])  # Exibe os primeiros 5 caracteres da string (fatiamento)


#---------------------------------------------------------------------------------------------------------------------------------------------------------------------


#find é um método que retorna o índice da primeira ocorrência de uma substring na string, ou -1 se não for encontrada.

# email = input('Digite seu email: ')  # input para receber o email do usuário
# arroba = email.find('@')  # Encontra o índice do caractere '@' na string email

# print(arroba)  # Exibe o índice do caractere '@' na string email

# usuario = email[0:arroba] # Extrai a parte do email antes do '@'

# dominio = email[arroba+1:] # Extrai a parte do email após o '@'

# print(f'Usuário: {usuario}')  # Exibe o usuário do email
# print(f'Domínio: {dominio}')  # Exibe o domínio do email


#---------------------------------------------------------------------------------------------------------------------------------------------------------------------

# produtos = 'Carbonato de sódio e óxido de zinco'
# print('sódio' in produtos)  # Verifica se 'sódio' está presente na string produtos
# print('magnésio' not in produtos)  # Verifica se 'magnésio' não está presente na string produtos


# item = 'hipoclorido'
# pos = item.find('clor') # Encontra o índice da substring 'clor' na string item
# print(pos)
# pos = item.find('flu') # Encontra o índice da substring 'flu' na string item
# print(pos) # Se a substring não for encontrada, retorna -1


#---------------------------------------------------------------------------------------------------------------------------------------------------------------------


# objeto_celeste = 'galáxia esPiral M31'
# print(objeto_celeste)  # Exibe a string original
# print(objeto_celeste.title())  # Converte a string para o formato de título com letra maiúscula no início de cada palavra
# print(objeto_celeste.capitalize())  # Converte a primeira letra da string para maiúscula e o restante para minúsculas
# print(objeto_celeste.upper())  # Converte a string para maiúsculas
# print(objeto_celeste.lower())  # Converte a string para minúsculas


# suplemento = 'cloreto de magnésio'
# n_suplemento = suplemento.replace('magnésio', 'zinco')  # Substitui 'magnésio' por 'potássio' na string suplemento
# print(suplemento) # Exibe a string original
# print(n_suplemento) # Exibe a string com a substituição


#---------------------------------------------------------------------------------------------------------------------------------------------------------------------


#Removendo espaços em branco:

# frase = '    Ômega 3 é bom para a saúde!    '
# print(frase)  # Exibe a string original
# print(frase.lstrip()) # Remove os espaços em branco à esquerda da string
# print(frase.rstrip())  # Remove os espaços em branco à direita da string
# print(frase.strip())  # Remove os espaços em branco no início e no final da string


#---------------------------------------------------------------------------------------------------------------------------------------------------------------------


# fruta = 'Abacate'
# print(fruta) # Exibe a string original
# print(fruta.rjust(20)) # Alinha a string à direita com um total de 20 caracteres, preenchendo com espaços à esquerda
# print(fruta.center(20)) # Centraliza a string com um total de 20 caracteres, preenchendo com espaços à esquerda e à direita
# print(fruta.ljust(20)) # Alinha a string à esquerda com um total de 20 caracteres, preenchendo com espaços à direita

# print(fruta.center(20, '-')) # Centraliza a string com um total de 20 caracteres, preenchendo com hífens à esquerda e à direita


#---------------------------------------------------------------------------------------------------------------------------------------------------------------------

# p = 'Treinamento de Python'
# print(p.startswith('t'))  # Verifica se a string começa com 't' (retorna False, pois é sensível a maiúsculas e minúsculas)
# print(p.startswith('T'))  # Verifica se a string começa com 'T' (retorna True, pois é sensível a maiúsculas e minúsculas)

# print(p.endswith('on'))  # Verifica se a string termina com 'on' (retorna True)
# print(p.endswith('o'))  # Verifica se a string termina com 'o' (retorna True)


#---------------------------------------------------------------------------------------------------------------------------------------------------------------------

#Docstrings

# Docstrings são strings de documentação que descrevem o propósito e o uso de funções, classes ou módulos em Python.
# Elas são definidas usando aspas triplas (''' ou """) e podem ser acessadas através do atributo __doc__ do objeto.

#pode ser atribuida a uma variável para ser exibida, mas geralmente é usada para documentar funções, classes ou módulos.
texto = """
Docstring é uma espécie de documentação que podemos inserir dentro de um módulo, função, método ou classe no Python, entre outros locais.
    Respeita deslocamento do texto e é multilinha.
"""

print(texto)  # Exibe a docstring