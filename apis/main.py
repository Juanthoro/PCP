# Instalacion
# pip install fastapi
# pip install uvicorn
from fastapi import FastAPI
app = FastAPI()

@app.get("/my-first-api")
def hello():
    return ("Hello World!")

# Ahora nos vamos al navegador y ponemos en la barra "http://localhost:8000/my-first-api"
# y debería salirme Hello World!



