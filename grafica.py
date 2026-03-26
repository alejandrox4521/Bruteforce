import matplotlib.pyplot as plt

alfabeto = 26

longitudes = []
combinaciones = []

for n in range(1, 9):
    longitudes.append(n)
    combinaciones.append(alfabeto ** n)

plt.plot(longitudes, combinaciones, marker='o')

plt.title("Crecimiento Exponencial en Fuerza Bruta")
plt.xlabel("Longitud de la contraseña")
plt.ylabel("Número de combinaciones")

plt.grid()

plt.show()