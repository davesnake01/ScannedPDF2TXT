from wand.image import Image
from wand.color import Color

with Image(filename="encuestas Sandra Fernandez Feijoo-1.pdf", resolution=400) as img:
  with Image(width=img.width, height=img.height, background=Color("white")) as bg:
    bg.composite(img,0,0)
    bg.save(filename="image.png")
