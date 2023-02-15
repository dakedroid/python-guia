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
# Integers
x = int(1)
y = int(2.8)
z = int("3")

# Floats
x = float(1)
y = float(2.8)
z = float("3")
w = float("4.2")

# Strings
x = str("s1")
y = str(2)
z = str(3.0)

# Python Strings - las cadenas en python
# estan rodeadas por comillas simples o
# dobles
print("Hola")
print('Hola')
a = "Adios"
b = 'Adios'
print(a)
print(b)

# Multiline String - Cadenas Multinea
a = """El dia de hoy estamos todos
reunidos en la clase de Ing. del 
conocimiento el 15-feb-2023 10:51:27"""
print(a)

b = '''El dia de hoy estamos todos
reunidos en la clase de Ing. del 
conocimiento el 15-feb-2023 10:51:27'''
print(b)

# Las cadenas son arreglos - Strings are Arrays
# Como muchos lenguajes de programación
# python no tiene el tipo de dato caracter
# Cada cadena es un arreglo de bytes.
nombre = "Oswaldo Sanchez"
print(nombre[0])
print(nombre[1])
print(nombre[2])
print(nombre[3])
print(nombre[4])
print(nombre[5])
print(nombre[6])

# Looping Through a String. For Each
# Recorrer atra ves de una cadena
# para_cada letra en nombre:
#   imprimir letra
for letra in nombre:
    print(letra)

# Imprimir lenght o longitud de un string
print(len(nombre))

# Check String, o checar si
# existe una cadena
txt = "Las mejores cosas en la vida cuestan"
print("vida" in txt)
print("gratis" in txt)

if "vida" in txt:
    print("Si, vida esta presente.")
else:
    print("No esta presente")

# Practica 3: Crear un texto que
# diga "Somos los 10 mejores" y si el texto 10
# esta dentro del string. se debe imprimir
# el numero 10 convertido a int e imprimirlo
# y si no decir que no se encontro.
