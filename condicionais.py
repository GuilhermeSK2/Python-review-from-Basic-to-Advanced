# Existem 3 tipos de estruturas condicionais: Simples, composta e aninhada.

#-----------------------------------------------------------------------------------------------------------------------------------------------------
# If

# Estrutura condicional simples
#A estrutura condicional simples é usada quando queremos executar um bloco de código apenas se uma condição for verdadeira. 
#Se a condição for falsa, o bloco de código não será executado.

n1 = n2 = 0.0
media = 0.0

n1 = float(input("Digite a primeira nota: "))  # input para receber a primeira nota e converter para float
n2 = float(input("Digite a segunda nota: "))  # input para receber a segunda nota e converter para float

#Calcular média aritimética das notas
media = (n1 + n2) / 2 # Calcular a média aritmética das notas dando prioridade à soma das notas e depois dividindo por 2

if (media >= 7):
    print("Resultado: Aprovado!")
    print("Parabéns!")
elif (media >= 5):
    print("Resultado: Recuperação!")
else:
    print("Aluno reprovado...")
    
print("Sua média é {}".format(media))  # Exibe a média formatada com duas casas decimais


#-----------------------------------------------------------------------------------------------------------------------------------------------------