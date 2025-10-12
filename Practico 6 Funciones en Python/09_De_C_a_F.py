def celsius_a_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit


celsius = float(input("Ingrese la temperatura en grados Celsius: "))


fahrenheit = celsius_a_fahrenheit(celsius)
print(f"{celsius:.2f}°C equivalen a {fahrenheit:.2f}°F")

