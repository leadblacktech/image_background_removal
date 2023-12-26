        
from rembg import remove
from PIL import Image
import io


input_path = 'images/voodoo10.JPG'
output_path = input_path.replace("images", "results")

with open(input_path, 'rb') as i:
    with open(output_path, 'wb') as o:
        original_image = i.read()
        output = remove(original_image)
        o.write(output)