#Exceção é um objeto que representa um erro ou uma condição excepcional que ocorre durante a execução de um programa.
#blocos try e except são usados para tratar exceções, permitindo que o programa continue a execução mesmo quando ocorre um erro.

def div(k, j):
    return round(k / j, 2)

if __name__ == "__main__":  # Verifica se o script está sendo executado diretamente
    while True:
        try:
            n1 = int(input("Digite um número inteiro: "))
            n2 = int(input("Digite outro número inteiro: "))
            break  # Tenta obter os números do usuário e sai do loop se for bem-sucedido
        except ValueError:  # Captura a exceção de valor inválido (não numérico)
            print("Ocorreu um erro ao ler o valor. Tente novamente.")  # Exibe mensagem de erro caso o usuário digite algo que não seja um número inteiro
    try:
        r = round(n1/n2, 2) # Tenta realizar a divisão e arredondar o resultado para 2 casas decimais
    except ZeroDivisionError: # Captura a exceção de divisão por zero
        print("Não é possível dividir por zero.") # Exibe mensagem de erro se ocorrer divisão por zero
    except:
        print("Ocorreu um erro desconhecido...") # Captura qualquer outra exceção não prevista
    else:
        print(f"O resultado da divisão é: {r}") # Exibe o resultado da divisão se não ocorrer nenhuma exceção
    finally:
        print("\nFim do cálculo") # Sempre executa esta parte, independentemente de ocorrer ou não uma exceção
