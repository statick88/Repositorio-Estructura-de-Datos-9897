class Juego:
    def __init__(self, nombre, plataforma):
        self.nombre = nombre
        self.plataforma = plataforma
    
    def __str__(self):
        return f"{self.nombre} - Plataforma: {self.plataforma}"


def mostrar_juegos(juegos):
    if juegos:
        print("Juegos ingresados:")
        for juego in juegos:
            print(juego)
    else:
        print("No se han ingresado juegos.")


def eliminar_juego(juegos):
    if juegos:
        nombre = input("Ingrese el nombre del juego a eliminar: ")
        juegos = [juego for juego in juegos if juego.nombre != nombre]
        print("Juego eliminado exitosamente.")
    else:
        print("No se han ingresado juegos.")

def modificar_juego(juegos):
    if juegos:
        nombre = input("Ingrese el nombre del juego a modificar: ")
        for juego in juegos:
            if juego.nombre == nombre:
                nuevo_nombre = input("Ingrese el nuevo nombre del juego: ")
                nueva_plataforma = input("Ingrese la nueva plataforma del juego: ")
                juego.nombre = nuevo_nombre
                juego.plataforma = nueva_plataforma
                print("Juego modificado exitosamente.")
                return
        print("No se encontró un juego con ese nombre.")
    else:
        print("No se han ingresado juegos.")

def ordenar_juegos(juegos, criterio):
    if juegos:
        if criterio == "nombre":
            algoritmo = input("Ingrese el algoritmo de ordenamiento a utilizar (burbuja, shell, quick): ")
            if algoritmo == "burbuja":
                juegos.sort(key=lambda juego: juego.nombre)
            elif algoritmo == "shell":
                # Implementar el algoritmo de ordenamiento ShellSort por nombre
                def shell_sort_nombre(juegos):
                    n = len(juegos)
                    gap = n // 2

                    while gap > 0:
                        for i in range(gap, n):
                            temp = juegos[i]
                            j = i

                            while j >= gap and juegos[j - gap].nombre > temp.nombre:
                                juegos[j] = juegos[j - gap]
                                j -= gap

                            juegos[j] = temp

                        gap //= 2

            elif algoritmo == "quick":
                # Implementar el algoritmo de ordenamiento Quicksort por nombre
                def partition_nombre(juegos, low, high):
                    pivot = juegos[high].nombre
                    i = low - 1

                    for j in range(low, high):
                        if juegos[j].nombre < pivot:
                            i += 1
                            juegos[i], juegos[j] = juegos[j], juegos[i]

                    juegos[i + 1], juegos[high] = juegos[high], juegos[i + 1]
                    return i + 1


                def quick_sort_nombre(juegos, low, high):
                    if low < high:
                        pivot_index = partition_nombre(juegos, low, high)
                        quick_sort_nombre(juegos, low, pivot_index - 1)
                        quick_sort_nombre(juegos, pivot_index + 1, high)


                def quicksort_por_nombre(juegos):
                    quick_sort_nombre(juegos, 0, len(juegos) - 1)
            else:
                print("Algoritmo de ordenamiento inválido.")
        elif criterio == "plataforma":
            algoritmo = input("Ingrese el algoritmo de ordenamiento a utilizar (burbuja, shell, quick): ")
            if algoritmo == "burbuja":
                juegos.sort(key=lambda juego: juego.plataforma)
            elif algoritmo == "shell":
                # Implementar el algoritmo de ordenamiento ShellSort por plataforma
                def shell_sort_plataforma(juegos):
                    n = len(juegos)
                    gap = n // 2

                    while gap > 0:
                        for i in range(gap, n):
                            temp = juegos[i]
                            j = i

                            while j >= gap and juegos[j - gap].plataforma > temp.plataforma:
                                juegos[j] = juegos[j - gap]
                                j -= gap

                            juegos[j] = temp

                        gap //= 2

            elif algoritmo == "quick":
                # Implementar el algoritmo de ordenamiento Quicksort por plataforma
                def partition_plataforma(juegos, low, high):
                    pivot = juegos[high].plataforma
                    i = low - 1

                    for j in range(low, high):
                        if juegos[j].plataforma < pivot:
                            i += 1
                            juegos[i], juegos[j] = juegos[j], juegos[i]

                    juegos[i + 1], juegos[high] = juegos[high], juegos[i + 1]
                    return i + 1


                def quick_sort_plataforma(juegos, low, high):
                    if low < high:
                        pivot_index = partition_plataforma(juegos, low, high)
                        quick_sort_plataforma(juegos, low, pivot_index - 1)
                        quick_sort_plataforma(juegos, pivot_index + 1, high)


                def quicksort_por_plataforma(juegos):
                    quick_sort_plataforma(juegos, 0, len(juegos) - 1)
            else:
                print("Algoritmo de ordenamiento inválido.")
        else:
            print("Criterio de ordenamiento inválido.")
    else:
        print("No se han ingresado juegos.")


def menu():
    juegos = []

    while True:
        print("------ MENÚ ------")
        print("1. Ingresar juego")
        print("2. Mostrar juegos")
        print("3. Eliminar juego")
        print("4. Modificar juego")
        print("5. Ordenar juegos por nombre")
        print("6. Ordenar juegos por plataforma")
        print("0. Salir")

        opcion = input("Ingrese una opción: ")

        if opcion == "1":
            nombre = input("Ingrese el nombre del juego: ")
            plataforma = input("Ingrese la plataforma del juego: ")
            juego = Juego(nombre, plataforma)
            juegos.append(juego)
            print("Juego ingresado exitosamente.")
        elif opcion == "2":
            mostrar_juegos(juegos)
        elif opcion == "3":
            eliminar_juego(juegos)
        elif opcion == "4":
            modificar_juego(juegos)
        elif opcion == "5":
            ordenar_juegos(juegos, "nombre")
        elif opcion == "6":
            ordenar_juegos(juegos, "plataforma")
        elif opcion == "0":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Por favor, ingrese una opción válida.")

menu()
