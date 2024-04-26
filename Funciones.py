# Forma en que se define una función

# def nombre_de_la_función(arg1, arg2, arg3):sentencias
# return   --> El return es opcional
# print(nombre_de_la_función)

def suma(a, b): # Definimos la función, "suma" Tiene 2 parámetros.
    suma = a+b
    return suma # "return" devuelve el resultado de la función.
resultado= suma(5, 3) # Llamada a la función. Hay que pasarle dos parámetros.
# Resultado: 8 
print ("El resultado de la suma es:", resultado)

def concatenar_frase(frase1, frase2):
    concatenacion=frase1+" "+frase2
    return concatenacion
frase_concatenada = concatenar_frase("Me gusta", "Python")
print("Frase concatenada:", frase_concatenada)

def en_pantalla(frase1, frase2): 
    print(frase1, frase2) # return no es obligatorio en_pantalla 
en_pantalla("Me gusta", "Python") # Resultado: Me gusta Python

print ("Frase concatenada:"), en_pantalla("Me encanta", "Python")

# Funciones y Poliformismo
def suma(a, b): # Definimos la
función "suma". Tiene 2 parámetros.
return a+b # "return" devuelve
el resultado de la función.
suma (2, 3) # Función con ints
# Resultado = 5
suma(2.7, 4.0) # Función con floats
# Resultado = 6.7
suma('Me gusta', 'Python') # Función con
strings

# Funciones anidadas
def f1(a): # Función que "encierra"
a f2 (enclosing)
print(a)
b = 100
def f2(x): # Función anidada
print(x) # Llamamos a f2 desde
f1
f2(b)
f1('Python') # Llamamos a f1  --> Resultado Python 100

# Recursividad
def factorial(x):
if x>1:
return x*factorial(x-1)
else:
return 1
factorial(5)

# Devolviendo múltiples valores simultáneamente
def maxmin(lista):
return max(lista), min(lista) #
Devielveuna tupla de 2 elementos
l = [1, 3, 5, 6, 0]
maximo, minimo = maxmin(l) #
Desempaqueta la tupla en 2 variables
print(minimo, maximo, sep= ' ')


