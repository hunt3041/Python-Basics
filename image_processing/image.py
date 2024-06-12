from PIL import Image, ImageFilter

img = Image.open('images/pikachu.jpg')
filtered_img = img.convert('L')
filtered_img.rotate(90)
filtered_img.show()
