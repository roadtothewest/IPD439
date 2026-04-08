import pandas as pd
import numpy as np

df = pd.read_csv('digital.csv')
col_tiempo = df.columns[0]

for canal in df.columns[1:]:
    #Tiempos los cantos de subida
    tiempos = df[(df[canal] == 1) & (df[canal].shift(1) == 0)][col_tiempo].values
    periodos = np.diff(tiempos) * 1000
    
    if len(periodos) > 0:
        promedio = np.mean(periodos)
        desviacion = np.std(periodos)
        print(f"{canal} -> Promedio: {promedio:.4f} ms | Desviación Est.: {desviacion:.6f} ms")
