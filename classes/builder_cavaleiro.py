# Classe builder de Cavaleiro
class BuilderCavaleiro:
    def __init__(self):
        self.builder = Cavaleiro()  # cria objeto do tipo Cavaleiro

    # Métodos que alteram os atributos do objeto criado
    def criar_espada(self) -> None:
        self.builder.set_espada()
        print('Espada Criada!')

    def criar_escudo(self) -> None:
        self.builder.set_escudo()
        print('Escudo Criado!')

    def criar_armadura(self) -> None:
        self.builder.set_armadura()
        print('Armadura Criada!')

    # retorna o objeto criado
    def get_cavaleiro(self) -> object:
        return self.builder


class Cavaleiro:
    def __init__(self):
        self.__espada = None
        self.__escudo = None
        self.__armadura = None

    def batalha(self):
        if self.__espada is not None and self.__escudo is not None and self.__armadura is not None:
            return "Pronto para a batalha !"
        else:
            return "Ainda não está pronto para a batalha, por falta de equipamentos !"

    def set_espada(self):
        self.__espada = True

    def set_escudo(self):
        self.__escudo = True

    def set_armadura(self):
        self.__armadura = True

    def __str__(self) -> str:
        to_string = f"""
        O cavaleiro possui espada? {self.__espada},\n
            Possui escudo? {self.__escudo}, \n
                Possui armadura? {self.__armadura}
        """
        return to_string
