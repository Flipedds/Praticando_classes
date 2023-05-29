class Cavaleiro:
    def __init__(self):
        self.__espada = False
        self.__escudo = False
        self.__armadura = False

    def criar_espada(self):
        self.__espada = True
        return 'Espada Criada'

    def criar_escudo(self):
        self.__escudo = True
        return 'Escudo Criado'

    def criar_armadura(self):
        self.__armadura = True
        return 'Armadura Criada'

    def reset(self):
        self.__armadura = False
        self.__espada = False
        self.__escudo = False
        return 'reset concluído'

    def __str__(self):
        to_string = f"""
        O cavaleiro possui espada? {self.__espada},\n
        Possui escudo? {self.__escudo}, \n
        Possui armadura? {self.__armadura}
        """
        return to_string


class Criador:
    def __init__(self):
        pass

    @staticmethod
    def create_all(builder_):
        builder_.reset()
        builder_.criar_espada()
        builder_.criar_escudo()
        builder_.criar_armadura()


builder = Cavaleiro()
print(builder.__str__())

print('\n')
Criador.create_all(builder)

print(builder.__str__())
print('\n')

builder.reset()
print(builder.__str__())
