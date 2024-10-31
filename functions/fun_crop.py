
from PIL import Image

def crop(file, coordenadas = (504, 0, 1008, 495)):
    '''
    Herramienta para recortar imágenes
    coordenadas: (left, top, right, bottom)
    '''

    if type(file) == list:
        #Aplico iterativamente scissors
        files = []
        for f in file:
            files.append(crop(f, coordenadas))

        return files
    else: 
        # Cargar la imagen
        imagen = Image.open(file)

        # Recortar la imagen
        imagen_recortada = imagen.crop(coordenadas)

        # Guardar la imagen recortada
        imagen_recortada.save(file)


    return file