class Libro:
    def __init__(self, nombre, anio):
        self.nombre = nombre
        self.anio = anio

    def __str__(self):
        return f"{self.nombre} ({self.anio})"


def mostrar_libros(libros):
    if libros:
        print("Libros ingresados:")
        for libro in libros:
            print(libro)
    else:
        print("No se han ingresado libros.")


def eliminar_libro(libros):
    if libros:
        nombre = input("Ingrese el nombre del libro a eliminar: ")
        libros = [libro for libro in libros if libro.nombre != nombre]
        print("Libro eliminado exitosamente.")
    else:
        print("No se han ingresado libros.")


def modificar_libro(libros):
    if libros:
        nombre = input("Ingrese el nombre del libro a modificar: ")
        for libro in libros:
            if libro.nombre == nombre:
                nuevo_nombre = input("Ingrese el nuevo nombre del libro: ")
                nuevo_anio = int(input("Ingrese el nuevo año del libro: "))
                libro.nombre = nuevo_nombre
                libro.anio = nuevo_anio
                print("Libro modificado exitosamente.")
                return
        print("No se encontró un libro con ese nombre.")
    else:
        print("No se han ingresado libros.")


def ordenar_libros(libros, criterio):
    if libros:
        if criterio == "nombre":
            algoritmo = input("Ingrese el algoritmo de ordenamiento a utilizar (burbuja, shell, quick): ")
            if algoritmo == "burbuja":
                libros.sort(key=lambda libro: libro.nombre)
            elif algoritmo == "shell":
                # Implementar el algoritmo de ordenamiento ShellSort por nombre
                def shell_sort_nombre(libros):
                    n = len(libros)
                    gap = n // 2

                    while gap > 0:
                        for i in range(gap, n):
                            temp = libros[i]
                            j = i

                            while j >= gap and libros[j - gap].nombre > temp.nombre:
                                libros[j] = libros[j - gap]
                                j -= gap

                            libros[j] = temp

                        gap //= 2

                shell_sort_nombre(libros)
            elif algoritmo == "quick":
                # Implementar el algoritmo de ordenamiento Quicksort por nombre
                def partition_nombre(libros, low, high):
                    pivot = libros[high].nombre
                    i = low - 1

                    for j in range(low, high):
                        if libros[j].nombre < pivot:
                            i += 1
                            libros[i], libros[j] = libros[j], libros[i]

                    libros[i + 1], libros[high] = libros[high], libros[i + 1]
                    return i + 1

                def quick_sort_nombre(libros, low, high):
                    if low < high:
                        pivot_index = partition_nombre(libros, low, high)
                        quick_sort_nombre(libros, low, pivot_index - 1)
                        quick_sort_nombre(libros, pivot_index + 1, high)

                quick_sort_nombre(libros, 0, len(libros) - 1)
            else:
                print("Algoritmo de ordenamiento inválido.")
        elif criterio == "anio":
            algoritmo = input("Ingrese el algoritmo de ordenamiento a utilizar (burbuja, shell, quick): ")
            if algoritmo == "burbuja":
                libros.sort(key=lambda libro: libro.anio)
            elif algoritmo == "shell":
                # Implementar el algoritmo de ordenamiento ShellSort por año
                def shell_sort_anio(libros):
                    n = len(libros)
                    gap = n // 2

                    while gap > 0:
                        for i in range(gap, n):
                            temp = libros[i]
                            j = i

                            while j >= gap and libros[j - gap].anio > temp.anio:
                                libros[j] = libros[j - gap]
                                j -= gap

                            libros[j] = temp

                        gap //= 2

                shell_sort_anio(libros)
            elif algoritmo == "quick":
                # Implementar el algoritmo de ordenamiento Quicksort por año
                def partition_anio(libros, low, high):
                    pivot = libros[high].anio
                    i = low - 1

                    for j in range(low, high):
                        if libros[j].anio < pivot:
                            i += 1
                            libros[i], libros[j] = libros[j], libros[i]

                    libros[i + 1], libros[high] = libros[high], libros[i + 1]
                    return i + 1

                def quick_sort_anio(libros, low, high):
                    if low < high:
                        pivot_index = partition_anio(libros, low, high)
                        quick_sort_anio(libros, low, pivot_index - 1)
                        quick_sort_anio(libros, pivot_index + 1, high)

                quick_sort_anio(libros, 0, len(libros) - 1)
            else:
                print("Algoritmo de ordenamiento inválido.")
        else:
            print("Criterio de ordenamiento inválido.")
    else:
        print("No se han ingresado libros.")


def menu():
    libros = []

    while True:
        print("------ MENÚ ------")
        print("1. Ingresar libro")
        print("2. Mostrar libros")
        print("3. Eliminar libro")
        print("4. Modificar libro")
        print("5. Ordenar libros por nombre")
        print("6. Ordenar libros por año")
        print("0. Salir")

        opcion = input("Ingrese una opción: ")

        if opcion == "1":
            nombre = input("Ingrese el nombre del libro: ")
            anio = int(input("Ingrese el año del libro: "))
            libro = Libro(nombre, anio)
            libros.append(libro)
            print("Libro ingresado exitosamente.")
        elif opcion == "2":
            mostrar_libros(libros)
        elif opcion == "3":
            eliminar_libro(libros)
        elif opcion == "4":
            modificar_libro(libros)
        elif opcion == "5":
            ordenar_libros(libros, "nombre")
        elif opcion == "6":
            ordenar_libros(libros, "anio")
        elif opcion == "0":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Por favor, ingrese una opción válida.")


menu()
