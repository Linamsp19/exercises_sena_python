# 1. Cree un programa que lea la edad de un usuario y muestre cuántos años tendrá el usuario dentro
# de tantos años como este indique. Por ejemplo, si el usuario tiene 20 años y quiere saber cuántos años tendrá dentro de 15 años, el programa deberá mostrar que tendrá 35 años.

# Algoritmo edad_futura
# Entero edad, cantidad_anios, edad_futura
# imprimir("Introduzca su edad: ")
# leer (edad)
# imprimir ("Introduzca años: ")
# leer (cantidad_anios)
# edad_futura = edad + cantidad_anios
# imprimir("Tu edad en", cantidad_anios, " años es ", edad_futura, " años.")
# FinAlgoritmo

# Leer edad
edad = input("Introduzca su edad: ")

# Leer la cantidad de años a visualizar (N)
cantidad_anios = input("Introduzca años: ")

# mostrar edad dentro de n años
edad_futura = int(edad) + int(cantidad_anios)
print(f"Tu edad en {cantidad_anios} años es {edad_futura} años.") 