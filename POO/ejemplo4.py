




class Abuelo:

    def __init__(self, nombre, profesion):
        self.nombre = nombre
        self.profesion = profesion

class Padre(Abuelo):

    def __init__(self, nombre, profesion, habilidad):
        super().__init__(nombre, profesion)
        self.habilidad = habilidad

    def realizarHabilidad(self):
        return(f"Yo puedo ", self.habilidad)

class Hijo(Padre):

    def __init__(self, nombre, profesion, habilidad):
        super().__init__(nombre, profesion, habilidad)

Jose = Hijo("Jose", "Desarrollador", "cantar")
print(Jose.profesion)
print(Jose.habilidad)

