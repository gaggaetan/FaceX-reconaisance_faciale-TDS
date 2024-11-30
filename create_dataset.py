import cv2
import time
from utils.cam_utils import *
from utils.create_dataset_utils import *

NBR_SAMPLE = 30

# Reconaisance faciale xml file
haar_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Initialisation de la caméra
cam = cv2.VideoCapture(0)

# Avoir user name du sample et sauver dans le fichier de nom
get_user_name()

# Affichage camera
ret, img = cam_read(cam)
show_img(img)

# Lancement des photos
print("\n Start in 3 sec :")
print("3")
time.sleep(1)
print("2")
time.sleep(1)
print("1")
time.sleep(1)

nbr_photos = 0
prev_time = time.time()
id = find_next_id()


# Récupere les Samples
while(True):

    # Récuperation image 
    ret, img = cam_read(cam)

    if cv2.waitKey(1) & 0xff == 27 :
        break
    

    grayIMG = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Détection image
    faces = haar_cascade.detectMultiScale(grayIMG, 1.1, 5)

    # Rectangle
    for (x,y,w,h) in faces:

        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)    
        nbr_photos += 1

        # Sauve l'image
        cv2.imwrite("data/user." + str(id) + '.' + str(nbr_photos) + ".jpg", grayIMG[y:y+h,x:x+w])

        print("Photo ", nbr_photos)

    # Calcul du FPS
    curr_time = time.time()
    fps = 1 / (curr_time - prev_time)
    prev_time = curr_time

    # Afficher le FPS sur l'image
    img = write_on_img(img, f"FPS: {fps:.2f}", 10, 30)
    img = write_on_img(img, f"Image: {nbr_photos}", 10, 60)

    show_img(img)

    if nbr_photos >= NBR_SAMPLE-1: 
         break # fin du program si l'on à tous les samples
    
    time.sleep(0.3)
 
print("\n exit program")
cam.release()
cv2.destroyAllWindows()