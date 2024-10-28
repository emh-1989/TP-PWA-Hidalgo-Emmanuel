# Solicitar al usuario una calificación del 0 al 100
calificacion = int(input("Ingrese una calificación del 0 al 100: "))

# Determinar la calificación alfabética 
if 0 <= calificacion <= 19:
    letra = "A"
elif 20 <= calificacion <= 39:
    letra = "B"
elif 40 <= calificacion <= 59:
    letra = "C"
elif 60 <= calificacion <= 79:
    letra = "D"
elif 80 <= calificacion <= 100:
    letra = "F"
else:
    letra = "Calificación fuera de rango"

# Mostrar la calificación alfabética
print("La calificación alfabética correspondiente es:", letra)
