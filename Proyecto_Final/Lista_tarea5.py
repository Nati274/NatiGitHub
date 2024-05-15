from colorama import init, Fore, Style

# Inicializar colorama
init(autoreset=True)

# Creamos dos clases: Tarea y GestorTareas
class Tarea:
    def __init__(self, nombre, descripcion, completada=False):
        self.nombre = nombre
        self.descripcion = descripcion
        self.completada = completada

    def marcar_completada(self):
        self.completada = True

    def __str__(self):
        estado = Fore.GREEN + "Completada" if self.completada else Fore.RED + "Pendiente"
        return f"Tarea: {self.nombre}\nDescripción: {self.descripcion}\nEstado: {estado}\n" + Style.RESET_ALL

class GestorTareas:
    def __init__(self):
        self.tareas = []

    def agregar_tarea(self, tarea):
        self.tareas.append(tarea)

    def mostrar_tareas(self):
        if not self.tareas:
            print("No hay tareas pendientes.")
            return
        print("┌──────────────────────────────────────────┐")
        for i, tarea in enumerate(self.tareas, start=1):
            print("│" + f"Tarea {i}: {tarea}".ljust(28) + "│")
        print("└───────────────────────────────────────────┘")

    def marcar_completada(self, indice):
        if 1 <= indice <= len(self.tareas):
            self.tareas[indice - 1].marcar_completada()
            print(Fore.GREEN + "Tarea marcada como completada.")
        else:
            print(Fore.RED + "¡Índice de tarea no válido!")

    def eliminar_tarea(self, indice):
        if 1 <= indice <= len(self.tareas):
            del self.tareas[indice - 1]
            print(Fore.GREEN + "Tarea eliminada exitosamente.")
        else:
            print(Fore.RED + "¡Índice de tarea no válido!")

# Función para mostrar el menú y manejar las opciones del usuario
def mostrar_menu():
    print(Fore.CYAN + "┌────────────────────────────────┐")
    print("│" + Fore.YELLOW + "           Menú           " + Fore.CYAN + "      │")
    print("│" + Fore.YELLOW + "1. Agregar tarea" + " " * 10 + Fore.CYAN + "      │")
    print("│" + Fore.YELLOW + "2. Marcar tarea como completada" + Fore.CYAN + " │")
    print("│" + Fore.YELLOW + "3. Eliminar tarea" + " " * 8 + Fore.CYAN + "       │")
    print("│" + Fore.YELLOW + "4. Mostrar tareas" + " " * 8 + Fore.CYAN + "       │")
    print("│" + Fore.YELLOW + "5. Salir" + " " * 15 + Fore.CYAN + "         │")
    print("└────────────────────────────────┘")

if __name__ == "__main__":
    gestor = GestorTareas()
    
    while True:
        mostrar_menu()
        opcion = input(Fore.CYAN + "Ingrese el número de la opción que desea realizar: ")

        if opcion == "1":
            nombre = input(Fore.YELLOW + "Ingrese el nombre de la tarea: ")
            descripcion = input("Ingrese la descripción de la tarea: ")
            nueva_tarea = Tarea(nombre, descripcion)
            gestor.agregar_tarea(nueva_tarea)
        elif opcion == "2":
            gestor.mostrar_tareas()
            indice = int(input(Fore.YELLOW + "Ingrese el índice de la tarea que desea marcar como completada: "))
            gestor.marcar_completada(indice)
        elif opcion == "3":
            gestor.mostrar_tareas()
            indice = int(input(Fore.YELLOW + "Ingrese el índice de la tarea que desea eliminar: "))
            gestor.eliminar_tarea(indice)
        elif opcion == "4":
            gestor.mostrar_tareas()
        elif opcion == "5":
            print(Fore.CYAN + "Saliendo del programa...")
            break
        else:
            print(Fore.RED + "Opción no válida. Por favor, ingrese un número del 1 al 5.")