from PIL import Image

img = Image.open("logo.jpg")
# icon_sizes = [(16, 16), (32, 32), (48, 48), (64, 64)]
icon_sizes = [(24, 24)]
img.save('logo.ico', sizes=icon_sizes)
