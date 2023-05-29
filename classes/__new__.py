class Meters(float):
    def __new__(cls, kilometers):
        meters = kilometers * 1000
        return super().__new__(cls, meters)


print(Meters(1))
