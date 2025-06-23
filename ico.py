from PIL import Image

img = Image.open("visionsmith.png")
img.save("vision_smith_tray.ico", format="ICO", sizes=[(64, 64)])
