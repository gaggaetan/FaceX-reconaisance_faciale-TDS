import cv2
import json


# initialiser le modele avec les élements entrainer
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('trainer/trainer.yml') 
cascadePath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascadePath);


# Récuperer tous les users du fichier 'users_names.json'
with open('users_names.json', 'r') as file:
    users_names = json.load(file)
print("All users are : ", users_names["users_names"])

cam = cv2.VideoCapture(0)



while True:

    ret, img = cam.read()
    grayIMG = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(
        grayIMG,
        scaleFactor=1.26,
        minNeighbors=5,
        minSize=(int(100), int(100)),
    )

    print(faces) #récup emplacement des faces




    cv2.imshow('camera', img)
    if cv2.waitKey(1) & 0xff == 27 :
        break



print("\n exit program")
cam.release()
cv2.destroyAllWindows()

