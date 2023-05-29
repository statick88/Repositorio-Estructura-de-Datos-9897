


class Deportes:

    def __init__(self, nombre):
        self.nombre = nombre

    def __str__(self):
        return(f"yo soy el deporte {self.nombre}")
    
class Baloncesto(Deportes):

    def __init__(self, nombre):
        super().__init__(nombre)

deporte1 = Baloncesto("Baloncesto")
print(deporte1)