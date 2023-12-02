import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

def template_matching(image, template):
    # Converte as imagens para arrays numpy
    img_array = np.array(image)
    template_array = np.array(template)

    # Obtém as dimensões da imagem e do template
    img_height, img_width = img_array.shape
    template_height, template_width = template_array.shape

    # Calcula a soma das diferenças absolutas
    result = np.zeros((img_height - template_height + 1, img_width - template_width + 1))

    for y in range(result.shape[0]):
        for x in range(result.shape[1]):
            region = img_array[y:y + template_height, x:x + template_width]
            diff = np.sum(np.abs(region - template_array))
            result[y, x] = diff

    return result

def plot_result(image, template, result):
    fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(12, 4))

    ax1.imshow(image, cmap='gray')
    ax1.set_title('Imagem Original')

    ax2.imshow(template, cmap='gray')
    ax2.set_title('Template')

    ax3.imshow(result, cmap='viridis')
    ax3.set_title('Resultado do Template Matching')

    plt.show()

# Carrega a imagem e o template
image = Image.open('Projeto/img.jpg').convert('L')
template = Image.open('Projeto/quadrado.jpg').convert('L')

# Executa o Template Matching
result = template_matching(image, template)

# Plota os resultados
plot_result(image, template, result)
