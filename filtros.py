import cv2
import numpy as np
import matplotlib.pyplot as plt

#--- FILTRO MÉDIA ---

# Lê a imagem em escala de cinza
imagem = cv2.imread('rosa.png', cv2.IMREAD_GRAYSCALE)

# Aplicando o filtro de média com tamanho 7x7
filtro_7x7 = cv2.blur(imagem, (7, 7))

# Aplicando o filtro de média com tamanho 15x15
filtro_15x15 = cv2.blur(imagem, (15, 15))

# Aplicando o filtro de média com tamanho 25x25
filtro_25x25 = cv2.blur(imagem, (25, 25))

# Mostrar as imagens com matplotlib
plt.figure(figsize=(15, 10))

# Imagem original
plt.subplot(2, 2, 1)
plt.imshow(imagem, cmap='gray')
plt.title('Imagem Original')
plt.axis('off')

# Filtro 7x7
plt.subplot(2, 2, 2)
plt.imshow(filtro_7x7, cmap='gray')
plt.title('Filtro de Média 7x7')
plt.axis('off')

# Filtro 15x15
plt.subplot(2, 2, 3)
plt.imshow(filtro_15x15, cmap='gray')
plt.title('Filtro de Média 15x15')
plt.axis('off')

# Filtro 25x25
plt.subplot(2, 2, 4)
plt.imshow(filtro_25x25, cmap='gray')
plt.title('Filtro de Média 25x25')
plt.axis('off')

plt.show()

#--- FILTRO SOBEL ---

# Carregar a imagem em escala de cinza
imagem = cv2.imread('rosa.png', cv2.IMREAD_GRAYSCALE)

# Aplicar o filtro de Sobel na direção X
sobel_x = cv2.Sobel(imagem, cv2.CV_64F, 1, 0, ksize=3)
# Aplicar o filtro de Sobel na direção Y
sobel_y = cv2.Sobel(imagem, cv2.CV_64F, 0, 1, ksize=3)

# Converter os resultados para um formato visualizável
sobel_x = cv2.convertScaleAbs(sobel_x)
sobel_y = cv2.convertScaleAbs(sobel_y)

# Combinar as bordas
sobel_combinado = cv2.addWeighted(sobel_x, 0.5, sobel_y, 0.5, 0)

# Criar uma figura única com layout 2x2
plt.figure(figsize=(10, 10))

# Imagem Original
plt.subplot(2, 2, 1)
plt.title('Imagem Original')
plt.imshow(imagem, cmap='gray')
plt.axis('off')

# Filtro Sobel X
plt.subplot(2, 2, 2)
plt.title('Filtro Sobel X')
plt.imshow(sobel_x, cmap='gray')
plt.axis('off')

# Filtro Sobel Y
plt.subplot(2, 2, 3)
plt.title('Filtro Sobel Y')
plt.imshow(sobel_y, cmap='gray')
plt.axis('off')

# Sobel Combinado
plt.subplot(2, 2, 4)
plt.title('Sobel Combinado')
plt.imshow(sobel_combinado, cmap='gray')
plt.axis('off')

plt.tight_layout() # Ajusta o espaçamento para não sobrepor títulos
plt.show()

# --- FILTRO MEDIANA ---

# Aplicando o filtro de mediana com tamanhos diferentes
# O kernel deve ser um número ímpar
mediana_3x3 = cv2.medianBlur(imagem, 3)
mediana_7x7 = cv2.medianBlur(imagem, 7)
mediana_15x15 = cv2.medianBlur(imagem, 15)

# Mostrar os resultados da Mediana
plt.figure(figsize=(15, 10))

# Imagem Original
plt.subplot(2, 2, 1)
plt.title('Imagem Original')
plt.imshow(imagem, cmap='gray')
plt.axis('off')

# Mediana 3x3
plt.subplot(2, 2, 2)
plt.title('Filtro de Mediana 3x3')
plt.imshow(mediana_3x3, cmap='gray')
plt.axis('off')

# Mediana 7x7
plt.subplot(2, 2, 3)
plt.title('Filtro de Mediana 7x7')
plt.imshow(mediana_7x7, cmap='gray')
plt.axis('off')

# Mediana 15x15
plt.subplot(2, 2, 4)
plt.title('Filtro de Mediana 15x15')
plt.imshow(mediana_15x15, cmap='gray')
plt.axis('off')

plt.tight_layout()
plt.show()