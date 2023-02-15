# Sintaxis General
print("Hola Mundo")
print('lA SUMA DE 1 MAS 2 ES: ', 1 + 2)
if 5 > 2:
    print('Cinco es mayor que 2')
print('Termino')

# Variables
nombre = 'Marcos'
Nombre = "said"
edad = 20
monto = 200.30
print(nombre, edad)

# Casting
mensaje = nombre + "tiene " + str(edad) + " años"
premio = monto + float(10)
cantidad = edad + int(1.0)
print(mensaje, premio, cantidad)

# Types - tipos
print(type(mensaje))
print(type(premio))
print(type(cantidad))
if type(mensaje) == str:
    print("ES STRING")
if isinstance(mensaje, str):
    print("ES STRING")

# Escribir un programa donde se cree la variable x = 2
# Y una variable y = “3” con comillas, el programa
# tiene que imprimir la suma de ambos números pero
# tiene que hacer una condición si el tipo de dato es
# String convertirlo a int para poder hacer la suma
x = "2"
y = 3
if type(x) == str:
    x = int(x)
if type(y) == str:
    y = int(y)
resultado = x + y
print("El resultado es: ", resultado)

# Numbers - Numeros
# int, float, complex

x = 1  # Float
y = 2.8  # Float
z = 1j  # Complex

print(type(x))
print(type(y))
print(type(z))

# Int o Integer is un numero positivo
# o negativo sin decimales y de longitud ilimitada
x = 1
y = 35656222554887711
z = -3255522
print(type(x))
print(type(y))
print(type(z))

# Float o numero de coma flotante es un numero
# Positivo o negativo que contiene uno o mas
# decimales.
x = 1.10
y = 1.0
z = -35.59
print(type(x))
print(type(y))
print(type(z))

# Float puede ser usado para numeros cientificos
# con la "e" indicando la potencia de 10.
x = 35e3
y = 12E4
z = -87.7e100
print(type(x))
print(type(y))
print(type(z))

# Los numeros complejos estan excritos con la letra
# j como la parte imaginaria
x = 3 + 5j
y = 5j
z = -5j
print(type(x))
print(type(y))
print(type(z))

# Practica 2: Crear x, y,z con los siguientes valores
# 1, 2.8, 1j
# crear variable a = Convertir x de entero a flotante
# Crear variable b = Convertir y de float a int
# crear variable c = Convertir x de int a complex
# imprimir a, b ,c e imprimir el tipo de a,b,c.
x = 1
y = 2.8
z = 1j
a = float(x)
b = int(y)
c = complex(x)
print(a)
print(b)
print(c)
print(type(a))
print(type(b))
print(type(c))

# Casting
# lo que escribio kevin

