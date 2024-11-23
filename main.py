import math

import cv2
import numpy as np
from PIL import Image, ImageOps
import matplotlib.pyplot as plt



# Charger l'image et la convertir en niveaux de gris
image = Image.open('IMG/gaetan.jpg')
image = ImageOps.grayscale(image)




# Définir le filtre Laplacien (3x3)
convolutionFilter = [[-1, 0, 1],
                     [-2, 0, 2],
                     [-1, 0, 1]]
convolutionFilter2 = [[-1, -2, -1],
                      [0, 0, 0],
                      [1, 2, 1]]


# Convertir l'image en tableau numpy
image_array = np.array(image)


# Fonction pour appliquer la convolution
def convolution(image_array, x, y, filter):
    # Prendre une fenêtre 3x3 autour du point (x, y)
    result = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            # Appliquer le filtre sur la région locale de l'image
            result += image_array[y + i][x + j] * filter[i + 1][j + 1]
    return result




# Créer une nouvelle image pour stocker le résultat
convoluted_image = np.zeros_like(image_array)

# Appliquer la convolution sur chaque pixel (sauf les bords)
for y in range(1, len(image_array) - 1):
    for x in range(1, len(image_array[y]) - 1):
        convoluted_image[y, x] = np.sqrt(pow(convolution(image_array, x, y, convolutionFilter), 2.0) + pow(convolution(image_array, x, y, convolutionFilter2), 2.0))
        
        


# Afficher l'image originale et l'image convoluée
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.title('Image originale')
plt.imshow(image_array, cmap='gray')

plt.subplot(1, 2, 2)
plt.title('Image après convolution')
plt.imshow(convoluted_image, cmap='gray')


plt.show()
