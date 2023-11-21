import math

# Función para calcular la distancia euclidiana entre dos puntos
def euclidean_distance(point1, point2):
    return math.sqrt((point2[0] - point1[0])**2 + (point2[1] - point1[1])**2)

# Datos de los clientes y el depósito
deposito = (82, 76, 0)
clientes = [
    (5, 10, 14),
    (98, 52, 21),
    (84, 25, 16),
    (61, 59, 3),
    (1, 65, 22),
    (88, 51, 18),
    (91, 2, 19),
    (19, 32, 1),
    (93, 3, 24),
    (50, 93, 8)
]

# Calcular las distancias entre el depósito y los clientes
distancias_depo = [euclidean_distance(deposito, cliente) for cliente in clientes]

# Calcular los ahorros para cada par de clientes
ahorros = {}
for i in range(len(clientes)):
    for j in range(len(clientes)):
        if i != j:
            ahorro = distancias_depo[i] + distancias_depo[j] - euclidean_distance(clientes[i], clientes[j])
            ahorros[(i, j)] = ahorro

# Ordenar los ahorros de mayor a menor
ahorros_ordenados = sorted(ahorros.items(), key=lambda x: x[1], reverse=True)

# Generar un reporte de las distancias de los ahorros
print("Pares de clientes y sus ahorros:")
for par, ahorro in ahorros_ordenados:
    print(f"Pareja: {par}, Ahorro: {ahorro:.2f}")
