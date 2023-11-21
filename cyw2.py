import numpy as np

# Matriz de distancias entre los nodos
distances = np.array([
    [0, 9, 14, 23, 32, 50, 21, 49, 30, 27, 35, 28, 18],
    [9, 0, 21, 22, 36, 52, 24, 51, 36, 37, 41, 30, 20],
    [14, 21, 0, 25, 38, 5, 31, 7, 36, 43, 29, 7, 6],
    [23, 22, 25, 0, 42, 12, 35, 17, 44, 31, 31, 11, 6],
    [32, 36, 38, 42, 0, 22, 37, 16, 46, 37, 29, 13, 14],
    [50, 52, 5, 12, 22, 0, 41, 23, 10, 39, 9, 17, 16],
    [21, 24, 31, 35, 37, 41, 0, 26, 21, 19, 10, 25, 12],
    [49, 51, 7, 17, 16, 23, 26, 0, 30, 28, 16, 27, 12],
    [30, 36, 36, 44, 46, 10, 21, 30, 0, 25, 22, 10, 20],
    [27, 37, 43, 31, 37, 39, 19, 28, 25, 0, 20, 16, 8],
    [35, 41, 29, 31, 29, 9, 10, 16, 22, 20, 0, 10, 10],
    [28, 30, 7, 11, 13, 17, 25, 27, 10, 16, 10, 0, 10],
    [18, 20, 6, 6, 14, 16, 12, 12, 20, 8, 10, 10, 0]
])

# Demandas de los nodos
demandas = [0, 1200, 1700, 1500, 1400, 3000, 1400, 1200, 1900, 1800, 4000, 1700, 1100]

# Calcular los ahorros para cada par de clientes
ahorros = {}
for i in range(1, distances.shape[0]):
    for j in range(1, distances.shape[0]):
        if i != j:
            ahorro = distances[0][i] + distances[0][j] - distances[i][j]
            ahorros[(i, j)] = ahorro

# Ordenar los ahorros de mayor a menor
ahorros_ordenados = sorted(ahorros.items(), key=lambda x: x[1], reverse=True)

# Imprimir los ahorros
print("Ahorros ordenados de mayor a menor:")
for par, ahorro in ahorros_ordenados:
    print(f"Pareja: {par}, Ahorro: {ahorro}")