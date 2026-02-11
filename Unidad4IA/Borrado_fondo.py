# pip install rembg
# pip install "rembg[cpu]"
# pip install onnxruntime
# pip install pillow
# pip install aspose-words

from rembg import remove
import aspose.words as aw

#####################################################################################################
# Función que elimina el fondo
def eliminar_fondo(path_entrada: str, path_salida: str) -> None:

    # Abrimos la imagen original en modo binario ("rb read binary") porque rembg trabaja con bytes
    with open(path_entrada, "rb") as i:
        input_image = i.read()

    # Aplicamos la IA para eliminar el fondo
    output_image = remove(input_image)

    # Guardamos la imagen resultante (usamos "wb write binary" porque es binario)
    with open(path_salida, "wb") as o:
        o.write(output_image)

    print("✅ Fondo eliminado correctamente")
#####################################################################################################

#####################################################################################################
# Función que convierte de png a svg
def convertir_png_a_svg(path_entrada: str, path_salida: str) -> None:

    # Creamos un documento vacío de Aspose
    doc = aw.Document()

    # DocumentBuilder permite insertar elementos dentro del documento
    builder = aw.DocumentBuilder(doc)

    # Insertamos la imagen en el documento
    shape = builder.insert_image(path_entrada)

    # Obtenemos el renderizador de la imagen y la guardamos como SVG
    shape.get_shape_renderer().save(path_salida,aw.saving.ImageSaveOptions(aw.SaveFormat.SVG))

    print("✅ Imagen convertida a SVG correctamente")
#####################################################################################################

# Rutas de las fotos (deben llevar r delante siempre)
path_in = r"C:\Users\vespertino\Documents\VS2DAW2025\PCP\Unidad4IA\img\camarero.png"
path_out = r"C:\Users\vespertino\Documents\VS2DAW2025\PCP\Unidad4IA\img\camarero_sin_fondo.png"
path_out2 = r"C:\Users\vespertino\Documents\VS2DAW2025\PCP\Unidad4IA\img\camarero_convertido.svg"
path_out3 = r"C:\Users\vespertino\Documents\VS2DAW2025\PCP\Unidad4IA\img\camarero_sin_fondo_convertido.svg"

# Llamamos a las funciones y ejecutamos la terminal
eliminar_fondo(path_in, path_out)
convertir_png_a_svg(path_out, path_out2)
convertir_png_a_svg(path_out, path_out3)
    


