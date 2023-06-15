class Deporte:
    def __init__(self, nombre, jugadores, reglas):
        self.nombre = nombre
        self.jugadores = jugadores
        self.reglas = reglas

    def __str__(self):
        return f"Deporte: {self.nombre}\nJugadores: {self.jugadores}\nReglas: {', '.join(self.reglas)}"


def mostrar_deportes(deportes):
    if deportes:
        print("Deportes ingresados:")
        for deporte in deportes:
            print(deporte)
    else:
        print("No se han ingresado deportes.")


def eliminar_deporte(deportes):
    if deportes:
        nombre = input("Ingrese el nombre del deporte a eliminar: ")
        deportes = [deporte for deporte in deportes if deporte.nombre != nombre]
        print("Deporte eliminado exitosamente.")
    else:
        print("No se han ingresado deportes.")


def modificar_deporte(deportes):
    if deportes:
        nombre = input("Ingrese el nombre del deporte a modificar: ")
        for deporte in deportes:
            if deporte.nombre == nombre:
                nuevo_nombre = input("Ingrese el nuevo nombre del deporte: ")
                nuevos_jugadores = input("Ingrese la cantidad de jugadores: ")
                nuevas_reglas = input("Ingrese las nuevas reglas (separadas por comas): ").split(",")
                deporte.nombre = nuevo_nombre
                deporte.jugadores = nuevos_jugadores
                deporte.reglas = nuevas_reglas
                print("Deporte modificado exitosamente.")
                return
        print("No se encontró un deporte con ese nombre.")
    else:
        print("No se han ingresado deportes.")


def menu():
    deportes = []

    while True:
        print("------ MENÚ ------")
        print("1. Ingresar deporte")
        print("2. Mostrar deportes")
        print("3. Eliminar deporte")
        print("4. Modificar deporte")
        print("0. Salir")

        opcion = input("Ingrese una opción: ")

        if opcion == "1":
            nombre = input("Ingrese el nombre del deporte: ")
            jugadores = input("Ingrese la cantidad de jugadores: ")
            reglas = input("Ingrese las reglas (separadas por comas): ").split(",")
            deporte = Deporte(nombre, jugadores, reglas)
            deportes.append(deporte)
            print("Deporte ingresado exitosamente.")
        elif opcion == "2":
            mostrar_deportes(deportes)
        elif opcion == "3":
            eliminar_deporte(deportes)
        elif opcion == "4":
            modificar_deporte(deportes)
        elif opcion == "0":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Por favor, ingrese una opción válida.")


menu()
