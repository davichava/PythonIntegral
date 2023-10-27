import numpy as np
import random

rows = 4
columns = 4

matriz_aleatoria = []
pilotos = ["Piloto1", "Piloto2", "Piloto3", "Piloto4"]

for i in range(rows):
    fila = []
    for j in range(columns):
        valor_decimal = round(random.uniform(0, 1), 2)
        fila.append(valor_decimal)
    matriz_aleatoria.append(fila)

for fila in matriz_aleatoria:
    print(fila)

# Calculate average lap time for each pilot
promedioT = [sum(matriz_aleatoria[i]) / len(matriz_aleatoria[i]) for i in range(rows)]

# Function to consult the lap times for each pilot for a specific lap
def consultar_tiempos_vuelta(piloto_index):
    piloto = pilotos[piloto_index]
    tiempos_piloto = matriz_aleatoria[piloto_index]
    for vuelta, tiempo in enumerate(tiempos_piloto, 1):
        print(f"{piloto} - Vuelta {vuelta}: {tiempo} segundos")

# Function to find the fastest pilot in a specific lap
def piloto_mas_rapido_en_vuelta(vuelta):
    tiempos_vuelta = [matriz_aleatoria[i][vuelta - 1] for i in range(rows)]
    piloto_index = tiempos_vuelta.index(min(tiempos_vuelta))
    return pilotos[piloto_index]

# Function to find the pilot with the lowest total time
def piloto_con_menor_tiempo_total():
    piloto_index = promedioT.index(min(promedioT))
    return pilotos[piloto_index]

# Examples of usage
consultar_tiempos_vuelta(1)

vuelta_mas_rapida = 1  # Specify the desired lap
piloto = piloto_mas_rapido_en_vuelta(vuelta_mas_rapida)
print(f"El piloto más rápido en la vuelta {vuelta_mas_rapida} es: {piloto}")

piloto_menor_tiempo_total = piloto_con_menor_tiempo_total()
print(f"El piloto con el menor tiempo total en todas las vueltas es: {piloto_menor_tiempo_total}")