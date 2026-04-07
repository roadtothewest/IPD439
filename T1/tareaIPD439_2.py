import matplotlib.pyplot as plt
import numpy as np

valores = []
with open("DMA10Hz.txt", "r") as f:
    for linea in f:
        linea = linea.strip()
        if "Transmitiendo" in linea or "Transmision" in linea:
            continue
        if linea:
            valores.append(float(linea))

tiempo = np.linspace(0, 2.0, len(valores), endpoint=False)

plt.figure(figsize=(10, 5))
plt.plot(tiempo, valores, marker='o', markersize=4, linestyle='-', color='b')
plt.title('Señal Capturada por el ADC (Modo DMA) - 10 Hz')
plt.xlabel('Tiempo [s]')
plt.ylabel('Voltaje [V]')
plt.grid(True)
plt.ylim(-0.2, 3.3)
plt.show()
