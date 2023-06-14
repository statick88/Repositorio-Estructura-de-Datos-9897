class Receta:
    def __init__(self, nombre, ingredientes, pasos):
        self.nombre = nombre
        self.ingredientes = ingredientes
        self.pasos = pasos

    def __str__(self):
        return f"Receta: {self.nombre}\nIngredientes: {', '.join(self.ingredientes)}\nPasos: {', '.join(self.pasos)}"


def mostrar_recetas(recetas):
    if recetas:
        print("Recetas ingresadas:")
        for receta in recetas:
            print(receta)
    else:
        print("No se han ingresado recetas.")


def eliminar_receta(recetas):
    if recetas:
        nombre = input("Ingrese el nombre de la receta a eliminar: ")
        recetas = [receta for receta in recetas if receta.nombre != nombre]
        print("Receta eliminada exitosamente.")
    else:
        print("No se han ingresado recetas.")


def modificar_receta(recetas):
    if recetas:
        nombre = input("Ingrese el nombre de la receta a modificar: ")
        for receta in recetas:
            if receta.nombre == nombre:
                nuevo_nombre = input("Ingrese el nuevo nombre de la receta: ")
                nuevos_ingredientes = input("Ingrese los nuevos ingredientes (separados por comas): ").split(",")
                nuevos_pasos = input("Ingrese los nuevos pasos (separados por comas): ").split(",")
                receta.nombre = nuevo_nombre
                receta.ingredientes = nuevos_ingredientes
                receta.pasos = nuevos_pasos
                print("Receta modificada exitosamente.")
                return
        print("No se encontró una receta con ese nombre.")
    else:
        print("No se han ingresado recetas.")


def menu():
    recetas = []

    while True:
        print("------ MENÚ ------")
        print("1. Ingresar receta")
        print("2. Mostrar recetas")
        print("3. Eliminar receta")
        print("4. Modificar receta")
        print("0. Salir")

        opcion = input("Ingrese una opción: ")

        if opcion == "1":
            nombre = input("Ingrese el nombre de la receta: ")
            ingredientes = input("Ingrese los ingredientes (separados por comas): ").split(",")
            pasos = input("Ingrese los pasos (separados por comas): ").split(",")
            receta = Receta(nombre, ingredientes, pasos)
            recetas.append(receta)
            print("Receta ingresada exitosamente.")
        elif opcion == "2":
            mostrar_recetas(recetas)
        elif opcion == "3":
            eliminar_receta(recetas)
        elif opcion == "4":
            modificar_receta(recetas)
        elif opcion == "0":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Por favor, ingrese una opción válida.")


menu()
