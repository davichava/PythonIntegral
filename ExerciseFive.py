import queue

class User:
    def __init__(self, name, priority, cpu_time):
        self.name = name
        self.priority = priority
        self.cpu_time = cpu_time

# Simula la cola de procesos listos
ready_queue = queue.Queue()

# Agrega usuarios con diferentes prioridades y tiempos de CPU a la cola
users = [
    User("UserA", 1, 5),
    User("UserB", 2, 3),
    User("UserC", 1, 2),
    User("UserD", 3, 4),
]

for user in users:
    ready_queue.put(user)

# Simula la asignación de tiempo de CPU en un ciclo de planificación de rondas
total_time = 0
while not ready_queue.empty():
    user = ready_queue.get()
    print(f"Ejecutando {user.name} (Prioridad: {user.priority}, Tiempo de CPU restante: {user.cpu_time})")
    
    # Simula la ejecución de una unidad de tiempo de CPU para el usuario
    user.cpu_time -= 1
    total_time += 1
    
    if user.cpu_time > 0:
        ready_queue.put(user)  # Vuelve a agregar el usuario a la cola si tiene tiempo de CPU restante

print(f"Tiempo total de ejecución: {total_time}")