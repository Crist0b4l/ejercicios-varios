# -*- coding: utf-8 -*-
"""Ejercicios_varios.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1yLdLyyyrrL5gSiBJBiyy6sPICRW5VdGN
"""

#print("Hola Mundo")

'''nombre = input("Ingrese su nombre y apellido: ")
print (f"Su nombre es {nombre}")

age = int(input("Ingrese su edad: "))
print (f"Su edad es: {age}")'''

''' Comentario de varias lineas (bloque)
Simbolos Matematicos: +, -, -, *, **, /, //, %
Simbolos Relacionales: ==, !=, <, >, <=, >=
Simbolos operadores logicos: and(Y), or(O), xor(o excluyente)
'''

#comentario de linea

#print("Hol\ta \t todos\t\tsoy informatico")

'''#Actividad 1
print("Bienvenido al mundo de la programación")
input("Para comenzar, ingresa tu nombre: ")

#Actividad 2
nom = input("Ingrese su nombre: ")
print(f"Bienvenido {nom}")

#Actividad 3
x = int(input("ingrese el valor de x: "))
calculo = ((x ** 2) + (3 * x) + 1)/4
print(f"El resultado de la ecuacion para el valor de x = {x} es igual a {calculo}")

#Actividad 4
nombre = input("Ingrese su nombre: ")
rut = input("Ingrese su rut: ")
correo = input("Ingrese su correo: ")
tel = int(input("Ingrese su telefono: "))

print(f"NOMBRE: {nombre}\nRUT: {rut}\nCORREO: {correo}\nTELEFONO: {tel}")'''

'''#Ejercicio 1

# Pedimos al usuario que ingrese tres números
num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
num3 = int(input("Ingrese el tercer número: "))

# Calculamos el promedio
suma = num1 + num2 + num3
prom = round(suma/3)

# Imprimimos el resultado
print(f"El resultado de la suma de los tres numeros es: {suma}");
print(f"El resultado del promedio de los tres numeros es: {prom}")

#Ejercicio 2
print("\t\t\t1\n\t\t1\t\t1\n\t1\t\t1\t\t1\n1\t\t1\t\t1\t\t1")'''

'''#Ejemplo Mayor o Menor de edad

edad = int(input("Ingrese su edad: "))
if edad >= 18:
    print("Es mayor de edad")
else:
    print("Es menor de edad")'''

'''#Ejemplo Usuarios empresa XY

user_1 = input("Ingrese su nombre de usuario: ")
pass_1 = input("Ingrese su contraseña: ")

if (user_1 == "pedro" and pass_1 == "1234"):
  print(f"Bienvenido {user_1}")
else:
  print("Usuario o contraseña incorrecta")

user_2 = input("Ingrese su nombre de usuario: ")
pass_2 = input("Ingrese su contraseña: ")

if (user_2 == "angel" and pass_2 == "a4s1"):
  print(f"Bienvenido {user_2}")
else:
  print("Usuario o contraseña incorrecta")'''

'''#Ejercicio 1
puntaje = 0
print("¿Cual de los siguientes animales vive en el agua?:\n1. Perro\n2. Cocodrilo\n3. Conejo\n4. Tiburón")
respuesta = int(input("Ingrese el número de respuesta: "))
if (respuesta == 2 ):
  puntaje = puntaje + 0.5
elif (respuesta == 4):
  puntaje = puntaje + 1.0
elif (respuesta > 4):
  print("Ingrese un número válido")
else:
  puntaje = puntaje
print(f"EL puntaje obtenido en base a su respuesta es: {puntaje}") '''
'''
#Ejercicio 2
puntaje = 0
print("Cuestionario sobre peliculas de Batman")
print("N°1: según IMDB ¿Cual es la mejor pelicula de Batman?(50%)\n1. Batman Begins\n2. Batman El caballero de la noche\n3. Batman El caballero de la noche asciende\n4. Batman y Robin")
respuesta1 = int(input("Ingrese el número de respuesta: "))
if (respuesta1 == 2):
  puntaje += 5
  print("Respuesta correcta")
elif (respuesta1 > 4):
  print("Ingrese un número válido")
else:
  print("Respuesta incorrecta")

print("N°2: ¿Quien es el actor principal en las peliculas de Batman de la saga de Christopher Nolan?(30%)\n1. Christian Bale\n2. Heath Ledger\n3. Tom Hardy\n4. Joaquin Phoenix")
respuesta2 = int(input("Ingrese el número de respuesta: "))
if (respuesta2 == 1):
  puntaje += 3
  print("Respuesta correcta")
elif (respuesta2 > 4):
  print("Ingrese un número válido")
else:
  print("Respuesta incorrecta")

print("N°3 ¿Como se llama el mayordomo de Batman?(20%)\n1. Richard\n2. Robert\n3. Andrew\n4. Alfred")
respuesta3 = int(input("Ingrese el número de respuesta: "))
if (respuesta3 == 4):
  puntaje += 2
  print("Respuesta correcta")
elif (respuesta3 > 4):
  print("Ingrese un número válido")
else:
  print("Respuesta incorrecta")


if (respuesta1 == 2 and respuesta2 == 1 and respuesta3 == 4):
  print(f"Pregunta 1: Correcta\nPregunta 2: Correcta\nPregunta 3: Correcta\nSu puntaje total es {puntaje} y su nota es un 7")
elif (respuesta1 == 2 and respuesta2 == 1 and respuesta3 != 4):
  print(f"Pregunta 1: Correcta\nPregunta 2: Correcta\nPregunta 3: Incorrecta\nSu puntaje total es {puntaje} y su nota es un 5.8")
elif (respuesta1 == 2 and respuesta2 != 1 and respuesta3 == 4):
  print(f"Pregunta 1: Correcta\nPregunta 2: Incorrecta\nPregunta 3: Correcta\nSu puntaje total es {puntaje} y su nota es un 5.2")
elif (respuesta1 != 2 and respuesta2 == 1 and respuesta3 == 4):
  print(f"Pregunta 1: Incorrecta\nPregunta 2: Correcta\nPregunta 3: Correcta\nSu puntaje total es {puntaje} y su nota es un 4.0")
elif (respuesta1 == 2 and respuesta2 != 1 and respuesta3 != 4):
  print(f"Pregunta 1: Correcta\nPregunta 2: Incorrecta\nPregunta 3: Incorrecta\nSu puntaje total es {puntaje} y su nota es un 4.0")
elif (respuesta1 != 2 and respuesta2 == 1 and respuesta3 != 4):
  print(f"Pregunta 1: Incorrecta\nPregunta 2: Correcta\nPregunta 3: Incorrecta\nSu puntaje total es {puntaje} y su nota es un 2.8")
elif (respuesta1 != 2 and respuesta2 != 1 and respuesta3 == 4):
  print(f"Pregunta 1: Incorrecta\nPregunta 2: Incorrecta\nPregunta 3: Correcta\nSu puntaje total es {puntaje} y su nota es un 2.2")
else:
  print(f"Pregunta 1: Incorrecta\nPregunta 2: Incorrecta\nPregunta 3: Incorrecta\nSu puntaje total es {puntaje} y su nota es un 1.0")
'''



'''
# Actividad comparar numeros ingresados

num1 = int(input("Ingrese el primer numero: "))
num2 = int(input("Ingrese el segundo numero: "))
num3 = int(input("Ingrese el tercer numero: "))

if (num1 > num2 and num1>num3):
  print(f"El número {num1} es el mayor")
elif (num2 > num1 and num2>num3):
  print(f"El número {num2} es el mayor")
elif (num3>num1 and num3>num2):
  print(f"El número {num3} es el mayor")

# Actividad hombre y mujer

name = input("Ingrese su nombre:")
age = int(input("Ingrese su edad: "))
genre = input("Ingrese su genero: ")
number = int(input("Ingrese su numero de celular: "))

if (genre == "masculino"):
  print(f"nombre: {name}\nedad: {age}")
elif (genre == "femenino"):
  print (f"nombre: {name}\nnumber: {number}")


# Tabla de multiplicar

num = int(input("Ingrese el numero de la tabla de multiplicar que desea ver: "))
if (num > 0):
  for i in range(11):
    print(f"{num} x {i} = {num*(i)}")
else:
  print("Ingrese un numero valido")

# Tienda
mascarilla = 1000
guantes = 1000
delantal = 2000
amonio = 3000
total = 0
while (True):
  articulo = input("Ingrese el articulo a comprar (o fin para terminar): \nMascarilla\nGuantes\nDelantal\nAmonio\n")
  if (articulo.lower() == "fin"):
    break
  if (articulo == "Mascarilla" or articulo == "mascarilla"):
    cantidad = int(input("Ingrese la cantidad de mascarillas que desea comprar: "))
    total = total + (mascarilla * cantidad)
  elif (articulo == "Guantes" or articulo == "guantes"):
    cantidad = int(input("Ingrese la cantidad de guantes que desea comprar: "))
    total = total + (guantes * cantidad)
  elif (articulo == "Delantal" or articulo == "delantal"):
    cantidad = int(input("Ingrese la cantidad de delantales que desea comprar: "))
    total = total + (delantal * cantidad)
  elif (articulo == "Amonio" or articulo == "amonio"):
    cantidad = int(input("Ingrese la cantidad de amonio que desea comprar: "))
    total = total + (amonio * cantidad)
  else:
    print("Ingrese un articulo valido")

print(f"El total a pagar es: {total}")

#Tienda 2
agua = 600
azucar = 1200
aceite = 1500
arroz = 1250
fideos = 790
bebida = 1780
chocolate = 2500
panMolde = 1340
total = 0

while (True):
  carrito = input("Ingrese el articulo a comprar (o fin para terminar): \nAgua\nAzucar\nAceite\nArroz\nFideos\nBebida\nChocolate\nPan Molde\n")
  if (carrito.lower() == "fin"):
    break
  if (carrito.lower() == "agua"):
    cantidad = int(input("Ingrese la cantidad de agua que desea comprar: "))
    total = total + (agua * cantidad)
  elif (carrito.lower() == "azucar"):
    cantidad = int(input("Ingrese la cantidad de azucar que desea comprar: "))
    total = total + (azucar * cantidad)
  elif (carrito.lower() == "aceite"):
    cantidad = int(input("Ingrese la cantidad de aceite que desea comprar: "))
    total = total + (aceite * cantidad)
  elif (carrito.lower() == "arroz"):
    cantidad = int(input("Ingrese la cantidad de arroz que desea comprar: "))
    total = total + (arroz * cantidad)
  elif (carrito.lower() == "fideos"):
    cantidad = int(input("Ingrese la cantidad de fideos que desea comprar: "))
    total = total + (fideos * cantidad)
  elif (carrito.lower() == "bebida"):
    cantidad = int(input("Ingrese la cantidad de bebida que desea comprar: "))
    total = total + (bebida * cantidad)
  elif (carrito.lower() == "chocolate"):
    cantidad = int(input("Ingrese la cantidad de chocolate que desea comprar: "))
    total = total + (chocolate * cantidad)
  elif (carrito.lower() == "pan molde"):
    cantidad = int(input("Ingrese la cantidad de pan molde que desea comprar: "))
    total = total + (panMolde * cantidad)
  else:
    print("Ingrese un articulo valido")
esPreferencial = input("¿Es cliente preferencial?\n")
if (esPreferencial.lower() == "si"):
    total = total * 0.75
elif (esPreferencial.lower() == "no"):
    total = total
else:
   print("Ingrese una respuesta valida")
print(f"El total a pagar es: {total}")
while (True):
  pago = int(input("Ingrese el efectivo para pagar: "))
  if (pago < total):
    print("!Dinero Insuficiente!")
  else:
    print(f"Su cambio es: ${pago - total}")'''
    break