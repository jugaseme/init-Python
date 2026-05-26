print ("holis")
#comerntario#
yo ="sevastian"
print (yo)

#variables#
meros = ["hola", "como estas", "bien", "mal"]
print (meros [0])

#listas#
jugadores = {
    "1": "sebastian",
    "2": "maria"}
print (jugadores["2"])

#constantes#
pi = 3.1416

#operadores#
a = 10
b = 5
suma = a + b
resta = a - b
multiplicacion = a * b
division = a / b
print ("suma:", suma)
print ("resta:", resta)

#comparativos#
print (a == b )
print (a > b)
print (a < b)
print (a >= b)
print (a <= b)
print (a != b) 

entero = 10
print (entero is entero)

#operadores logicos#
print (a and b)
print (a or b)
print (not a)

#condicionales#
autorizado = True
if autorizado:
    print ("Acceso permitido")
else:    
    print ("Acceso denegado")



if entero == 9:
    print ("El número es 9")
elif entero == 10:
    print ("El número es 10")
else:   
    print ("El número no es ni 9 ni 10")

color = "rojo"
match color:
    case "rojo":
        print ("El color es rojo")
    case "azul":
        print ("El color es azul")
    case _:
        print ("El color no es ni rojo ni azul")

#funciones#
def sumar (primero , segundo):
    resultado = primero + segundo
    return resultado
    
sumar (3, 5)

#loops#
animales = ["perro", "gato", "conejo"]
for animal in animales:
    print (animal)

 

def multiplicador (primero, segundo):
    print (primero * segundo)

numeros =[1,23,23,54,23,54,23,54,23,54]

for numero in numeros:
    multiplicador (numero, 2)

emergencia = 15

while entero < emergencia:
    print (entero)
    entero += 1

import modulo

modulo.restar(10, 5)