from rembg import remove
from PIL import Image

input_path = 'Python.png'
output_path = 'Python.png'

inp = Image.open(input_path)
output = remove(inp)
output.save(output_path)