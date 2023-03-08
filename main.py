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
txt = "Somos los 10 mejores"
if "10" in txt:
    numero = int("10")
    print(numero)
else:
    print("No se encontro el 10")

## Booleans
## Los boleanos se representan con dos valores: True o False
print(True)
print(False)
print(10 > 9)
print(10 == 9)
print(10 < 9)

# Practica 4 crear variable a = 200 y
# variable b = 33 y si b es mayor que a
# imprimir que b y mayor que a
# y si no imprimir que b no es mayor que a
a = 200
b = 33
if b > a:
    print('b=', b, ' es mayor que a=', a)
else:
    print('b=', b, ' no es mayor que a=', a)

## Evaluar valores y variables
print(bool("Hello"))
print(bool(15))
print(bool(True))
print(bool(False))
x = "Hello"
y = 15
print(bool(x))
print(bool(y))
print(bool(""))
print(bool(0))
print(bool(["Marcos", "Baez", "Oswaldo"]))
print(bool([]))
print(bool(()))
print(bool({}))
print(bool(None))


class myclass():
    def __len__(self):
        return 0


myobj = myclass()
print(bool(myobj))


# Funciones que retornan boleanos
def miFuncion():
    return True


if miFuncion():
    print("YES")
else:
    print("NO!")
# Checar si x es instancia de int
x = 200
print(isinstance(x, int))

# Operadores en python se dividen en:
# Arithmetic operators
# Assignment operators
# Comparison operators
# Logical operators
# Identity operators
# Membership operators
# Bitwise operators

# Ejemplo
print(10 + 5)

# Precedencia de Operadores
print((6 + 2) - (6 + 3))

print(100 + 5 * 3)

print(5 + 4 - 7 + 3)

##Imprimir en pantalla utilizando
# jerarquia de operadores
# Crear una variable x = 110
# Y una variable y = 9
# Si x - 10 es igual a 100 y Y * 10 es igual a 90
# Ó x  es != a 70
# Imprimir x al exponente de 2 y dividir entre 2
# y sino  imprimir x utilizando
#  el operador de += 5


# Listas en Python - permite valores duplicados
listaNumeros = [10, 20, 30, 40, 50, 10]
listaStrings = ["FELIX", "JAVIER", "MARCOS", "MARIA", "FELIX"]
print(listaNumeros)
print(listaStrings)
print(listaNumeros[4])
# Imprimir longitud de la lista
print(len(listaNumeros))
print(len(listaStrings))

# Se pueden crear con multiples tipos de datos
lista = ["abc", 34, True, 40, "male"]

# imprimir tipo de dato de la lista
print(type(listaNumeros))
print(type(listaStrings))

## Acceder al ultimo elemento
print(listaNumeros[-1])
print(listaStrings[-2])

# Rango de indices.
print(listaStrings[1:3])
print(listaNumeros[0:2])

print(listaNumeros[:4])
print(listaStrings[4:])

frutas = ["manzana",
          "platano",
          "cherry",
          "naranja",
          "kiwi",
          "melon",
          "mango"]
if "manzana" in frutas:
    print("Si esta 'manzana'")

# Utilizando posiciones negativas imprimir
# cherry, naranja , kiwi y melon sin que se imprima mango.
# de la impresion resultante van a checar con condicion
# Si existe mango, y debe imprimir que no se encontro.
frutasFiltradas = frutas[-5:-1]
print(frutasFiltradas)
if "mango" in frutasFiltradas:
    print("Se encontro")
else:
    print("No se encontro")

# Agregar y eliminar  elementos a la lista
# append agrega al final
frutas.append("Carambola")
print(frutas)

# insert agrega en una posicion especifica
frutas.insert(3, "Sandia")
print(frutas)

# extend une la lista con otra lista diferente.
verduras = ["zanahoria", "brocoli", "lechuga"]
frutas.extend(verduras)

print(frutas)

# Tuplas - son inmutables.
alumnos = ("lic. marcos", "doc. javier", "ing. oswaldo", "ing. felix")
print(alumnos)

# Sets - no permite valores duplicados
alumnas = {"guadalupe", "marisol", "yuliza", "ariana"}
alumnas.add("maria")
alumnas.add("maria")
alumnas.add("ana")
alumnas.remove("ana")
# alumnas.update() es como exends

print(alumnas)

if "guadalupe" in alumnas:
    print("Se encontro guadalupe")
else:
    print("No se encontro")

# Diccionarios - sirve para guardar clave - valor
calificaciones = {
    "Marcos": 100,
    "Oswaldo": 80,
    "Uriel": 70,
    "Javier": 95,
    "Felix": 0
}

carro = {
    "marca": "Tesla",
    "modelo": "X",
    "anio": 2022,
    "pasajeros": ["Kevin", "Marcos", "Felix"],
    "tieneRefaccion": True,
    "velocidades": ("1", "2", "3", "4", "R"),
    "precio": 1000000
}

print(calificaciones)
print(carro)

print(calificaciones["Felix"])