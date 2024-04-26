
#   find() retorna la posición de la primera similitud de la substring

cadenaDeTexto = "Es peor cometer una injusticia que padecerla porque quien la comete se convierte en injusto y quien la padece no."
print(cadenaDeTexto.find('quien'))

#   Devolvería: 52

# ----------------------------------------------------------------

#   rfind() retorna la última posición de la similitud de la substring.

cadenaDeTexto = "Es peor cometer una injusticia que padecerla porque quien la comete se convierte en injusto y la padece no."
print(cadenaDeTexto.rfind('quien'))

#   Devolvería: 94
#   Si, el substring no es encontrado retorna -1.

# ******Comentar con el profesor que no devuelve -1 , devuelve nuevamente 52******

# ----------------------------------------------------------------