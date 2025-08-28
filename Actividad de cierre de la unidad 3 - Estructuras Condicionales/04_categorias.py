edad = int(input("Ingrese su esdad:"))

if edad < 12:
    print("Nino/a")
elif edad >= 12 and edad > 18:
    print("Adolecente")
elif edad >= 18 and edad > 30:
    print("Adulto joven")
else:
    print ("Adulto")
    