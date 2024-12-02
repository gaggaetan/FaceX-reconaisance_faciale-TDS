import cv2
import win32gui,win32con

def write_on_img (img, text, H, L):
    """
    Ecrit sur l'image le text ... , à la poxition H=.. et L=..
    """
    cv2.putText(img, text, (H, L), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)
    return img


def cam_read(camera) :
    """
    Lis la camera et remvois l'image
    """
    ret, img = camera.read()
    return ret, img

def show_img(img):
    """
    Affiche l'image
    """
    cv2.imshow('FaceX-reconnaissance_faciale', img)

    # Change icone de la fenetre
    hwnd = win32gui.FindWindow(None, "FaceX-reconnaissance_faciale")
    icon_path = "./programs/utils/faceX_logo.ico"
    win32gui.SendMessage(hwnd, win32con.WM_SETICON, win32con.ICON_BIG, win32gui.LoadImage(None, icon_path, win32con.IMAGE_ICON, 0, 0, win32con.LR_LOADFROMFILE | win32con.LR_DEFAULTSIZE))