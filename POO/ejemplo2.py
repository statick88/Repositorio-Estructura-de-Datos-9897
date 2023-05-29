

class Perro:
    
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} de {self.age} años de edad"
    
    def ladrar(self):
        print(f"{self.name} ladra fuerte")
    
perro_1 = Perro("Wolf", 7)
# perro_1 = Perro()

print(perro_1.age)
print(perro_1)
help(perro_1)
perro_1.ladrar()
