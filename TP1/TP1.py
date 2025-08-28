##TRABAJOPRACTICO1##

## Ejercicio 1 ##
print ("hola, mundo")

## Ejercicio 2 ##

name = input("Ingrese su nombre:")

print(f"Hola {name}, como estas?")


## Ejercicio 3 ##

name = input("Ingrese su nombre:")
lastname = input("Ingrese su apellido:")
age = int(input("Ingrese su edad:"))
home = input("Ingrese lugar de residencia:")

print (f"Bienvenido al sistema {name} {lastname}, tu edad es {age} y vives en {home}. ")

## Ejercicio 4 ##

pi = 3.1416
r = float (input("Escribe el radio de tu circulo:"))
a = pi * r**2
p = 2 * pi * r

print (f"Segun el radio proporcionado el area es de:{a}, y el perimetro es de:{p}.")


## Ejercicio 5 ##

seg = 3600
hora = int(input("Ingresa los segundos:"))
hora = hora * seg
print (f"La catindad de segundos por  hora es de:{hora}")


## Ejercicio 6 ##

x = int(input("Ingresa un numero:"))

for i in range(0,11):
    y = x * i
    print(f" {x} x {i} =  {y} ")


## Ejercicio 7 ##

nro1 = int(input("Ingrese un numero:"))
nro2 = int(input("Ingrese otro numero:"))

resu1 = nro1 + nro2
resu2 = nro1 - nro2
resu3 = nro1 * nro2
resu4 = float(nro1/nro2)

if nro1 == 0 or nro2 == 0:
    print("Error")
else:
    print(f"El resultado de la suma es de:{resu1}, de la resta:{resu2}, de la multiplicaciones de:{resu3}, de la division: {resu4}.")


## Ejercicio 8 ##

alt = float(input("Ingrese su altura: "))
peso = float(input("Ingrese su peso: "))

imc = peso / alt**2

print(f"Su indice de masa corporal es de: {imc:.2f}.")


## Ejercicio 9 ##

cel = int(input("Ingrese la temperatura CEL:"))
f = (cel * 1.8) + 32
print(f"Fahrenheit:{f}")


## Ejercicio 10 ##
nro1 = int(input("Ingrese un numeroro:"))
nro2 = int(input("Ingrese otro numero:"))
nro3 = int(input("Ingrese otro numero:"))

rta = (nro1 + nro2 + nro3)/ 3
print (f"El promedio de los nros ingresados es de:{rta}")


############################################################
