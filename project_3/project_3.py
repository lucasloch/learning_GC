import matplotlib.pyplot as plt
import numpy as np

plt.figure(figsize=(8, 6))
plt.title('Transformações Geométricas em Coordenadas Homogêneas')
plt.xlabel('X')
plt.ylabel('Y')

casa = np.matrix([
    [4, 3, 1], 
    [0, 3, 1], 
    [1, 4, 1], 
    [3, 4, 1], 
    [4, 3, 1], 
    [4, 0, 1], 
    [0, 0, 1], 
    [0, 3, 1]
])

# Translação
matriz_translacao = np.matrix([
    [1, 0, 0], 
    [0, 1, 0], 
    [6, 6, 1]
])
casa_transladada = casa * matriz_translacao
plt.plot(casa_transladada[:,0], casa_transladada[:,1], color='red', label='Translação')

# Escala
matriz_escala = np.matrix([
    [4, 0, 0], 
    [0, 4, 0], 
    [0, 0, 1]
])
casa_escalonada = casa * matriz_escala
plt.plot(casa_escalonada[:,0], casa_escalonada[:,1], color='orange', label='Escala')

# Reflexão em relação ao eixo X
matriz_reflexao = np.matrix([
    [1, 0, 0], 
    [0, -1, 0], 
    [0, 0, 1]
])
casa_refletida = casa * matriz_reflexao
plt.plot(casa_refletida[:,0], casa_refletida[:,1], color='purple', label='Reflexão')

# Rotação
matriz_rotacao = np.matrix([
    [np.cos(1), np.sin(1), 0], 
    [-np.sin(1), np.cos(1), 0], 
    [0, 0, 1]
])
casa_rotacionada = casa * matriz_rotacao
plt.plot(casa_rotacionada[:,0], casa_rotacionada[:,1], color='green', label='Rotação')

# Cisalhamento
matriz_cisalhamento = np.matrix([
    [1, 0, 0], 
    [1, 1, 0], 
    [0, 0, 1]
])
casa_cisalhada = casa * matriz_cisalhamento
plt.plot(casa_cisalhada[:,0], casa_cisalhada[:,1], color='black', label='Cisalhamento')

# Normal
plt.plot(casa[:,0], casa[:,1], color='blue', label='Normal')
plt.legend()
plt.show()