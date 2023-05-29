# Herança
class Dados:
    __nome: str
    __idade: str

    def __init__(self, nome, idade):
        self.__nome = nome
        self.__idade = idade

    def mostrar_dados(self):
        print(f'Nome: {self.__nome}, Idade: {self.__idade}')

    def __str__(self):
        return f'{self.__nome}, {self.__idade}'


class User(Dados):
    def __init__(self, nome, idade):
        Dados.__init__(self, nome, idade)


User('Filipe', 19).mostrar_dados()

