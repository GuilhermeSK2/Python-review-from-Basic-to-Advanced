#Operadores lógicos ou operadores booleanos são usados para combinar expressões booleanas. Eles retornam um valor booleano (True ou False).

# Os operadores lógicos mais comuns são:
# 1. and (E lógico)
# 2. or (OU lógico)
# 3. not (NÃO lógico)


#-----------------------------------------------------------------------------------------------------------------------------------------------------


#Exemplo de uso do operador lógico and:

# Condição A     -    Condição B    -   Resultado
# False          -    False          -   False
# True           -    False          -   False
# False          -    True           -   False
# True           -    True           -   True


#-----------------------------------------------------------------------------------------------------------------------------------------------------


#Exemplo de uso do operador lógico or:

# Condição A     -    Condição B    -   Resultado
# False          -    False          -   False
# True           -    False          -   True
# False          -    True           -   True
# True           -    True           -   True


#-----------------------------------------------------------------------------------------------------------------------------------------------------


#Exemplo de uso do operador lógico not:

# Condição A     -    Resultado
# False          -    True
# True           -    False


#-----------------------------------------------------------------------------------------------------------------------------------------------------


#Exemplo de uso do operador lógico and:

#idade = 25
#altura = 1.75

#resultado = (idade >= 18) and (altura >= 1.70) # Verifica se a pessoa é maior de idade e tem altura maior ou igual a 1.70m
#msg = 'Pode participar do evento? ' + str(resultado)

#print(msg) # Exibe a mensagem com o resultado da verificação



#-----------------------------------------------------------------------------------------------------------------------------------------------------

# Programa de disparo de alarme (Exemplo de uso do operador lógico or):

#porta = 'a'
#janela = 'f'

#alarme = (porta == 'a') or (janela == 'a')  # Verifica se a porta e a janela estão abertas

#msg = ('O alarme está disparado? ' + str(alarme))  # Exibe a mensagem com o resultado da verificação
#print(msg)  # Exibe a mensagem com o resultado da verificação


#-----------------------------------------------------------------------------------------------------------------------------------------------------


# Programa de verificação de saldo (Exemplo de uso do operador lógico not):

tem_dinheiro = False # Inicializa a variável tem_dinheiro como False, indicando que o usuário não tem dinheiro
#Supondo que o usuário receba uma quantia
tem_dinheiro = not tem_dinheiro  # Inverte o valor de tem_dinheiro

msg = 'Tem dinheiro? ' + str(tem_dinheiro)  # Exibe a mensagem com o resultado da verificação
print(msg) # Exibe a mensagem com o resultado da verificação
