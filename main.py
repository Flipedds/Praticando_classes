from classes.builder_cavaleiro import BuilderCavaleiro


builder = BuilderCavaleiro()  # builder
print("Cavaleiro antes da criação dos seus atributos !")
print(builder.builder.__str__())  # to_string do objeto antes do build
builder.builder.batalha()
print('\n')

# Chamando métodos de alteração de atributos
builder.criar_espada()
builder.criar_escudo()
builder.criar_armadura()
print('\n')

# retorna o objeto criado pelo builder para uma variável
cavaleiro: object = builder.get_cavaleiro()
print("Cavaleiro depois da criação dos seus atributos !")
print(cavaleiro.__str__())
print(cavaleiro.batalha())
