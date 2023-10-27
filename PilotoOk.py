import random
import numpy as np

# Función para generar tiempos aleatorios para las vueltas de los pilotos
def generar_tiempos_aleatorios(num_pilotos, num_vueltas):
    ClasificacionPole = np.random.uniform(60, 120, size=(num_pilotos, num_vueltas))
    return ClasificacionPole

# Función para calcular los promedios de los tiempos de cada piloto
def calcular_promedios(ClasificacionPole):
    PromedioT = np.mean(ClasificacionPole, axis=1)
    return PromedioT

# Función para mostrar los tiempos de cada piloto por vuelta
def mostrar_tiempos_por_piloto(ClasificacionPole):
    num_pilotos, num_vueltas = ClasificacionPole.shape
    for i in range(num_pilotos):
        nombre = f"Piloto {i + 1}"
        tiempos = ClasificacionPole[i]
        print(f"{nombre}: {tiempos}")

# Función para encontrar el piloto más rápido en una vuelta específica
def piloto_mas_rapido_en_vuelta(ClasificacionPole, vuelta):
    tiempos_vuelta = ClasificacionPole[:, vuelta - 1]
    piloto_mas_rapido = np.argmin(tiempos_vuelta)
    return piloto_mas_rapido

# Función para mostrar el piloto con el menor tiempo promedio
def mostrar_piloto_con_menor_promedio(PromedioT):
    piloto_menor_promedio = np.argmin(PromedioT)
    return piloto_menor_promedio

# Función para mostrar el promedio de todos los pilotos
def mostrar_promedio_general(PromedioT):
    promedio_general = np.mean(PromedioT)
    print(f"El promedio de todos los pilotos es: {promedio_general:.2f}")

# Menú de opciones
def menu():
    num_pilotos = int(input("Ingrese el número de pilotos: "))
    num_vueltas = 4

    ClasificacionPole = generar_tiempos_aleatorios(num_pilotos, num_vueltas)
    PromedioT = calcular_promedios(ClasificacionPole)

    while True:
        print("\nMenú de opciones:")
        print("1. Mostrar tiempos por piloto")
        print("2. Encontrar el piloto más rápido en una vuelta")
        print("3. Mostrar el piloto con el menor tiempo promedio")
        print("4. Mostrar el promedio de todos los pilotos")
        print("5. Mostrar quien quedó en el primer lugar")
        print("6. Salir")

        opcion = int(input("Seleccione una opción: "))

        if opcion == 1:
            mostrar_tiempos_por_piloto(ClasificacionPole)
        elif opcion == 2:
            vuelta = int(input("Ingrese el número de vuelta: "))
            piloto_mas_rapido = piloto_mas_rapido_en_vuelta(ClasificacionPole, vuelta)
            print(f"El piloto más rápido en la vuelta {vuelta} es el Piloto {piloto_mas_rapido + 1}")
        elif opcion == 3:
            piloto_menor_promedio = mostrar_piloto_con_menor_promedio(PromedioT)
            print(f"El piloto con el menor tiempo promedio es el Piloto {piloto_menor_promedio + 1}")
        elif opcion == 4:
            mostrar_promedio_general(PromedioT)
        elif opcion == 5:
            piloto_pole = mostrar_piloto_con_menor_promedio(PromedioT)
            print(f"El piloto que logra la Pole Position es el Piloto {piloto_pole + 1}")
        elif opcion == 6:
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

if __name__ == "__main__":
    menu()