
#rep

from PIL import Image
import numpy as np

def load_image(image_path):
    with Image.open(image_path) as img:
        return np.array(img)
    
def encrypt_imagen(image_array, key):
    encrypted_imagen = image_array.copy()
    for index, value in np.ndenumerate(image_array):
        encrypted_imagen[index] = value ^ key 
        return encrypted_imagen
    
def guardar_imagen(image_array, output_path):
    img = Image.fromarray(image_array)
    img.save(output_path)

image_path = ' '
encrypted_imagen_path = ' '

og_image = load_image(image_path)
key = 123456

encrypted_imagen = encrypt_imagen(og_image, key)
guardar_imagen(encrypted_imagen, encrypted_imagen_path)