import cv2
import json
import time
from utils.cam_utils import *
from utils.face_recongnition import *


# initialiser le modele avec les élements entrainer
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('programs\\trainer\\trainer.yml') 
cascadePath = "programs\\utils\\haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascadePath);


# Récuperer tous les users du fichier 'users_names.json'
with open('programs\\utils\\users_names.json', 'r') as file:
    users_names = json.load(file)["users_names"]

    if len(users_names) == 0 :
        print("No users found")
        quit()
    print("All users are : ", users_names)

cam = cv2.VideoCapture(0)
prev_time = time.time()


while True:

    ret, img = cam_read(cam)
    grayIMG = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # récupere les emplacement des tete
    faces = faceCascade.detectMultiScale(
        grayIMG,
        scaleFactor=1.26,
        minNeighbors=5,
        minSize=(int(100), int(100)),
    )

    for (x, y, w, h) in faces:

        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)


        id, confidence = predict_user(recognizer, users_names, grayIMG, x, h, x, w)


        write_on_img(img, str(id), x + 5, y - 5)
        write_on_img(img, str(confidence), x + 5, y + h - 5)



    # Afficher le FPS sur l'image
    curr_time = time.time()
    fps = 1 / (curr_time - prev_time)
    prev_time = curr_time
    img = write_on_img(img, f"FPS: {fps:.2f}", 10, 30)

    show_img(img)

    if cv2.waitKey(1) & 0xff == 27 :
        break


print("\n exit program")
cam.release()
cv2.destroyAllWindows()

