# Importaciones
import pandas as pd
import numpy as np
import re

# Cargar el CSV si aún no lo hiciste
df = pd.read_csv("personas_sucio.csv")

# Nombres: primera letra en mayúscula y el resto en minúscula
df["nombre"] = df["nombre"].str.title()

# Edades: convertir a numérico y reemplazar 0 o NaN por la media
df["edad"] = pd.to_numeric(df["edad"], errors="coerce")  # convierte texto raro en NaN
media_edad = df.loc[df["edad"] != 0, "edad"].mean()      # media sin los ceros
df["edad"] = df["edad"].replace(0, np.nan)               # cambia 0 por NaN
df["edad"].fillna(media_edad, inplace=True)               # reemplaza NaN por media
df["edad"] = df["edad"].astype(int)                       # convierte a int si quieres

# Ciudades: en mayúsculas
df["ciudad"] = df["ciudad"].replace({"Mad": "Madrid", "Sev": "Sevilla", "Sev.": "Sevilla", "MAD": "Madrid"})
df["ciudad"] = df["ciudad"].str.upper()

# Emails
def obtener_nombre_con_dominio(df, email_col='email', dominio='example.com'):
    df[email_col] = df['nombre'].astype(str).str.strip() + "@" + dominio
    return df

df = obtener_nombre_con_dominio(df)

# Fechas: formato DD/MM/AAAA
df["fecha_registro"] = pd.to_datetime(df["fecha_registro"], errors="coerce", dayfirst=True)
df["fecha_registro"] = df["fecha_registro"].dt.strftime("%d/%m/%Y")

# Guardar el resultado final
df.to_csv("personas_limpio.csv", index=False)
