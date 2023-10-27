import numpy as np
import random
# np.random.randint(54.0, 55.9, 16)
# np.random.rand(1, 50, 10)

rows = 4
colums = 4

# matriz_aleatoria = np.random.rand(rows, colums)
matriz_aleatoria = []

# matriz_aleatoria = random.random()
# matriz_aleatoria = np.random.uniform()

pilotos = ["Piloto1", "Piloto2", "Piloto3", "Piloto4"]
# tiempos = [
#     [55.2, 54.8, 55.0, 55.3],
#     [54.7, 54.9, 55.2, 54.6],
#     [55.5, 55.3, 54.0, 55.2],
#     [54.6, 54.7, 54.8, 54.9] ]

# Calcular el promedio de tiempos para cada piloto y guardarlos en un vector


# Generar valores decimales aleatorios y llenar la matriz
for i in range(rows):
    fila = []
    for j in range(colums):
        # Generar un valor decimal aleatorio entre un rango específico
        valor_decimal = round(random.uniform(0, 1), 2)  # En este ejemplo, se redondea a 2 decimales
        fila.append(valor_decimal)
    matriz_aleatoria.append(fila)
    
#Imprime la matriz
for fila in matriz_aleatoria:
    print(fila)

promedioT = [sum(matriz_aleatoria) / len(matriz_aleatoria) for matriz_aleatoria in matriz_aleatoria]

# Función para consultar los tiempos de cada piloto por cada vuelta
def consultar_tiempos_vuelta(piloto_index):
    piloto = pilotos[piloto_index]
    tiempos_piloto = matriz_aleatoria[piloto_index]
    for vuelta, tiempo in enumerate(tiempos_piloto, 1):
        print(f"{piloto} - Vuelta {vuelta}: {tiempo} segundos")

# Función para mostrar el piloto más rápido en una vuelta específica
def piloto_mas_rapido_en_vuelta(vuelta):
    tiempos_vuelta = [matriz_aleatoria[vuelta - 1] for i in range(rows)]
    piloto_index = tiempos_vuelta.index(min(tiempos_vuelta))
    return pilotos[piloto_index]

# Función para consultar quién tuvo el menor tiempo en todas las vueltas
def piloto_con_menor_tiempo_total():
    piloto_index = promedioT.index(max(promedioT))
    return pilotos[piloto_index]

# Ejemplos de uso  VUELTAS POR PILOTO
consultar_tiempos_vuelta(3)  # Consultar los tiempos del primer piloto en cada vuelta

vuelta_mas_rapida = 3 # CONSULTAR LA VUELTA DESEADA

piloto = piloto_mas_rapido_en_vuelta(vuelta_mas_rapida)
print(f"El piloto más rápido en la vuelta {vuelta_mas_rapida} es: {piloto}")
piloto_menor_tiempo_total = piloto_con_menor_tiempo_total()
print(f"El piloto con el menor tiempo total en todas las vueltas es: {piloto_menor_tiempo_total}")
