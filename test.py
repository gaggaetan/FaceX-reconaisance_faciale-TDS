import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import random

# Charger l'image en niveaux de gris
image = np.array(Image.open('IMG/HE202277.jpg').convert('L'))

# Appliquer un filtre Sobel pour détecter les contours
sobel_x = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])
sobel_y = np.array([[-1, -2, -1], [0, 0, 0], [1, 2, 1]])

def apply_filter(image, filter):
    h, w = image.shape
    filtered_image = np.zeros((h, w))
    for i in range(1, h - 1):
        for j in range(1, w - 1):
            region = image[i - 1:i + 2, j - 1:j + 2]
            filtered_image[i, j] = abs(np.sum(region * filter))
    return filtered_image

# Appliquer les filtres de Sobel
grad_x = apply_filter(image, sobel_x)
grad_y = apply_filter(image, sobel_y)

# Calculer la magnitude du gradient
gradient_magnitude = np.sqrt(grad_x**2 + grad_y**2)
gradient_magnitude = (gradient_magnitude / gradient_magnitude.max()) * 255  # Normaliser

# Appliquer un seuillage pour binariser l'image
binary_image = np.where(gradient_magnitude > 50, 255, 0).astype(np.uint8)

# Détecter les blobs dans l'image binaire
def detect_blobs(binary_image):
    h, w = binary_image.shape
    visited = np.zeros((h, w), dtype=bool)
    blobs = []

    def dfs(x, y, blob):
        stack = [(x, y)]
        while stack:
            cx, cy = stack.pop()
            if cx < 0 or cx >= h or cy < 0 or cy >= w:
                continue
            if binary_image[cx, cy] == 0 or visited[cx, cy]:
                continue
            visited[cx, cy] = True
            blob.append((cx, cy))
            stack.extend([(cx + 1, cy), (cx - 1, cy), (cx, cy + 1), (cx, cy - 1)])

    for i in range(h):
        for j in range(w):
            if binary_image[i, j] == 255 and not visited[i, j]:
                blob = []
                dfs(i, j, blob)
                blobs.append(blob)
    return blobs

# Détecter et afficher tous les blobs
blobs = detect_blobs(binary_image)

# Afficher le résultat avec les blobs entourés de rectangles colorés
plt.figure(figsize=(10, 5))
plt.imshow(binary_image, cmap='gray')
plt.title('Tous les blobs détectés')

# Dessiner des rectangles autour de chaque blob
for blob in blobs:
    ys, xs = zip(*blob)
    min_x, max_x = min(xs), max(xs)
    min_y, max_y = min(ys), max(ys)
    width, height = max_x - min_x, max_y - min_y

    # Générer une couleur aléatoire pour chaque blob
    color = (random.random(), random.random(), random.random())
    
    # Dessiner le rectangle autour du blob
    if width > 0 and height > 0:  # S'assurer que le blob est valide
        plt.gca().add_patch(plt.Rectangle((min_x, min_y), width, height, edgecolor=color, facecolor='none', linewidth=1.5))

plt.show()
