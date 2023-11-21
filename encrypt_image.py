
#rep

from PIL import Image
import numpy as np

def load_image(image_path)
    with Image.open(image_path) as img:
        return np.array(img)
    
def encrypt_imagen(image_array, key):
    encrypted_imagen = image_array.copy()
    for index, value in np.ndenumerate(imagen_array):
        encrypted_image[index] = value ^ key 
        return encrypted_image
    
def guardar_imagen(image_array, output_path):
    img = Image.fromarray(image_array)
    img.save(output_path)

