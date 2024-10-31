#Import libraries
import cv2

def gray_scale(file):
    '''
    Convierte la/s imagen/es cuya dirección es file en escala de grises. Luego, sobreescribe la imagen.
    '''

    #If file es una lista
    if type(file) == list:

        #Aplico iterativamente gray_scale
        files = []
        for f in file:
            files.append(gray_scale(f))
            
        return files
    
    else:

        #Cargo imagen de ejemplo
        img = cv2.imread(file, cv2.IMREAD_GRAYSCALE)

        # #From file extract the folder
        # folder = file.split("/")
        # folder = folder[:-1]
        # #Change last folder to preprocessed
        # folder[-1] = "preprocessed"
        # file = "/".join(folder) + "/" + file.split("/")[-1]
        # #Create temp_file as folder/name_temp.extension
        # #From file extract the name without extension
        # name = file.split("/")[-1].split(".")[0]
        # #From file extract extension
        # extension = file.split("/")[-1].split(".")[1]
        # temp_file = "/".join(folder) + "/" + name + "_temp." + extension

        cv2.imwrite(file, img)

        return file