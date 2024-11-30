import cv2

def write_on_img (img, text, H, L):
    """
    Ecrit sur l'image le text ... , à la poxition H=.. et L=..
    """
    cv2.putText(img, text, (H, L), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)
    return img


def cam_read(cam) :
    """
    Lis la camera et remvois l'image
    """
    ret, img = cam.read()
    return ret, img

def show_img(img):
    """
    Affiche l'image
    """
    cv2.imshow('image', img)