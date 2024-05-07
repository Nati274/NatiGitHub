#Creamos dos clases: Tarea y GestorTareas

#La clase Tarea representa una tarea individual con atributos como 
#nombre, descripción y estado de completado. 
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

#La clase GestorTareas gestiona una lista de tareas y proporciona métodos 
#para agregar tareas, mostrar tareas y marcar tareas como completadas.
class GestorTareas:
    def __init__(self):
        self.tareas = []

#En resumen, toma una tarea como argumento y la añade a la lista de tareas. 
#Esto permite mantener un registro de todas las tareas pendientes dentro de 
#la aplicación de gestión de tareas.
#agregar una tarea a la lista de tareas gestionada por esta clase
#Toma dos parámetros: self, que es una referencia a la instancia 
#de la clase actual, y tarea, que es el objeto de tipo Tarea que 
#queremos agregar a la lista.
    def agregar_tarea(self, tarea):
        self.tareas.append(tarea) #Dentro del método, utilizamos el atributo 
        #tareas de la instancia actual (self.tareas) para acceder a la lista 
        #de tareas. Luego, utilizamos el método append() de las listas en Python 
        #para agregar la tarea proporcionada como argumento (tarea) a esta lista.

# imprime en la consola todas las tareas almacenadas en la lista de tareas de la 
#instancia actual de la clase GestorTareas, numerándolas para facilitar su identificación.
    def mostrar_tareas(self):
        if not self.tareas: #Manejo de excepciones
            print("No hay tareas pendientes.")
            return
        for i, tarea in enumerate(self.tareas, start=1):
            print(f"Tarea {i}:\n{tarea}") # Utilizamos un bucle for para iterar sobre todas 
            #las tareas almacenadas en la lista self.tareas. La función enumerate() nos permite 
            #iterar sobre los elementos de la lista self.tareas y al mismo tiempo obtener el índice 
            #de cada tarea. El argumento start=1 especifica que queremos que los índices comiencen 
            #en 1 en lugar de en 0.
            #Dentro del bucle, imprimimos cada tarea junto con su número de índice correspondiente. 
            #Usamos una cadena de formato (f-string) para incluir el número de tarea (i) y la 
            #descripción de la tarea (tarea). La variable i contiene el número de índice de la tarea 
            #actual, y tarea es el objeto de tipo Tarea que representa la tarea actual.

#permite marcar una tarea como completada utilizando su índice en la lista de tareas gestionadas
#por la instancia actual de la clase GestorTareas. Si el índice proporcionado es válido, se marca
#la tarea correspondiente como completada; de lo contrario, se imprime un mensaje de error.
    def marcar_completada(self, indice): #Esta línea define el método marcar_completada que 
        #pertenece a la clase GestorTareas. Al igual que en los otros casos, toma dos parámetros:
        #self, que es una referencia a la instancia de la clase actual, y indice, que representa 
        #el índice de la tarea que se desea marcar como completada.
        if 1 <= indice <= len(self.tareas): #Esta línea verifica si el índice proporcionado (indice)
            #está dentro del rango válido de índices de la lista de tareas (self.tareas). Comparamos 
            #el índice con el rango de valores válido, que va desde 1 hasta la longitud de la lista 
            #de tareas (len(self.tareas)).
            self.tareas[indice - 1].marcar_completada()  #Si el índice proporcionado es válido, accedemos
            #a la tarea correspondiente en la lista de tareas utilizando la notación de indexación 
            #(self.tareas[indice - 1]). Luego, llamamos al método marcar_completada() de la clase Tarea 
            #para marcar la tarea como completada.
        else:
            print("¡Índice de tarea no válido!") #Si el índice proporcionado no es válido (es decir, 
            #está fuera del rango de índices de la lista de tareas), imprimimos un mensaje de error.

#elimina una tarea específica de la lista de tareas según su índice. 
#Este método verifica si el índice proporcionado está dentro 
#del rango válido antes de eliminar la tarea correspondiente.
    def eliminar_tarea(self, indice):
        if 1 <= indice <= len(self.tareas):
            del self.tareas[indice - 1]
            print("Tarea eliminada exitosamente.")
        else:
            print("¡Índice de tarea no válido!")


# Ejemplo de uso
if __name__ == "__main__":
    gestor = GestorTareas()
    tarea1 = Tarea("Hacer la compra", "Comprar leche, huevos y pan")
    tarea2 = Tarea("Preparar presentación", "Preparar diapositivas para reunión")
    gestor.agregar_tarea(tarea1)
    gestor.agregar_tarea(tarea2)

    gestor.mostrar_tareas()

    gestor.marcar_completada(1)
    gestor.mostrar_tareas()

    gestor.eliminar_tarea(1)
    gestor.mostrar_tareas()

