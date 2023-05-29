# Mesmo objeto após a primeira criação do objeto
class Singleton:
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.instance = super().__new__(cls)

        return cls.__instance


A = Singleton()
B = Singleton()

print(True if A == B else False)
