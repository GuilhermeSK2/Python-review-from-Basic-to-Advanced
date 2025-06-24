#Exceções raise são usadas para lançar uma exceção manualmente, interrompendo a execução normal do programa e transferindo o controle para 
# o bloco de tratamento de exceções mais próximo.

# Elas são úteis quando queremos sinalizar que uma condição específica ocorreu e que o programa não pode continuar normalmente.

from math import sqrt

class NumeroNegativoError(Exception):
    def __init__(self):
        pass #pass indica que não tem nada aqui e pode seguir adiante

# if __name__ == "__main__":
#     while True:
#         try:
#             num = int(input("Digite um número positivo: "))
#             if num < 0:
#                 raise ArithmeticError("Número negativo não é permitido.")  # Lança uma exceção ArithmeticError se o número for negativo
#             break  # Tenta obter um número do usuário e sai do loop se for bem-sucedido
#         except ArithmeticError:
#             print(f'Foi fornecido um número negativo!')
#     try:
#         rq = sqrt(num) # Calcula a raiz quadrada do número
#     except:  # Captura qualquer outra exceção não prevista
#         print("Ocorreu um erro ao calcular a raiz quadrada.")  # Exibe mensagem de erro se ocorrer algum problema no cálculo
#     else:
#         print(f'A raiz quadrada de {num} é: {rq}')
#     finally:
#         print("\nFim do cálculo")


if __name__ == "__main__":
    try:
        num = int(input("Digite um número positivo: "))
        if num < 0:
            raise NumeroNegativoError()  # Lança uma exceção personalizada se o número for negativo
    except NumeroNegativoError:
        print("Número negativo não é permitido.")
    else:
        print(f'A raiz quadrada de {num} é: {sqrt(num)}')  # Exibe a raiz quadrada do número se não ocorrer nenhuma exceção
    finally:
        print("\nFim do cálculo")


