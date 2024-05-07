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
        try:
            tarea = self.tareas[indice - 1]
            tarea.marcar_completada()
            print("Tarea marcada como completada.")
        except IndexError:
            print("¡Índice de tarea no válido!")
        except Exception as e:
            print(f"Error: {e}")

    def eliminar_tarea(self, indice):
        try:
            tarea = self.tareas.pop(indice - 1)
            print("Tarea eliminada exitosamente:")
            print(tarea)
        except IndexError:
            print("¡Índice de tarea no válido!")
        except Exception as e:
            print(f"Error: {e}")

# Ejemplo de uso
if __name__ == "__main__":
    gestor = GestorTareas()
    tarea1 = Tarea("Hacer la compra", "Comprar leche, huevos y pan")
    tarea2 = Tarea("Preparar presentación", "Preparar diapositivas para reunión")
    gestor.agregar_tarea(tarea1)
    gestor.agregar_tarea(tarea2)

    gestor.mostrar_tareas()

    try:
        gestor.marcar_completada(3)  # Intentar marcar una tarea con un índice no válido
    except Exception as e:
        print(f"Error: {e}")

    gestor.eliminar_tarea(1)
    gestor.mostrar_tareas()