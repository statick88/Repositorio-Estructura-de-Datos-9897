

lista = []
print(type(lista))

lista = [1,2,3,5]
print(lista)

lista = ["Diego", True, 3.14, 8, 4j, ["a", "b"], 4]
print(lista)

lista.append("Juan")
print(lista)

lista2 = lista.copy()
print(lista2)

lista2.clear()
print(lista2)

lista2 = ["a", "e", "e","i", "o", "u"]
print(lista2.count("e"))

print(len(lista2))

print(lista2[4])
print(lista2[5])

lista2.pop()
print(lista2)

lista2.remove("a")
lista2.remove("e")
lista2.remove("e")

print(lista2)

lista2.reverse()
print(lista2)

lista2.sort()
print(lista2)

lista2 = ["a", "b", "B", "c"]
lista2.sort()
print(lista2)

tupla = ("Quito", "Guayaquil", "Cuenca", "Quito")
# tupla2 = set(tupla)
# print(tupla2)

print(type(tupla))

# tupla.append("Machala")
# print(tupla)

print(tupla.count("Quito"))
print(tupla.index("Cuenca"))
# print(tupla.index("Quito"))

lista = list(tupla)
print(lista)
print(tupla)

lista.append("Machala")
tupla = tuple(lista)

print(lista)
print(tupla)

# Range

rango = range(5, 10, 2)
print(type(rango))
print(rango)

# Sets

conjunto = {"i", "o", "a", "e", "u", "u", "u", "u", "u", "u", "u"}
print(type(conjunto))
print(conjunto)

# Diccionarios

cliente001 = {
    "nombre": "Diego", 
    "apellido":"Saavedra", 
    "telefono":"0986217216", 
    "correo":"dmsaavedra@espe.edu.ec"
    }
print(type(cliente001))
print(cliente001["nombre"])
print(cliente001["correo"])

print(cliente001.get("telefono"))
cliente001["nombre"] = "Juan"
print(cliente001)
print(len(cliente001))

cliente001.popitem()
print(cliente001)

cliente001.pop("apellido")
print(cliente001)

del cliente001["telefono"]
print(cliente001)

perros = {
    "Tobby":{
    "name": "Tobby",
    "age": 6
    },
    "Leo":{
    "name": "Leo",
    "age": 1
    }
}
print(perros)

perritos = dict(name="Rocky", age=7)
print(perritos)

perros["Rokcky"] = perritos
print(perros)

# Bolean

mayorEdad = True
open = False

