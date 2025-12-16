from fastapi import FastAPI
from pydantic import BaseModel, Field, EmailStr
from fastapi.responses import JSONRESPONSE

app = FastAPI()
inventario = []

class Item(BaseModel):
    name: str = Field(examples=["Foo"])
    description: str | None = Field(default=None, examples=["A very nice Item"])
    price: float = Field(examples=[35.4])
    tax: float | None = Field(default=None, examples=[3.2])


@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    results = {"item_id": item_id, "item": item}
    return results

# Mostrar las categorías de los libros
@app.get("/categoria/{cat}")
def articulos_por_categoria(cat:str="General"):
    por_categoria = [libro for libro in inventario if libro["category"] == cat]
    if por_categoria: return {f"Libros sobre {cat}"}


# CREA UN ARTICULO NUEVO
@app.put("/libro")
def crear_libro(libro:Book):
    libro_nuevo = libro.model_dump()
    libro_nuevo["id"] = max(lib['id'] for lib in inventario) + 1 if inventario else 1 # Compresión en python
    inventario.append(libro_nuevo)
    return("Añadido el libro": libro_nuevo)

# Actualizar un articulo
@app.post("/almacen/{id_libro}")
def actualizar_libro(id_libro: int, libro: Item):
    for lib in inventario:
        if lib["id"]=id_libro:
            lib["name"]=libro.name
            lib["category"]=libro.category
            lib["price"]=libro.price
            lib["tax"]=libro.tax
            return {"Actualizado el libro": inventario[inventario.index(lib)]}

    return JSONRESPONSE(status_code=404, content={"update":False, "message":"Artículo no encontrado"})
