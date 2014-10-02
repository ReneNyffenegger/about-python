import Image

im = Image.new('RGB', (256, 256), "black")

pixels = im.load()

for     x in range(0, 256):
    for y in range(0, 256):

        pixels[x, y] = (x, y, 127)

im.show()
im.save('pixels.png')
