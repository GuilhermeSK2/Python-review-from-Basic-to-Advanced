#O laço while é usado para repetir um bloco de código enquanto uma condição for verdadeira. É útil quando não sabemos quantas vezes precisamos repetir o código.


#-----------------------------------------------------------------------------------------------------------------------------------------------------


# Exemplo de uso do laço while:

#num = 1

#while (num <= 10):
#    print(num)
#    num += 1  # Incrementa num em 1 a cada iteração do loop
#print('Laço encerrado!')  # Mensagem exibida após o término do loop


#-----------------------------------------------------------------------------------------------------------------------------------------------------

# Laço while com if e break

nome = None

while True: # Inicia um loop infinito
    print("Digite seu nome, ou x para parar:")
    nome = input()
    if nome == 'x' or nome == 'X': # Verifica se o usuário digitou 'x' ou 'X' para sair do loop
        break # Se a condição for verdadeira, sai do loop
    print(f"Bem Vindo, {nome}") # Exibe uma mensagem de boas-vindas com o nome digitado
print("Até logo!")