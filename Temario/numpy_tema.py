### NUMPY ###
## Para instalar pip install numpy
## Para instalar pip install matplotlib
import numpy as np
import pandas as pd
import matplotlib as plt


print (np.__version__)# son dos guiones bajos

a = np.array([1,2,3,4,5])
print(a)

b = np.array([[1,2,3],[4,5,6]])
print(b)# los saca como una matriz, unos debajo de otros

c = np.zeros(5)# el número es el tamaño
print(c)# array de 0

d = np.ones(3)
print(d)# array de 1

e = np.zeros([5,5])
print(e)# array de 5 x 5 de 0

f = np.arange(0,10,2)# comienzo,final,cuanto avanza cada salto
print(f)

g = np.linspace(0,2,5)# comienzo,final,cuantas elementos equidistamntes entre los dos valores
print(g)

h = np.eye(4)# matriz identidad de ese tamaño
print(h)

i = np.random.rand(4)# array de números aleatorios
print(i)

# Operaciones matemáticas

print(a+c)# deben ser del mismo módulo

print(h*7)

### PANDAS ###
## Basada en NUMPY ###
## Para instalas pip install pandas
# import pandas as pd

serie1 = pd.Series([1,2,3])
print(serie1)# Lo imprime con el indice del array a la izquierda

df1 = pd.DataFrame({"columna1":[1,2,3,4,5], "columna2":[a,b,c,d,e], "columna3":[1,2,3,4,5],})
print(df1)

# Importar con un fichero csv
df2 = pd.read_csv("https://gist.githubusercontent.com/curran/a08a1080b88344b0c8a7/raw/0e7a9b0a5d22642a06d3d5b9bcbad9890c8ee534/iris.csv")
print(df2.head())# head() nos muestra las 5 primeras lineas por defecto. Si ponemos en el parentasis un numero sacara eso

# Principales funciones
print(df2.size)# Los elementos de df1
print(df2.shape)# Cuantas filas y columnas
print(df2.head(2))# Por defecto nos saca 5 lineas
print(df2.tail())# Igual que head pero del final
print(df2.describe())# nos da estadísticas básicas como media etc
print(df2["species"].value_counts())# nos hace la suma de los mismos valores
print(df2.dtypes)# tipos de cada columna
print(df2.memory_usage().sum())# Memoria total
print(df2.T)# Transpone las filas por columnas
print(df2.sort_values("species", ascending=False))# va con las columna que quieras
print(df2.species)# nos da esa columna en concreto
print(df2.iloc([1,4],[1,2]))# se pueden especificar filas y columnas concretas
print(df1[df1["columna1"]>2])# se puede filtrar por condicion y columna
print(df2.isna().sum())# saca el sumatorio de NaN (Not a Number)
print(df2.mean())
print(df2.median())




