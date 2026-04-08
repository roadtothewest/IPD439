import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

n_values = [50000, 100000, 150000, 200000, 250000, 300000, 500000]

df_mean = pd.DataFrame(index=n_values)
df_std = pd.DataFrame(index=n_values)

for n in n_values:
    filename = f"{n}.csv"
    try:
        df = pd.read_csv(filename)
    except FileNotFoundError:
        print(f"Advertencia: No se encontró {filename}, omitiendo...")
        continue

    t_col = df.columns[0]
    
    for canal in df.columns[1:]:
        tiempos = df[(df[canal] == 1) & (df[canal].shift(1) == 0)][t_col].values
        periodos = np.diff(tiempos) * 1000
        
        if len(periodos) > 0:
            df_mean.loc[n, canal] = np.mean(periodos)
            df_std.loc[n, canal] = np.std(periodos)

nombres = ['Tarea 1 (100ms)', 'Tarea 2 (200ms)', 'Tarea 3 (Carga)']
if len(df_mean.columns) == len(nombres):
    df_mean.columns = nombres
    df_std.columns = nombres

# Gráfico Tendencia
df_mean.plot.bar(figsize=(10, 6), rot=0, colormap='tab10', title='Tendencia vs Carga Computacional')
plt.xlabel('Carga Computacional (n)')
plt.ylabel('Periodo Promedio (ms)')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.savefig('tendencia_carga.png', dpi=300)

# Gráfico Varianza
df_std.plot.bar(figsize=(10, 6), rot=0, colormap='tab10', title='Variabilidad vs Carga Computacional')
plt.xlabel('Carga Computacional (n)')
plt.ylabel('Desviación Estándar / Jitter (ms)')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.savefig('varianza_carga.png', dpi=300)

plt.show()
