#Recursividade é uma técnica de programação onde uma função chama a si mesma para resolver um problema.
# É útil para resolver problemas que podem ser divididos em subproblemas menores, 
# como calcular o fatorial de um número, percorrer estruturas de dados como árvores ou listas encadeadas, ou resolver problemas matemáticos complexos.

#Formula geral para fatorial:
# fatorial(num) = 1, se num = 0 ou se num = 1  'Caso-Base'
# fatorial(num) = num * fatorial(num - 1), isso para num > 1  'Caso Recursivo'
# 4! (Quatro fatorial) -> 4 * fatorial(3) =  4 * 3 * fatorial(2) = 4 * 3 * 2 * fatorial(1) -> 
# 4! = 4 * 3 * 2 * 1 = 24



def fatorial(numero):
    if numero == 0 or numero == 1:
        return 1
    else:
        return numero * fatorial(numero - 1)

if __name__ == '__main__':
    x = int(input("Digite um número inteiro para calcular seu fatorial: "))
    try:
        res = fatorial(x)
    except RecursionError:
        print("O número fornecido é muito grande ou negativo")
    else:
        print(f'O fatorial de {x} é {res}')