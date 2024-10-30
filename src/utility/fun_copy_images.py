#Import libraries
import os
import cv2


def copy_images(folder_1, folder_2):
    '''
    Copia todas las imágenes desde folder_1 a folder_2
    '''

    #Create folder if not exists
    if not os.path.exists(folder_2):
        os.makedirs(folder_2)

    #Copy images
    files = os.listdir(folder_1)
    for file in files:
        if file.endswith(".jpg"):
            file_path = os.path.join(folder_1, file)
            img = cv2.imread(file_path)
            cv2.imwrite(os.path.join(folder_2, file), img)

    return