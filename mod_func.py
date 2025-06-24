#Módulo com funções variadas

#Mensagem de boas-vindas
def mensagem():
    print("Bem-vindo ao módulo de funções variadas!")

def fibonacci(limite):
    """
    Gera a sequência de Fibonacci até atingir ou ultrapassar um determinado número.

    Args:
        limite (int): Valor máximo que os termos da sequência podem atingir.

    Returns:
        list: Lista com os termos da sequência de Fibonacci menores ou iguais ao limite.
    """
    if limite < 0:
        return []
    sequencia = [0, 1]
    while True:
        proximo = sequencia[-1] + sequencia[-2]
        if proximo > limite:
            break
        sequencia.append(proximo)
    return sequencia

def fatorial(n):
    """
    Calcula o fatorial de um número inteiro não negativo.

    O fatorial de um número inteiro positivo n é o produto de todos os
    inteiros positivos menores ou iguais a n. O fatorial de 0 é 1.
    Ex: 5! = 5 * 4 * 3 * 2 * 1 = 120

    Args:
        n (int): O número inteiro não negativo.

    Returns:
        int: O fatorial do número.
             Retorna 1 se n for 0.
             Gera ValueError se n for negativo.
    """
    if not isinstance(n, int) or n < 0:
        raise ValueError("O fatorial é definido apenas para números inteiros não negativos.")
    if n == 0:
        return 1
    else:
        resultado = 1
        for i in range(1, n + 1):
            resultado *= i
        return resultado

def eh_primo(numero):
    """
    Verifica se um número é primo.

    Um número primo é um número natural maior que 1 que não pode ser formado
    pela multiplicação de dois números naturais menores.

    Args:
        numero (int): O número a ser verificado.

    Returns:
        bool: True se o número for primo, False caso contrário.
    """
    if numero < 2:
        return False
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True

def inverte_string(texto):
    """
    Inverte uma string.

    Args:
        texto (str): A string a ser invertida.

    Returns:
        str: A string invertida.
    """
    return texto[::-1]

def calcula_media(lista_numeros):
    """
    Calcula a média de uma lista de números.

    Args:
        lista_numeros (list): Uma lista contendo números (int ou float).

    Returns:
        float: A média dos números na lista.
               Retorna 0.0 se a lista estiver vazia.
    """
    if not lista_numeros:
        return 0.0
    return sum(lista_numeros) / len(lista_numeros)

# Exemplo de como você pode testar as funções diretamente no módulo
if __name__ == "__main__":
    print("--- Testes do Módulo ---")
    print(f"Fibonacci de 7: {fibonacci(7)}")  # Esperado: 13
    print(f"Fatorial de 5: {fatorial(5)}")    # Esperado: 120
    print(f"É 17 primo? {eh_primo(17)}")      # Esperado: True
    print(f"É 10 primo? {eh_primo(10)}")      # Esperado: False
    print(f"String invertida de 'Python': {inverte_string('Python')}") # Esperado: 'nohtyP'
    print(f"Média de [1, 2, 3, 4, 5]: {calcula_media([1, 2, 3, 4, 5])}") # Esperado: 3.0
    print(f"Média de []: {calcula_media([])}") # Esperado: 0.0