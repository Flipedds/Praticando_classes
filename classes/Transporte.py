class Transporte:
    __nome: str

    def __init__(self, nome):
        self.__nome = nome

    def Criar_carro(self):
        return Carro(self.__nome)

    def Criar_moto(self):
        return Moto(self.__nome)

    def Criar_aviao(self):
        return Aviao(self.__nome)


class Carro:
    __nome: str
    __tipo: str

    def __init__(self, nome):
        self.__nome = nome
        self.__tipo = '4 portas'

    def info_carro(self):
        print(f'O carro: {self.__nome}, que tem o tipo: {self.__tipo} foi criado!')


class Moto:
    __nome: str
    __tipo: str

    def __init__(self, nome):
        self.__nome = nome
        self.__tipo = '2 rodas'

    def info_moto(self):
        print(f'A moto: {self.__nome}, que tem o tipo: {self.__tipo} foi criada!')


class Aviao:
    __nome: str
    __tipo: str

    def __init__(self, nome):
        self.__nome = nome
        self.__tipo = '2 asas'

    def info_aviao(self):
        print(f'O avião: {self.__nome}, que tem o tipo: {self.__tipo} foi criado!')


carro1 = Transporte('carro1').Criar_carro()
carro1.info_carro()
print('\n')
moto1 = Transporte('moto1').Criar_moto()
moto1.info_moto()
print('\n')
aviao1 = Transporte('aviao1').Criar_aviao()
aviao1.info_aviao()
