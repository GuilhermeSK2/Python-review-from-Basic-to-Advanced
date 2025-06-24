#O escopo de uma variável refere-se à região do código onde a variável é acessível. Em Python, existem dois tipos principais de escopo: local e global.

#Escopo local: Variáveis definidas dentro de uma função ou bloco de código são locais a esse bloco e não podem ser acessadas fora dele.
#Escopo global: Variáveis definidas fora de qualquer função ou bloco de código são globais e podem ser acessadas de qualquer lugar no código.

var_global = "Curso completo de Python"

def escreve_texto():
    global var_global  # Declara que vamos usar a variável global var_global
    #Sem definir a variável var_local como global, ela será considerada local à função
    var_global = "Bancos de dados com SQL" # Esta variável é local à função escreve_texto
    var_local = "Guilherme Freitas"
    print(f'Variável Global: {var_global}')  # Acessa a variável global
    print(f'Variável Local: {var_local}')  # Acessa a variável local

if __name__ == "__main__":  # Verifica se o script está sendo executado diretamente
    print(f'Executar a função escreve_texto()')
    escreve_texto()  # Chama a função para exibir as variáveis
    
    print('Tentar acessar as variáveis diretamente:')
    print(f'Variável Global: {var_global}')  # Acessa a variável global
    #print(f'Variável Local: {var_local}')  # Tenta a variável local o que causa erro