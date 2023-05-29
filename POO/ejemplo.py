
class Monster:

    def __init__(self, nombre, categoria):
        self.nombre = nombre
        self.categoria = categoria

    def myFunc(self):
        print("Hey, soy un ", self.categoria)

mounstrito = Monster("Sullivan", "Asustador")
print(mounstrito.nombre)
print(mounstrito.myFunc())