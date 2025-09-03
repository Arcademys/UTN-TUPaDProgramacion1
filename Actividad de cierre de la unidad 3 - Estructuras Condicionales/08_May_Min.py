name = input("Ingrese su nombre:")
option = int(input("Selecione 1) Mayusculas 2) Minusculas 3) Capitalizado"))

if option == 1:
    print(str.upper(name))
elif option == 2:
    print(str.lower(name))
elif option == 3:
    print(str.title(name))
else:
    print(f"ERROR")

