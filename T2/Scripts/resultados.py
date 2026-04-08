import pandas as pd
import numpy as np
import os

n_values = [50000, 100000, 150000, 200000, 250000, 300000, 500000]

print("--- RESULTADOS DE TENDENCIA Y VARIANZA ---")

for n in n_values:
    filename = f"{n}.csv"
    if not os.path.exists(filename):
        print(f"\n[{n}] Archivo {filename} no encontrado.")
        continue
        
    print(f"\nCarga n = {n}:")
    df = pd.read_csv(filename)
    col_tiempo = df.columns[0]
    
    for canal in df.columns[1:]:
        # Tiempos de los cantos de subida
        tiempos = df[(df[canal] == 1) & (df[canal].shift(1) == 0)][col_tiempo].values
        periodos = np.diff(tiempos) * 1000
        
        if len(periodos) > 0:
            promedio = np.mean(periodos)
            desviacion = np.std(periodos)
            print(f"  {canal} -> Media: {promedio:.4f} ms | Desv: {desviacion:.6f} ms")
        else:
            print(f"  {canal} -> Sin datos suficientes.")
