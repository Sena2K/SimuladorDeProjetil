import numpy as np
import matplotlib.pyplot as plt

while True:
    try:
        V0 = int(input("Digite a velocidade do projetil:"))

        if V0 <= 0:
            raise ValueError

        Angulo = int(input("Digite o angulo de lançamento:"))

        if Angulo < 0 or Angulo > 90:
            raise ValueError

        break
    except ValueError:
        print("Por favor, digite um valor de acordo com as regras")

angRAd = np.deg2rad(Angulo)
g = 9.8

alcance_maximo = round(((V0**2) * np.sin(2*angRAd)) / g, 1)
altura_maxima = round((V0**2) * (np.sin(angRAd))**2 / (2*g), 1)
tempo_total = round((((2*V0) * np.sin(angRAd)) / g), 1)

t = np.linspace(0, tempo_total, num=100)

x_trajetoria = V0 * np.cos(angRAd) * t
y_trajetoria = V0 * np.sin(angRAd) * t - 0.5 * g * t**2

print("Alcance máximo:", alcance_maximo, "metros")
print("Altura máxima:", altura_maxima, "metros")
print("Tempo total de voo:", tempo_total, "segundos")

plt.title("Trajetoria")
plt.xlabel("Distancia")
plt.ylabel("Altura")
plt.plot(x_trajetoria, y_trajetoria)
plt.grid(True)
plt.show()
