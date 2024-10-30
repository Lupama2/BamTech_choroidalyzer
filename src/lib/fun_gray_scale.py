#Import libraries
import cv2

def gray_scale(file, change_name = True):
    '''
    Convertir imagen a escala de grises
    change_name hace referencia a si añadir _temp al nombre del archivo
    '''

    #If file es una lista
    if type(file) == list:

        #Aplico iterativamente gray_scale
        temp_files = []
        for f in file:
            temp_files.append(gray_scale(f, change_name))
            
        return temp_files
    
    else:

        #Cargo imagen de ejemplo
        img = cv2.imread(file, cv2.IMREAD_GRAYSCALE)

        #From file extract the folder
        folder = file.split("/")
        folder = folder[:-1]

        #Change last folder to preprocessed
        folder[-1] = "preprocessed"

        file = "/".join(folder) + "/" + file.split("/")[-1]

        #Create temp_file as folder/name_temp.extension
        if change_name:

            #From file extract the name without extension
            name = file.split("/")[-1].split(".")[0]

            #From file extract extension
            extension = file.split("/")[-1].split(".")[1]

            temp_file = "/".join(folder) + "/" + name + "_temp." + extension
        else:
            temp_file = file

        cv2.imwrite(temp_file, img)

        return temp_file