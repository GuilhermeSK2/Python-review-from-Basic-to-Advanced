# Orientação a Objetos: Paradigma de Programação
#Paradigma é a forma/conceito de programar, ou seja, a maneira como o programador organiza o código e as estruturas de dados. A Orientação a 
# Objetos é um paradigma que organiza o código em objetos, que são instâncias de classes. 
# Cada objeto possui atributos (dados) e métodos (funções) que operam sobre esses dados.

#Classes são como moldes para criar objetos. Elas definem os atributos e métodos que os objetos terão.
#Objetos são instâncias de classes. Eles possuem seus próprios valores para os atributos definidos na classe e podem usar os métodos da classe para realizar ações.


#-------------------------------------------------------------------------------------------------------------------------------------------------------------------

#Por padrão a classe tem o nome da primeira letra maiúscula
#Atributos são as características dos objetos, ou seja, os dados que eles armazenam.
class Veiculo:
    #Self para indicar que o método pertence à instância do objeto
    def movimentar(self): # Método para movimentar o veículo
        print(f'Sou um veículo e me desloco!')
    
    #Método init é o construtor da classe, é chamado quando um objeto é criado
    def __init__(self, fabricante, modelo):
        self.__fabricante = fabricante # Atributo fabricante do veículo, está encapsulado (privado), pois começa com __ (dois underlines)
        self.__modelo = modelo  # Atributo modelo do veículo, está encapsulado (privado), pois começa com __ (dois underlines)
        self.__num_registro = None  # Atributo num_registro do veículo, inicializado como None, atributo privado, está encapsulado
    
    #Getters e Setters são métodos para acessar e modificar os atributos encapsulados
    def get_fabricante(self):  # Método getter para obter o fabricante do veículo
        print(f'O fabricante do veículo é: {self.__fabricante}')  # Exibe o fabricante do veículo
    
    def set_fabricante(self, fabricante):  # Método setter para definir o fabricante do veículo
        self.__fabricante = fabricante
        
    def get_modelo(self):  # Método getter para obter o modelo do veículo
        print(f'O modelo do veículo é: {self.__modelo}')  # Exibe o modelo do veículo
    
    def set_modelo(self, modelo):  # Método setter para definir o modelo do veículo
        self.__modelo = modelo
    
    def get_num_registro(self):  # Método getter para obter o número de registro do veículo
        return self.__num_registro
    
    def set_num_registro(self, num_registro):  # Método setter para definir o número de registro do veículo
        self.__num_registro = num_registro
    
    
#-----------------------------------------------------------------------------------------------------

#Herança é quando uma classe herda atributos e métodos de outra classe
#A classe Carro herda da classe Veiculo, ou seja, Carro é uma subclasse de Veiculo.
#Isso significa que Carro terá todos os atributos e métodos de Veiculo, além de poder adicionar seus próprios atributos e métodos.

class Carro(Veiculo):
    #metodo __init__ será herdado da classe Veiculo, mas pode ser sobrescrito para adicionar novos atributos ou modificar o comportamento
    def movimentar(self):
        print(f'Sou um carro e corro muito!')

#-----------------------------------------------------------------------------------------------------

class Motocicleta(Veiculo):
    #metodo __init__ será herdado da classe Veiculo, mas pode ser sobrescrito para adicionar novos atributos ou modificar o comportamento
    def movimentar(self):
        print(f'Sou uma motocicleta e ando pelas ruas!') #Esse conceito é chamado de polimorfismo, onde o mesmo método tem comportamentos diferentes em classes diferentes.

#-----------------------------------------------------------------------------------------------------

class Aviao(Veiculo):
    def __init__(self, fabricante, modelo, categoria): #Override o método __init__ da classe Veiculo para adicionar um novo atributo categoria
        self.__cat = categoria  # Atributo categoria do avião, está encapsulado (privado), pois começa com __ (dois underlines)
        super().__init__(fabricante, modelo)  # Chama o construtor da classe Veiculo para inicializar os atributos fabricante e modelo
        
    def movimentar(self):
        print(f'Sou um avião e voo alto!')
        
    def get_categoria(self):  # Método getter para obter a categoria do avião
        return self.__cat  # Retorna a categoria do avião
    
    def set_categoria(self, categoria):  # Método setter para definir a categoria do avião
        self.__cat = categoria  # Define a categoria do avião


#-----------------------------------------------------------------------------------------------------

if __name__ == '__main__':
    # meu_veiculo = Veiculo('GM', 'Cadillac Escalade')  # Cria um objeto carro1 da classe Veiculo
    # meu_veiculo.movimentar()  # Chama o método movimentar do objeto meu_veiculo
    
    # print(f'O modelo do meu carro é: {meu_veiculo.get_modelo()}')  # Exibe o modelo do veículo usando o método getter
    # print(f'O fabricante do meu carro é: {meu_veiculo.get_fabricante()}')  # Exibe o fabricante do veículo usando o método getter
    # meu_veiculo.set_num_registro('123456789-1')  # Define o número de registro do veículo usando o método setter
    # print(f'O número de registro do meu carro é: {meu_veiculo.get_num_registro()}')  # Exibe o número de registro do veículo usando o método getter

#------------------------------------------------------------------------------------------------------

#     meu_carro = Carro('Lexus', 'LFA')  # Cria um objeto carro2 da classe Carro
#     meu_carro.movimentar()  # Chama o método movimentar do objeto meu_carro
#     meu_carro.get_fabricante()  # Exibe o fabricante do veículo usando o método getter
#     meu_carro.get_modelo()  # Exibe o modelo do veículo usando o método getter
    
# #------------------------------------------------------------------------------------------------------
    
#     seu_carro = Carro('Audi', 'RS2') # Cria um objeto seu_carro da classe Carro
#     seu_carro.movimentar()  # Chama o método movimentar do objeto seu_carro
#     seu_carro.get_fabricante()  # Exibe o fabricante do veículo usando o método getter
#     seu_carro.get_modelo()  # Exibe o modelo do veículo usando o método getter

# #------------------------------------------------------------------------------------------------------

#     moto = Motocicleta('Honda', 'CBR 1000RR')  # Cria um objeto moto da classe Motocicleta
#     moto.movimentar()  # Chama o método movimentar do objeto moto
#     moto.get_fabricante()  # Exibe o fabricante do veículo usando o método getter
#     moto.get_modelo()  # Exibe o modelo do veículo usando o método getter
    
#------------------------------------------------------------------------------------------------------

    meu_avião = Aviao('Boeing', '747', 'Comercial')  # Cria um objeto meu_avião da classe Aviao
    meu_avião.movimentar()  # Chama o método movimentar do objeto meu_avião
    meu_avião.get_fabricante()  # Exibe o fabricante do veículo usando o método getter
    print(f'Categoria: {meu_avião.get_categoria()}')  # Exibe o modelo do veículo usando o método getter