import pandas as pd
from datetime import datetime
# Reemplaza 'nombre_archivo.csv' con el nombre real de tu archivo CSV
df = pd.read_csv('mantenimiento_modificado.csv')
date_columns = ['Fecha de Fallo 1', 'Fecha de Fallo 2', 'Fecha de Fallo 3', 'Fecha de Fallo 4', 'Fecha de Fallo 5']

for column in date_columns:
    df[column] = pd.to_datetime(df[column], format='%Y-%m-%d')
df['Fecha de Mantenimiento'] = df[date_columns].min(axis=1)
# Reemplaza 'resultado.csv' con el nombre deseado para el nuevo archivo CSV
df.to_csv('resultado.csv', index=False)
