class Libro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

    def __str__(self):
        return f"{self.titulo} - {self.autor}"


def mostrar_libros(libros):
    if libros:
        print("Libros ingresados:")
        for libro in libros:
            print(libro)
    else:
        print("No se han ingresado libros.")


def eliminar_libro(libros):
    if libros:
        titulo = input("Ingrese el título del libro a eliminar: ")
        libros_filtrados = [libro for libro in libros if libro.titulo != titulo]
        if len(libros_filtrados) < len(libros):
            libros[:] = libros_filtrados
            print("Libro eliminado exitosamente.")
        else:
            print("No se encontró un libro con ese título.")
    else:
        print("No se han ingresado libros.")


def modificar_libro(libros):
    if libros:
        titulo = input("Ingrese el título del libro a modificar: ")
        for libro in libros:
            if libro.titulo == titulo:
                nuevo_titulo = input("Ingrese el nuevo título del libro: ")
                nuevo_autor = input("Ingrese el nuevo autor del libro: ")
                libro.titulo = nuevo_titulo
                libro.autor = nuevo_autor
                print("Libro modificado exitosamente.")
                return
        print("No se encontró un libro con ese título.")
    else:
        print("No se han ingresado libros.")


def ordenar_libros(libros, criterio):
    if libros:
        if criterio == "titulo":
            algoritmo = input("Ingrese el algoritmo de ordenamiento a utilizar (burbuja, shell, quick): ")
            if algoritmo == "burbuja":
                libros.sort(key=lambda libro: libro.titulo)
            elif algoritmo == "shell":
                # Implementar el algoritmo de ordenamiento ShellSort por título
                def shell_sort_titulo(libros):
                    n = len(libros)
                    gap = n // 2

                    while gap > 0:
                        for i in range(gap, n):
                            temp = libros[i]
                            j = i

                            while j >= gap and libros[j - gap].titulo > temp.titulo:
                                libros[j] = libros[j - gap]
                                j -= gap

                            libros[j] = temp

                        gap //= 2

                shell_sort_titulo(libros)
            elif algoritmo == "quick":
                # Implementar el algoritmo de ordenamiento Quicksort por título
                def partition_titulo(libros, low, high):
                    pivot = libros[high].titulo
                    i = low - 1

                    for j in range(low, high):
                        if libros[j].titulo < pivot:
                            i += 1
                            libros[i], libros[j] = libros[j], libros[i]

                    libros[i + 1], libros[high] = libros[high], libros[i + 1]
                    return i + 1

                def quick_sort_titulo(libros, low, high):
                    if low < high:
                        pivot_index = partition_titulo(libros, low, high)
                        quick_sort_titulo(libros, low, pivot_index - 1)
                        quick_sort_titulo(libros, pivot_index + 1, high)

                quick_sort_titulo(libros, 0, len(libros) - 1)
            else:
                print("Algoritmo de ordenamiento inválido.")
        elif criterio == "autor":
            algoritmo = input("Ingrese el algoritmo de ordenamiento a utilizar (burbuja, shell, quick): ")
            if algoritmo == "burbuja":
                libros.sort(key=lambda libro: libro.autor)
            elif algoritmo == "shell":
                # Implementar el algoritmo de ordenamiento ShellSort por autor
                def shell_sort_autor(libros):
                    n = len(libros)
                    gap = n // 2

                    while gap > 0:
                        for i in range(gap, n):
                            temp = libros[i]
                            j = i

                            while j >= gap and libros[j - gap].autor > temp.autor:
                                libros[j] = libros[j - gap]
                                j -= gap

                            libros[j] = temp

                        gap //= 2

                shell_sort_autor(libros)
            elif algoritmo == "quick":
                # Implementar el algoritmo de ordenamiento Quicksort por autor
                def partition_autor(libros, low, high):
                    pivot = libros[high].autor
                    i = low - 1

                    for j in range(low, high):
                        if libros[j].autor < pivot:
                            i += 1
                            libros[i], libros[j] = libros[j], libros[i]

                    libros[i + 1], libros[high] = libros[high], libros[i + 1]
                    return i + 1

                def quick_sort_autor(libros, low, high):
                    if low < high:
                        pivot_index = partition_autor(libros, low, high)
                        quick_sort_autor(libros, low, pivot_index - 1)
                        quick_sort_autor(libros, pivot_index + 1, high)

                quick_sort_autor(libros, 0, len(libros) - 1)
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
        print("5. Ordenar libros por título")
        print("6. Ordenar libros por autor")
        print("0. Salir")

        opcion = input("Ingrese una opción: ")

        if opcion == "1":
            titulo = input("Ingrese el título del libro: ")
            autor = input("Ingrese el autor del libro: ")
            libro = Libro(titulo, autor)
            libros.append(libro)
            print("Libro ingresado exitosamente.")
        elif opcion == "2":
            mostrar_libros(libros)
        elif opcion == "3":
            eliminar_libro(libros)
        elif opcion == "4":
            modificar_libro(libros)
        elif opcion == "5":
            ordenar_libros(libros, "titulo")
        elif opcion == "6":
            ordenar_libros(libros, "autor")
        elif opcion == "0":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Por favor, ingrese una opción válida.")


menu()
