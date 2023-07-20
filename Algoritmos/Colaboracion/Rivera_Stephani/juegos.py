class Juego:
    def _init_(self, nombre, anio):
        self.nombre = nombre
        self.anio = anio
    
    def _str_(self):
        return f"{self.nombre} ({self.anio})"


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
                nuevo_anio = int(input("Ingrese el nuevo año del juego: "))
                juego.nombre = nuevo_nombre
                juego.anio = nuevo_anio
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

                shell_sort_nombre(juegos)
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

                quick_sort_nombre(juegos, 0, len(juegos) - 1)
            else:
                print("Algoritmo de ordenamiento inválido.")
        elif criterio == "anio":
            algoritmo = input("Ingrese el algoritmo de ordenamiento a utilizar (burbuja, shell, quick): ")
            if algoritmo == "burbuja":
                juegos.sort(key=lambda juego: juego.anio)
            elif algoritmo == "shell":
                # Implementar el algoritmo de ordenamiento ShellSort por año
                def shell_sort_anio(juegos):
                    n = len(juegos)
                    gap = n // 2

                    while gap > 0:
                        for i in range(gap, n):
                            temp = juegos[i]
                            j = i

                            while j >= gap and juegos[j - gap].anio > temp.anio:
                                juegos[j] = juegos[j - gap]
                                j -= gap

                            juegos[j] = temp

                        gap //= 2

                shell_sort_anio(juegos)
            elif algoritmo == "quick":
                # Implementar el algoritmo de ordenamiento Quicksort por año
                def partition_anio(juegos, low, high):
                    pivot = juegos[high].anio
                    i = low - 1

                    for j in range(low, high):
                        if juegos[j].anio < pivot:
                            i += 1
                            juegos[i], juegos[j] = juegos[j], juegos[i]

                    juegos[i + 1], juegos[high] = juegos[high], juegos[i + 1]
                    return i + 1


                def quick_sort_anio(juegos, low, high):
                    if low < high:
                        pivot_index = partition_anio(juegos, low, high)
                        quick_sort_anio(juegos, low, pivot_index - 1)
                        quick_sort_anio(juegos, pivot_index + 1, high)

                quick_sort_anio(juegos, 0, len(juegos) - 1)
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
        print("6. Ordenar juegos por año")
        print("0. Salir")

        opcion = input("Ingrese una opción: ")

        if opcion == "1":
            nombre = input("Ingrese el nombre del juego: ")
            anio = int(input("Ingrese el año del juego: "))
            juego = Juego(nombre, anio)
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
            ordenar_juegos(juegos, "anio")
        elif opcion == "0":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Por favor, ingrese una opción válida.")

menu()