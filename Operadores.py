# **** Tabla de operadores ****

X = 5

yield x  # Protocolo de generadores “send”
lambda args: expresión # Función anónima
x if y else z  # Selección ternaria (retorna x si y es cierta)
x or y # OR lógico (y es evaluada sólo si x es falsa)
x and y # AND lógico (y es evaluada sólo si x es verdadera)
not x # Negación Lógica
x in y, x not in y # Operadores de membresía
x is y, y is not y # Operadores de identidad
x < y, x<= y, x > y, x >= y # Comparación de magnitudes. Set, subset y superset
x == y, x != y # Operadores de igualdad
x | y  # Bit a bit (bitwise) OR. Unión de sets (conjuntos)
x ^ y  # Bitwise XOR. Diferencia simétrica de sets
x & y  # Bit a bit AND. Intersección de sets (conjuntos)
x << y, x >> y  # Desplazamiento de x en y bits a izquierda y derecha
x + y  # Adición. Concatenación
x - y  # Substración. Diferencia entre sets (conjuntos)
x * y  # Multiplicación. Repetición
x % y  # Resto de la división
x / y  # División real (verdadera)
x // y  # División truncada
-x, +x  # Negación. Identidad
~x  # Negación Bit a bit
x ** y  # Potencia (exponenciación)
x[i]  # Indexado (secuencias, mapeados, otros)
x[i:j:k]  # Troceado (slicing)
x(...)  # Llamada (función, método, clase, etc.)
x.attr  # Referencia a un atributo
(...)  # Tupla, expresión, expresión de generador
[...]  # Lista, lista por comprensión
{...}  # Diccionario, Set, comprensión de diccionarios y sets

2*3+2*4 # Multiplicación precede a suma
2*(3+2)*4 # Expresiones entre paréntesis se evaluan primero