class Electrodomestico:
    def __init__(self, nombre, anio):
        self.nombre = nombre
        self.anio = anio

    def __str__(self):
        return f"{self.nombre} ({self.anio})"


def mostrar_electrodomesticos(electrodomesticos):
    if electrodomesticos:
        print("Electrodomésticos ingresados:")
        for electrodomestico in electrodomesticos:
            print(electrodomestico)
    else:
        print("No se han ingresado electrodomésticos.")


def eliminar_electrodomestico(electrodomesticos):
    if electrodomesticos:
        nombre = input("Ingrese el nombre del electrodoméstico a eliminar: ")
        electrodomesticos = [electrodomestico for electrodomestico in electrodomesticos if electrodomestico.nombre != nombre]
        print("Electrodoméstico eliminado exitosamente.")
    else:
        print("No se han ingresado electrodomésticos.")


def modificar_electrodomestico(electrodomesticos):
    if electrodomesticos:
        nombre = input("Ingrese el nombre del electrodoméstico a modificar: ")
        for electrodomestico in electrodomesticos:
            if electrodomestico.nombre == nombre:
                nuevo_nombre = input("Ingrese el nuevo nombre del electrodoméstico: ")
                nuevo_anio = int(input("Ingrese el nuevo año del electrodoméstico: "))
                electrodomestico.nombre = nuevo_nombre
                electrodomestico.anio = nuevo_anio
                print("Electrodoméstico modificado exitosamente.")
                return
        print("No se encontró un electrodoméstico con ese nombre.")
    else:
        print("No se han ingresado electrodomésticos.")


def ordenar_electrodomesticos(electrodomesticos, criterio):
    if electrodomesticos:
        if criterio == "nombre":
            algoritmo = input("Ingrese el algoritmo de ordenamiento a utilizar (burbuja, shell, quick): ")
            if algoritmo == "burbuja":
                electrodomesticos.sort(key=lambda electrodomestico: electrodomestico.nombre)
            elif algoritmo == "shell":
                # Implementar el algoritmo de ordenamiento ShellSort por nombre
                def shell_sort_nombre(electrodomesticos):
                    n = len(electrodomesticos)
                    gap = n // 2

                    while gap > 0:
                        for i in range(gap, n):
                            temp = electrodomesticos[i]
                            j = i

                            while j >= gap and electrodomesticos[j - gap].nombre > temp.nombre:
                                electrodomesticos[j] = electrodomesticos[j - gap]
                                j -= gap

                            electrodomesticos[j] = temp

                        gap //= 2

            elif algoritmo == "quick":
                # Implementar el algoritmo de ordenamiento Quicksort por nombre
                def partition_nombre(electrodomesticos, low, high):
                    pivot = electrodomesticos[high].nombre
                    i = low - 1

                    for j in range(low, high):
                        if electrodomesticos[j].nombre < pivot:
                            i += 1
                            electrodomesticos[i], electrodomesticos[j] = electrodomesticos[j], electrodomesticos[i]

                    electrodomesticos[i + 1], electrodomesticos[high] = electrodomesticos[high], electrodomesticos[i + 1]
                    return i + 1

                def quick_sort_nombre(electrodomesticos, low, high):
                    if low < high:
                        pivot_index = partition_nombre(electrodomesticos, low, high)
                        quick_sort_nombre(electrodomesticos, low, pivot_index - 1)
                        quick_sort_nombre(electrodomesticos, pivot_index + 1, high)

                def quicksort_por_nombre(electrodomesticos):
                    quick_sort_nombre(electrodomesticos, 0, len(electrodomesticos) - 1)
            else:
                print("Algoritmo de ordenamiento inválido.")
        elif criterio == "anio":
            algoritmo = input("Ingrese el algoritmo de ordenamiento a utilizar (burbuja, shell, quick): ")
            if algoritmo == "burbuja":
                electrodomesticos.sort(key=lambda electrodomestico: electrodomestico.anio)
            elif algoritmo == "shell":
                # Implementar el algoritmo de ordenamiento ShellSort por año
                def shell_sort_anio(electrodomesticos):
                    n = len(electrodomesticos)
                    gap = n // 2

                    while gap > 0:
                        for i in range(gap, n):
                            temp = electrodomesticos[i]
                            j = i

                            while j >= gap and electrodomesticos[j - gap].anio > temp.anio:
                                electrodomesticos[j] = electrodomesticos[j - gap]
                                j -= gap

                            electrodomesticos[j] = temp

                        gap //= 2

            elif algoritmo == "quick":
                # Implementar el algoritmo de ordenamiento Quicksort por año
                def partition_anio(electrodomesticos, low, high):
                    pivot = electrodomesticos[high].anio
                    i = low - 1

                    for j in range(low, high):
                        if electrodomesticos[j].anio < pivot:
                            i += 1
                            electrodomesticos[i], electrodomesticos[j] = electrodomesticos[j], electrodomesticos[i]

                    electrodomesticos[i + 1], electrodomesticos[high] = electrodomesticos[high], electrodomesticos[i + 1]
                    return i + 1

                def quick_sort_anio(electrodomesticos, low, high):
                    if low < high:
                        pivot_index = partition_anio(electrodomesticos, low, high)
                        quick_sort_anio(electrodomesticos, low, pivot_index - 1)
                        quick_sort_anio(electrodomesticos, pivot_index + 1, high)

                def quicksort_por_anio(electrodomesticos):
                    quick_sort_anio(electrodomesticos, 0, len(electrodomesticos) - 1)
            else:
                print("Algoritmo de ordenamiento inválido.")
        else:
            print("Criterio de ordenamiento inválido.")
    else:
        print("No se han ingresado electrodomésticos.")


def menu():
    electrodomesticos = []

    while True:
        print("------ MENÚ ------")
        print("1. Ingresar electrodoméstico")
        print("2. Mostrar electrodomésticos")
        print("3. Eliminar electrodoméstico")
        print("4. Modificar electrodoméstico")
        print("5. Ordenar electrodomésticos por nombre")
        print("6. Ordenar electrodomésticos por año")
        print("0. Salir")

        opcion = input("Ingrese una opción: ")

        if opcion == "1":
            nombre = input("Ingrese el nombre del electrodoméstico: ")
            anio = int(input("Ingrese el año del electrodoméstico: "))
            electrodomestico = Electrodomestico(nombre, anio)
            electrodomesticos.append(electrodomestico)
            print("Electrodoméstico ingresado exitosamente.")
        elif opcion == "2":
            mostrar_electrodomesticos(electrodomesticos)
        elif opcion == "3":
            eliminar_electrodomestico(electrodomesticos)
        elif opcion == "4":
            modificar_electrodomestico(electrodomesticos)
        elif opcion == "5":
            ordenar_electrodomesticos(electrodomesticos, "nombre")
        elif opcion == "6":
            ordenar_electrodomesticos(electrodomesticos, "anio")
        elif opcion == "0":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Por favor, ingrese una opción válida.")

menu()
