# Importaciones
import pandas as pd
import numpy as np
import re

# Cargar el CSV si aún no lo hiciste
df = pd.read_csv("Airbnb_Open_Data.csv",low_memory=False)

# Miramos los nombres de columnas
df.columns

# Cambiamos los nombres. Guion bajo donde haya espacio y todo minúsculas.
df.columns = ['id', 'name', 'host_id', 'host_identity_verified', 'host_name',
       'neighbourhood_group', 'neighbourhood', 'lat', 'long', 'country',
       'country code', 'instant_bookable', 'cancellation_policy', 'room_type',
       'construction_year', 'price', 'service_fee', 'minimum_nights',
       'number_of_reviews', 'last_review', 'reviews_per_month',
       'review_rate_number', 'calculated_host_listings_count',
       'availability_365', 'house_rules', 'license']
# Se puede hacer a mano como arriba o con ordenes
df.columns.str.lower()
df.columns.str.replace(" ","_")

# Rellenar valores nulos de 'reviews per month' con 0
df["reviews_per_month"] = df["reviews_per_month"].fillna(0)

# Eliminar valores duplicados
df = df.drop_duplicates()

# 

















