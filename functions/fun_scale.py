#Import libraries
import cv2


def scale(file, new_dim):
    '''
    Escalea la imagen file para que tenga las dimensiones new_dim en pixeles
    '''
    if type(file) == list:
        #Aplico iterativamente scale
        files = []
        for f in file:
            files.append(scale(f, new_dim))

        return files
    else:
        #Cargo imagen
        img = cv2.imread(file)
        img = cv2.resize(img, new_dim)
        #Sobreescribo
        cv2.imwrite(file, img)

        return file
    
