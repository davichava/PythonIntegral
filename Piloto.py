import random

pilotos = ["Piloto1", "Piloto2", "Piloto3", "Piloto4"]
tiempos = [
    [55.2, 54.8, 55.0, 55.3],
    [54.7, 54.9, 55.2, 54.6],
    [55.5, 55.3, 54.0, 55.2],
    [54.6, 54.7, 54.8, 54.9]
]

# Calcular el promedio de tiempos para cada piloto y guardarlos en un vector
promedios = [sum(tiempo) / len(tiempo) for tiempo in tiempos]

# Función para consultar los tiempos de cada piloto por cada vuelta
def consultar_tiempos_vuelta(piloto_index):
    piloto = pilotos[piloto_index]
    tiempos_piloto = tiempos[piloto_index]
    for vuelta, tiempo in enumerate(tiempos_piloto, 1):
        print(f"{piloto} - Vuelta {vuelta}: {tiempo} segundos")

# Función para mostrar el piloto más rápido en una vuelta específica
def piloto_mas_rapido_en_vuelta(vuelta):
    tiempos_vuelta = [tiempo[vuelta - 1] for tiempo in tiempos]
    piloto_index = tiempos_vuelta.index(min(tiempos_vuelta))
    return pilotos[piloto_index]

# Función para consultar quién tuvo el menor tiempo en todas las vueltas
def piloto_con_menor_tiempo_total():
    piloto_index = promedios.index(max(promedios))
    return pilotos[piloto_index]

# Ejemplos de uso
consultar_tiempos_vuelta(3)  # Consultar los tiempos del primer piloto en cada vuelta
vuelta_mas_rapida = 1
piloto = piloto_mas_rapido_en_vuelta(vuelta_mas_rapida)
print(f"El piloto más rápido en la vuelta {vuelta_mas_rapida} es: {piloto}")
piloto_menor_tiempo_total = piloto_con_menor_tiempo_total()
print(f"El piloto con el menor tiempo total en todas las vueltas es: {piloto_menor_tiempo_total}")
