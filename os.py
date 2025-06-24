#O módulo OS é um módulo integrado do Python que fornece uma maneira de interagir com o sistema operacional. 
# Ele permite acessar funcionalidades dependentes do sistema operacional, como manipulação de arquivos, diretórios e variáveis de ambiente.

#Exemplo de uso do módulo OS para renomear arquivos em um diretório específico

import os

os.chdir('e:\\Teste') # Muda o diretório de trabalho para 'e:\\Teste'
print(f'Diretório atual: {os.getcwd()}')  # Exibe o diretório atual

padrao_nome = input('Qual o padrão do nome dos arquivos a usar (Sem a extensão)? ') # Solicita ao usuário o padrão de nome para os arquivos, sem a extensão

for contador, arq in enumerate(os.listdir()): # Itera sobre os arquivos no diretório atual, enumerando-os para obter um contador
    if os.path.isfile(arq): # Verifica se o item é um arquivo
        nome_arq, exten_arq = os.path.splitext(arq) # Separa o nome do arquivo e a extensão
        nome_arq = padrao_nome + ' ' + str(contador) # Cria o novo nome do arquivo com o padrão fornecido pelo usuário e o contador
        
        nome_novo = f'{nome_arq}{exten_arq}'  # Cria o novo nome do arquivo com a extensão original
        
        os.rename(arq, nome_novo)  # Renomeia o arquivo

print('Arquivos renomeados')