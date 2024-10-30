
from PIL import Image

def crop(file, change_name, coordenadas = (504, 0, 1008, 495)):
    '''
    Herramienta para recortar imágenes
    change_name hace referencia a si añadir _temp al nombre del archivo
    coordenadas: (left, top, right, bottom)
    '''

    if type(file) == list:
        #Aplico iterativamente scissors
        temp_files = []
        for f in file:
            temp_files.append(crop(f, change_name, coordenadas))

        return temp_files
    else: 
        # Cargar la imagen
        imagen = Image.open(file)

        # Recortar la imagen
        imagen_recortada = imagen.crop(coordenadas)

        # Guardar la imagen recortada
        if change_name == True:
            # Extraer el nombre del archivo
            nombre_archivo = file.split('/')[-1]

            # Extraer la extensión del archivo
            extension = nombre_archivo.split('.')[-1]

            # Crear un nuevo nombre para el archivo
            nuevo_nombre = nombre_archivo.split('.')[0] + '_temp.' + extension

            # Guardar la imagen recortada con el nuevo nombre
            imagen_recortada.save(nuevo_nombre)

        else:
            imagen_recortada.save(file)


    return nuevo_nombre