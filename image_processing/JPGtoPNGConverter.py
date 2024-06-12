import sys
import os
from PIL import Image

# grab first and second command line arguments
img_source_folder = sys.argv[1]
new_folder = sys.argv[2]
print(img_source_folder)
print(new_folder)

# check if new/ exists, if not create it
if os.path.exists(new_folder):
    print('Directory already exists.')
else:
    os.makedirs(new_folder)

# loop through images folder, convert images to png
for entry in os.listdir(img_source_folder):
    print(entry)
    dot_index = entry.find('.')
    name = entry[0:dot_index]
    img = Image.open('images/' + entry)
    img.save(new_folder + name + '.png', 'png')

# save to new folder
