#Manipulação de arquivos de texto, udando a função open() para abrir o arquivo, read() para ler o conteúdo e write() para escrever no arquivo.
# Quando usamos a função open() para abrir um arquivo, podemos especificar o modo de abertura, como leitura ('r'), escrita ('w') ou anexação ('a').
# Modos de acesso com open():
# 'r' - Leitura (read): Abre o arquivo para leitura. Se o
# arquivo não existir, gera um erro.
# 'w' - Escrita (write): Abre o arquivo para escrita. Se o arquivo já existir, ele será sobrescrito. Se não existir, será criado.
# 'a' - Anexação (append): Abre o arquivo para anexação.
# 'x' - Exclusivo (exclusive): Abre o arquivo para escrita, mas falha se o arquivo já existir.
# 'b' - Binário (binary): Abre o arquivo em modo binário.
# 't' - Texto (text): Abre o arquivo em modo texto (padrão).
# 'r+' - Leitura e escrita (read and write): Abre o arquivo para leitura e escrita. O ponteiro é colocado no início do arquivo.
# 'w+' - Escrita e leitura (write and read): Abre o arquivo para escrita e leitura. Se o arquivo já existir, ele será sobrescrito. Se não existir, será criado.
# 'a+' - Anexação e leitura (append and read): Abre o arquivo para anexação e leitura. O ponteiro é colocado no final do arquivo.
# 'x+' - Exclusivo e leitura (exclusive and read): Abre o arquivo para escrita e leitura, mas falha se o arquivo já existir.
# 'b+' - Binário e leitura (binary and read): Abre o arquivo em modo binário para leitura e escrita.
# 't+' - Texto e leitura (text and read): Abre o arquivo em modo texto para leitura e escrita (padrão).

#manipulador = open('arquivo.txt', 'r', encoding='utf-8')  # Abre o arquivo 'arquivo.txt' em modo leitura com codificação UTF-8
# print(f'Método read():')
# print(manipulador.read())  # Lê todo o conteúdo do arquivo e exibe na tela

#com readliune() lê o arquivo linha por linha
# print(f'Método readline():')
# print(manipulador.readline())  # Lê a primeira linha do arquivo e exibe na tela

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------


# texto = input('Qual termo deseja procurar no arquivo?')


# try:
#     manipulador = open('arquivo.txt', 'r', encoding='utf-8')  # Abre o arquivo 'arquivo.txt' em modo leitura com codificação UTF-8
#     for linha in manipulador:  # Itera sobre cada linha do arquivo
#         linha = linha.strip()  # Remove espaços em branco no início e no final da linha
#         if texto in linha:
#             print('A string foi encontrada')
#             print(linha)
#         else:
#             print('A string não foi encontrada')
#             break
# except IOError:
#     print("Não foi possível abrir o arquivo")
# else:
#     manipulador.close()  # Fecha o arquivo após a leitura

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------

#Escrever em arquivos de texto:

# try:
#     manipulador = open('arquivo.txt', 'w', encoding='utf-8')  # Abre o arquivo 'arquivo.txt'
#     manipulador.write("IA ja é o presente\n")  # Adiciona uma nova linha ao final do arquivo
#     manipulador.write("Python é muito empregado em IA\n")  # Adiciona uma nova linha
#     manipulador.write("IA veio pra ficar\n")  # Adiciona essa linha ao final do arquivo
# except IOError:
#     print("Não foi possível abrir o arquivo")
# else:
#     manipulador.close()  # Fecha o arquivo após a leitura


#-------------------------------------------------------------------------------------------------------------------------------------------------------------------


#Com writelines() podemos escrever várias linhas de uma vez
# frutas = ["Maçã\n", "Banana\n", "Laranja\n", "Uva\n", "Pera\n"]  # Lista de frutas para escrever no arquivo com quebra de linha após cada fruta

# try:
#     manipulador = open('frutas.dat', 'w', encoding='utf-8')  # Abre o arquivo 'frutas.dat' em modo escrita com codificação UTF-8
#     manipulador.writelines(frutas)  # Escreve todas as frutas na lista no arquivo, cada uma em uma nova linha
# except IOError:
#     print("Não foi possível abrir o arquivo")
# else:
#     manipulador.close()  # Fecha o arquivo após a leitura
    
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------
    
#ler o arquivo frutas.dat e exibir seu conteúdo
try:
    manipulador = open('frutas.dat', 'r', encoding='utf-8')  # Abre o arquivo 'frutas.dat' em modo escrita com codificação UTF-8
    print(manipulador.read())  # Lê todo o conteúdo do arquivo e exibe na tela
except IOError:
    print("Não foi possível abrir o arquivo")
else:
    manipulador.close()  # Fecha o arquivo após a leitura