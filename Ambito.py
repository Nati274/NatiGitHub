G = 'Esta variable es de ámbito Global'
def f1():
E='Esta variable es local a f1. Enclosing a f2'
def f2():
L = 'Esta variable es local a f2'
print(L, E, G, sep = '\n')
f2()
f1()

'''Esta variable es local a f2
Esta variable es local a f1. Enclosing a f2
Esta variable está en ámbito Global (de
módulo)'''


G = 'Esta variable es de ámbito Global'
def f1():
E='Esta variable es local a f1. Enclosing a f2'
def f2():
L = 'L es local a f2'
E = 'E también es local a f2'
G = 'G también es local a f2'
print(L, E, G, sep = '\n')
f2()
f1()

'''L es local a f2
E también es local a f2
G también es local a f2'''

G = 'Esta variable es de ámbito Global'
def f1():
E='Esta variable es local a f1. Enclosing a f2'
def f2():
L = 'L es local a f2'
E = 'E también es local a f2'
G = 'G también es local a f2'
print(L, E, G, sep = '\n')
def f3():
print(L) # DEVUELVE ERROR
f2()
f3()
f1()


G = 'Esta variable es de ámbito Global'
def f1():
E='Esta variable es local a f1. Enclosing a f2'
def f2():
L = 'L es local a f2'
E = 'E también es local a f2'
G = 'G también es local a f2'
print(L, E, G, sep = '\n')
def f3():
print(E, G, sep = '\n')
f2()
f3()
f1()


def suma(a, b): # Modificamos a y b en el scope de suma() Objeto inmutable
a = 3
b = 4
return a+b
a, b = 5, 10
print(suma(a, b))
print(a, b) # a y b no han cambiado fuera de la función

# Objeto mutable
def minimo(l):
l[0] = 1000 # Modificamos la lista en el interior
return min(l)
l = [1, 2, 3]
print(l)
print(minimo(l)) # Modifica la lista aquí
print(l)


def minimo(l):
l[0] = 1000 # Modificamos la lista en el interior
return min(l)
l = [1, 2, 3]
print(minimo(l[:])) # minimo modifica la lista aquí
print(l)
