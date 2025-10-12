def segundos_a_horas(segundos):
    hora = segundos / 3600
    return hora

segundos = float(input("Ingrese los segundos a convertir: "))
print(f"El resultado de la convercion es de: {segundos_a_horas(segundos)}")
