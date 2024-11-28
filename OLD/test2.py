import cv2
import outils.perfImage as perfImage
from outils.webcamThreadParallele import FluxVideoParallele
import time


class DetectVisageAvecHaar:
    def __init__(self):
        self.__faceCascade = cv2.CascadeClassifier('D:\Anaconda3\Lib\site-packages\cv2\data\haarcascade_frontalface_alt.xml')

    def detectVisage(self,image):
        # On passe en niveau de gris (nécessaire pour haar)
        imageEnGris = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        ## Detection des visages
        coordVisages = self.__faceCascade.detectMultiScale(imageEnGris, 1.1, 4)

## On crée notre objet depuis la classe 
haar = DetectVisageAvecHaar()

## On initialise le flux de capture vidéo
## depuis la webcam ou caméra de surveillance
## videoWebcam = cv2.VideoCapture(0)
videoWebcam = FluxVideoParallele(0,100).demarrer()

## On instancie notre objet depuis la classe PerfImage
monPerfImage = perfImage.PerfImage(1)

## Top départ de notre boucle inifinie
## Tant que Vrai est toujours vrai :)
while True:
    ##on récupère la dernière image de la vidéo 
    valeurRetour, imageWebcam = videoWebcam.image()

    ## on s'assure qu'aucune erreur n'a été rencontrée
    if valeurRetour:
        # Detection avec haar
        coordVisages = haar.detectVisage(imageWebcam)
        ## Est ce qu'il y'a des visages ?
        if len(coordVisages) > 0:
            for coordUnVisage in coordVisages:
                x1 = coordUnVisage[0]
                y1 = coordUnVisage[1]
                largeur = coordUnVisage[2]
                hauteur = coordUnVisage[3]

                cv2.rectangle(imageWebcam, (x1, y1), (x1 + largeur, y1 + hauteur), (255, 0, 0), 2)
        ## On récupère notre texte avec les performances
        textePerf = monPerfImage.textePerf()

        ## On ajoute notre ligne à l'image
        cv2.putText(imageWebcam, textePerf, (10, 15),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), thickness=2, lineType=1)

        ## On affiche l'image
        cv2.imshow('Image de la webcam', imageWebcam)

        ## Comme c'est une boucle infinie, il faut bien se prévoir une sortie
    ## Dans notre cas, ce sera l'appui sur la touche Q
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

## Si on arrive jusque là, c'est qu'on est sortie de notre boucle
# Donc, on libère le flux de la webcam et on détruit la fenêtre d'affichage
videoWebcam.arreter()
cv2.destroyAllWindows()