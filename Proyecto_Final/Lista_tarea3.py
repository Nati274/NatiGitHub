#Creamos dos clases: Tarea y GestorTareas
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
        self.tareas.append(tarea) #    def mostrar_tareas(self):
        if not self.tareas: #Manejo de excepciones
            print("No hay tareas pendientes.")
            return
        for i, tarea in enumerate(self.tareas, start=1):
            print(f"Tarea {i}:\n{tarea}") 

    def mostrar_tareas(self):
        if not self.tareas: #Manejo de excepciones
            print("No hay tareas pendientes.")
            return
        for i, tarea in enumerate(self.tareas, start=1):
            print(f"Tarea {i}:\n{tarea}")

    def marcar_completada(self, indice):
        if 1 <= indice <= len(self.tareas): 
            self.tareas[indice - 1].marcar_completada()  
        else:
            print("¡Índice de tarea no válido!") 
    def eliminar_tarea(self, indice):
        if 1 <= indice <= len(self.tareas):
            del self.tareas[indice - 1]
            print("Tarea eliminada exitosamente.")
        else:
            print("¡Índice de tarea no válido!")



# Ejemplo de uso
if __name__ == "__main__":
    gestor = GestorTareas()
    '''El programa solicitará al usuario que ingrese el nombre y la descripción de la tarea. 
    Cuando el usuario ingresa "fin", el bucle se detiene y se muestran todas las tareas ingresadas.'''
    while True:
        nombre = input("Ingrese el nombre de la tarea (o escriba 'fin' para terminar): ")
        if nombre.lower() == "fin":
            break
        descripcion = input("Ingrese la descripción de la tarea: ")
        nueva_tarea = Tarea(nombre, descripcion)
        gestor.agregar_tarea(nueva_tarea)

    gestor.mostrar_tareas()
    '''Después de que se muestren las tareas, se solicitará al usuario que ingrese 'c' para marcar una tarea como completada, 
    e' para eliminar una tarea o 'fin' para terminar. Dependiendo de la opción elegida, se pedirá al usuario que ingrese el 
    índice de la tarea correspondiente y se realizará la acción correspondiente. Después de cada acción, 
    se mostrarán las tareas actualizadas. El proceso continuará hasta que el usuario escriba "fin".'''
    if gestor.tareas:
        while True:
            opcion = input("Ingrese 'c' para marcar una tarea como completada, 'e' para eliminar una tarea, o 'fin' para terminar: ")
            if opcion.lower() == "fin":
                break
            elif opcion.lower() == "c":
                indice = input("Ingrese el índice de la tarea que desea marcar como completada: ")
                try:
                    indice = int(indice)
                    gestor.marcar_completada(indice)
                    gestor.mostrar_tareas()
                except ValueError:
                    print("¡Índice de tarea no válido!")
            elif opcion.lower() == "e":
                indice = input("Ingrese el índice de la tarea que desea eliminar: ")
                try:
                    indice = int(indice)
                    gestor.eliminar_tarea(indice)
                    gestor.mostrar_tareas()
                except ValueError:
                    print("¡Índice de tarea no válido!")
            else:
                print("Opción no válida. Por favor, ingrese 'c', 'e' o 'fin'.")

    print("Tareas restantes:")
    gestor.mostrar_tareas()