# 1. Cree un programa que lea la edad de un usuario y muestre cuántos años tendrá el usuario dentro
# de tantos años como este indique. Por ejemplo, si el usuario tiene 20 años y quiere saber cuántos años tendrá dentro de 15 años, el programa deberá mostrar que tendrá 35 años.

# -*- encoding UTF-8 -*-
#algoritmo edad
    # Leer edad
    # Leer la cantidad de años a visualizar (N)
    # mostrar edad dentro de n años
#FinAlgoritmo


edad = input("Introduzca su edad: ")
cantidad_anios = input("Introduzca años: ")
print(int(edad) + int(cantidad_anios))


# 2. Cree un programa que lea dos números y muestre su producto, su cociente, su módulo, su suma y su resta.

# Algoritmo operaciones
#    Real numero1, numero2, suma, resta, multip, modulo, cociente
#   logico error_division = False
#   Imprimir("Ingrese un numero")

numero1 = input("Ingrese un número: ")
numero2 = input("Ingrese otro número ")

# primero sucede lo que está en el parentesis más interno hacia afuera.
numero1 = float(numero1)
numero2 = float(numero2)

suma = numero1 + numero2
resta = numero1 - numero2
multip = numero1 * numero2
if numero2 != 0 : #si el número2 es diferente a 0
    modulo = numero1 % numero2
    cociente = numero1 / numero2
else
modulo = "indeterminado"
cociente = "indeterminado"

print(f"la suma de los dos número es: {suma}"f"la resta de los dos números es: {resta}", f"la multiplicación de los dos números es: {multip}",f"el modulo de los dos números es: {modulo}" f"el cociente de los dos números es {cociente}")

# 3. Cree un programa que lea el monto de un préstamo y el plazo en meses, y muestre al usuario el valor de las cuotas mensuales pagando un interés fijo del 2.7% mensual.

# Algoritmo prestamo
# Constante Real INTERES = 2.7
# Entero prestamo, plazo
# Real cuota_mensual_neta, valor_interes, cuota_mensual
# imprimir("Introduzca monto de préstamo: $")
# leer(prestamo)
# imprimir("Introduzca el plazo: ")
# leer(plazo)
# cuota_mensual_neta = prestamo / plazo
# valor_interes = INTERES / 100 * cuota_mensual_neta
# cuota_mensual = cuota_mensual_neta + valor_interes
# imprimir("El valor de su cuota es ", cuota_mensual, "dinero")
# FinAlgoritmo

# Leer monto de un prestamo
INTERES = 2.7
prestamo = input("Introduzca monto de prestamo: ") # 1000


# Leer plazo a mensuales
plazo = input("Introduzca el plazo: ") # 2 meses

# Conversión de los valores
prestamo = int(prestamo)
plazo = int(plazo)

# Mostrar al usuario el valor de las cuotas

cuota_mensual_neta = prestamo / plazo # 250
valor_interes = INTERES / 100 * cuota_mensual_neta # 6.75 INTERES MENSUAL
cuota_mensual = cuota_mensual_neta + valor_interes # 256.75

print(f"El valor de su cuota es ${cuota_mensual} dinero")