# Creamos dos clases: Tarea y GestorTareas
class Tarea:
    def __init__(self, nombre, descripcion, completada=False):
        self.nombre = nombre
        self.descripcion = descripcion
        self.completada = completada

    def marcar_completada(self):
        self.completada = True

    def __str__(self):
        estado = "Completada" if self.completada else "Pendiente"
        return f"Tarea: {self.nombre}\nDescripción: {self.descripcion}\nEstado: {estado}\n"

class GestorTareas:
    def __init__(self):
        self.tareas = []

    def agregar_tarea(self, tarea):
        self.tareas.append(tarea)

    def mostrar_tareas(self):
        if not self.tareas:
            print("No hay tareas pendientes.")
            return
        for i, tarea in enumerate(self.tareas, start=1):
            print(f"Tarea {i}:\n{tarea}")

    def marcar_completada(self, indice):
        if 1 <= indice <= len(self.tareas):
            self.tareas[indice - 1].marcar_completada()
            print("Tarea marcada como completada.")
        else:
            print("¡Índice de tarea no válido!")

    def eliminar_tarea(self, indice):
        if 1 <= indice <= len(self.tareas):
            del self.tareas[indice - 1]
            print("Tarea eliminada exitosamente.")
        else:
            print("¡Índice de tarea no válido!")

# Función para mostrar el menú y manejar las opciones del usuario
def mostrar_menu():
    print("\n*** Menú ***")
    print("1. Agregar tarea")
    print("2. Marcar tarea como completada")
    print("3. Eliminar tarea")
    print("4. Mostrar tareas")
    print("5. Salir")

if __name__ == "__main__":
    gestor = GestorTareas()
    
    while True:
        mostrar_menu()
        opcion = input("Ingrese el número de la opción que desea realizar: ")

        '''función mostrar_menu() que muestra las opciones disponibles para el usuario. Luego, en el bucle principal, 
        se solicita al usuario que ingrese el número de la opción que desea realizar. Dependiendo de la opción elegida, 
        se realiza la acción correspondiente. El bucle continuará hasta que el usuario elija salir del programa.'''

        if opcion == "1":
            nombre = input("Ingrese el nombre de la tarea: ")
            descripcion = input("Ingrese la descripción de la tarea: ")
            nueva_tarea = Tarea(nombre, descripcion)
            gestor.agregar_tarea(nueva_tarea)
        elif opcion == "2":
            gestor.mostrar_tareas()
            indice = int(input("Ingrese el índice de la tarea que desea marcar como completada: "))
            gestor.marcar_completada(indice)
        elif opcion == "3":
            gestor.mostrar_tareas()
            indice = int(input("Ingrese el índice de la tarea que desea eliminar: "))
            gestor.eliminar_tarea(indice)
        elif opcion == "4":
            gestor.mostrar_tareas()
        elif opcion == "5":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Por favor, ingrese un número del 1 al 5.")