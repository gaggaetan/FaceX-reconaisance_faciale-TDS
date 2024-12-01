import cv2
import numpy as np
from utils.training_utils import *


# chemin vers les photos
path = 'data'

recognizer = cv2.face.LBPHFaceRecognizer_create()

print ("\n [INFO] Entrainement en cours...")
faces,ids = getImagesAndLabels(path)
recognizer.train(faces, np.array(ids))

# Sauve le modèle dans trainer/trainer.yml
recognizer.write('programs\\trainer\\trainer.yml')

# Imprime le nombre de visages entrainés
print("\n [INFO] {0} visages entrainés.".format(len(np.unique(ids))))