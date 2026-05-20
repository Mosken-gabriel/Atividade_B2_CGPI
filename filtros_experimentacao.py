import cv2
import numpy as np
import matplotlib.pyplot as plt

# Lê a imagem original em escala de cinza
imagem = cv2.imread('rosa.png', cv2.IMREAD_GRAYSCALE)

# ==========================================
# --- 1. FILTRO MÉDIA (Experimentação) ---
# ==========================================

# Aplicando o filtro de média com tamanhos crescentes de kernel
media_3x3 = cv2.blur(imagem, (3, 3))
media_5x5 = cv2.blur(imagem, (5, 5))
media_7x7 = cv2.blur(imagem, (7, 7))

# Mostrar os resultados da Média
plt.figure(figsize=(15, 10))

plt.subplot(2, 2, 1)
plt.imshow(imagem, cmap='gray')
plt.title('Imagem Original')
plt.axis('off')

plt.subplot(2, 2, 2)
plt.imshow(media_3x3, cmap='gray')
plt.title('Filtro de Média 3x3')
plt.axis('off')

plt.subplot(2, 2, 3)
plt.imshow(media_5x5, cmap='gray')
plt.title('Filtro de Média 5x5')
plt.axis('off')

plt.subplot(2, 2, 4)
plt.imshow(media_7x7, cmap='gray')
plt.title('Filtro de Média 7x7')
plt.axis('off')

plt.tight_layout()
plt.show()

# ==========================================
# --- 2. FILTRO MEDIANA (Experimentação) ---
# ==========================================

# Aplicando o filtro de mediana com tamanhos crescentes de kernel (sempre ímpares)
mediana_3x3 = cv2.medianBlur(imagem, 3)
mediana_5x5 = cv2.medianBlur(imagem, 5)
mediana_7x7 = cv2.medianBlur(imagem, 7)

# Mostrar os resultados da Mediana
plt.figure(figsize=(15, 10))

plt.subplot(2, 2, 1)
plt.title('Imagem Original')
plt.imshow(imagem, cmap='gray')
plt.axis('off')

plt.subplot(2, 2, 2)
plt.title('Filtro de Mediana 3x3')
plt.imshow(mediana_3x3, cmap='gray')
plt.axis('off')

plt.subplot(2, 2, 3)
plt.title('Filtro de Mediana 5x5')
plt.imshow(mediana_5x5, cmap='gray')
plt.axis('off')

plt.subplot(2, 2, 4)
plt.title('Filtro de Mediana 7x7')
plt.imshow(mediana_7x7, cmap='gray')
plt.axis('off')

plt.tight_layout()
plt.show()

