import cv2
import numpy as np
from PIL import Image
import os

# chemin vers les photos
path = 'data'

recognizer = cv2.face.LBPHFaceRecognizer_create()
detector = cv2.CascadeClassifier("haarcascade_frontalface_default.xml");

# récupère les image et donne des labels
def getImagesAndLabels(path):

    imagePaths = [os.path.join(path,f) for f in os.listdir(path)]
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

print ("\n [INFO] Entrainement en cours...")
faces,ids = getImagesAndLabels(path)
recognizer.train(faces, np.array(ids))

# Sauve le modèle dans trainer/trainer.yml
recognizer.write('trainer/trainer.yml')
pipi
# Imprime le nombre de visages entrainés
print("\n [INFO] {0} visages entrainés.".format(len(np.unique(ids))))