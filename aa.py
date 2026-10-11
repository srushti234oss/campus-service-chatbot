from PIL import Image
from pyzbar.pyzbar import decode

img = Image.open("triphala_qr.png")

result = decode(img)

print(result)