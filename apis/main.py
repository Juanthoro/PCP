# Instalacion
# https://anderfernandez.com/blog/como-crear-api-en-python/
# y en la consola ponemos uvicorn main:app

# pip install fastapi
# pip install uvicorn
# pip install pandas
# pip install matplotlib
# pip install requests
from fastapi import FastAPI
from fastapi.responses import StreamingResponse
app = FastAPI()

# @app.get("/my-first-api")
# def hello():
#     return ("Hello World!")

# Ahora nos vamos al navegador y ponemos en la barra "http://localhost:8000/my-first-api"
# y debería salirme Hello World!

# @app.get("/my-first-api")
# def hello(name: str):
#   return {'Hello ' + name + '!'}

# IMPORTANTE: Hay que volver a poner uvicorn main:app en la consola para que cargue
# # Ahora nos vamos al navegador y ponemos en la barra "http://localhost:8000/my-first-api?name=Juan"
# y nos saldria Hello Juan!

@app.get("/my-first-api")
def hello(name = None):

    if name is None:
        text = 'Hello!'

    else:
        text = 'Hello ' + name + '!'

    return text

# IMPORTANTE: Hay que volver a poner uvicorn main:app en la consola para que cargue
# # Ahora nos vamos al navegador y ponemos en la barra "http://localhost:8000/my-first-api?name=Juan"
# y nos saldria Hello Juan! Si no pones el name solo te saldria Hello!

# Devolver diferentes tipos de datos con FastAPI

@app.get("/get-iris")
def get_iris():

    import pandas as pd
    url ='https://gist.githubusercontent.com/curran/a08a1080b88344b0c8a7/raw/0e7a9b0a5d22642a06d3d5b9bcbad9890c8ee534/iris.csv'
    iris = pd.read_csv(url)

    return iris

# IMPORTANTE: Hay que volver a poner uvicorn main:app en la consola para que cargue
# # Ahora nos vamos al navegador y ponemos en la barra "http://localhost:8000/get-iris"
# y nos saldria el dataframe ordenado

@app.get("/plot-iris")
def plot_iris():

    import pandas as pd
    import matplotlib.pyplot as plt

    url ='https://gist.githubusercontent.com/curran/a08a1080b88344b0c8a7/raw/0e7a9b0a5d22642a06d3d5b9bcbad9890c8ee534/iris.csv'
    iris = pd.read_csv(url)

    plt.scatter(iris['sepal_length'], iris['sepal_width'])
    plt.savefig('iris.png')
    file = open('iris.png', mode="rb")

    return StreamingResponse(file, media_type="image/png")

# IMPORTANTE: from fastapi.responses import StreamingResponse


# Comprobar el funcionamiento de una API de FastAPI
# uvicorn main:app --reload
# esta orden nos corre otra vez el uvicorn

# import requests
# from PIL import Image
# import io

# resp = requests.get('http://127.0.0.1:8000/plot-iris')
# file = io.BytesIO(resp.content)
# im = Image.open(file)
# im.show()

# resp = requests.get('http://127.0.0.1:8000/my-first-api?name=Ander')
# resp.text

# En el http cambiamos la dirección por localhost ya que lo usamos en nuestro equipo
# también cambiamos el name por Juan

# FastAPI nos crea la documentación en swagger.
# Se puede acceder a ella=> http://localhost:8000/docs
# Se puede acceder a ella=> http://localhost:8000/redoc
# las capturas de como se debe ver las adjunto en la carpeta img









