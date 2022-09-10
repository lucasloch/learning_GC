import matplotlib.pyplot as plt
import numpy as np

casa_x = np.array([4, 0, 1, 3, 4, 4, 0, 0])
casa_y = np.array([3, 3, 4, 4, 3, 0, 0, 3])

plt.figure(figsize=(8, 6))
plt.title('Transformações Geométricas')
plt.xlabel('X')
plt.ylabel('Y')
plt.plot(casa_x+6, casa_y+6, color='red', label='Translação (+6)')
plt.plot(casa_x*4, casa_y*4, color='orange', label='Escala (*4)')
plt.plot((casa_x*np.cos(1) - casa_y*np.sin(1)), (casa_y*np.cos(1) + casa_x*np.sin(1)), color='green', label='Rotação (cos(1) e sin(1))')
plt.plot(casa_x, casa_y*-1, color='purple', label='Reflexão (em relação ao eixo X)')
plt.plot(casa_x+1*casa_y, casa_y+0*casa_x, color='black', label='Cisalhamento (em X)')
plt.plot(casa_x, casa_y, color='blue', label='Normal')
plt.legend()
plt.show()