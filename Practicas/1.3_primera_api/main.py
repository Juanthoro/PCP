import pandas as pd
from fastapi import FastAPI, Query
from typing import Optional# Necesario para poder meter de manera opcional los parámetros

# Cuidado al colocar el csv que la ubicación importa
df = pd.read_csv("datos_alumnos.csv")
app = FastAPI(title="iesazarquiel")


# Primer endpoint
@app.get("/info-alumnos")
def info():
    return {df["ID"].tolist()}


# Segundo endpoint
@app.get("/asistencia")
def asistencia(id: Optional[int] = Query(None)):
# En los parámetros opcionales se podría hacer directamente id = None sin tener que importar la libreria Optional
    if (id is None):
        return "El parámetro adicional es id"

    alumno = df[df["ID"] == id]
    row = alumno.iloc[0]
    return {
        row["Nombre"] + " " + row["Apellidos"] + ": " + "Asistencia": row["Asistencia"]
    }


# Tercer endpoint
@app.get("/notas")
def notas(id: Optional[int] = Query(None), nota: Optional[str] = Query(None)):

    if (id is None) or (nota is None):
        return "Los parámetros opcionales son id y nota"

    alumno = df[df["ID"] == id]
    row = alumno.iloc[0]
    return {
        "Nombre": row["Nombre"] + row["Apellidos"] + ": " + row[nota]
    }



