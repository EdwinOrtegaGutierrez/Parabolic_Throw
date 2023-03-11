import math
import json

def function(v0, theta, g):
    # Convertir el ángulo a radianes
    theta = math.radians(theta)

    # Calcular componentes de la velocidad inicial
    v0x = v0 * math.cos(theta)
    v0y = v0 * math.sin(theta)

    # Calcular el tiempo de vuelo y el rango máximo
    tmax = 2 * v0y / g
    rmax = v0x * tmax

    # Crear una lista para almacenar los valores de x, y, v y t
    data = []

    # Calcular y almacenar la posición y la velocidad en cada instante de tiempo
    t = 0
    while t <= tmax:
        x = v0x * t
        y = v0y * t - 0.5 * g * t**2
        v = math.sqrt(v0x**2 + (v0y - g*t)**2)
        data.append({"t": t, "x": x, "y": y, "v": v})
        t += 0.1

    # Guardar los datos en un archivo JSON
    with open("static/json/pt.json", "w") as f:
        json.dump(data, f)
    print("Finish")
    return (tmax, rmax)