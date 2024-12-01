from PIL import Image
import os
import numpy as np
import cv2


def getImagesAndLabels(path):
    """
    récupère les image et donne des labels
    """

    detector = cv2.CascadeClassifier("programs\\utils\\haarcascade_frontalface_default.xml");
    imagePaths = [os.path.join(path,f) for f in os.listdir(path)]

    if not imagePaths:
        print(" [INFO] No image to train on")
        quit()
    
    
    faceSamples=[]
    ids = []

    for imagePath in imagePaths:

        PIL_img = Image.open(imagePath).convert('L')
        img_numpy = np.array(PIL_img,'uint8')

        id = int(os.path.split(imagePath)[-1].split(".")[1])
        faces = detector.detectMultiScale(img_numpy)

        for (x,y,w,h) in faces:
            faceSamples.append(img_numpy[y:y+h,x:x+w])
            ids.append(id)

    return faceSamples,ids