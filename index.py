import os
from PIL import Image

LOGO_NAME = input('Enter the logo name with extension :')
NEW_FOLDER_NAME = input('Enter the folder name :')

logo_image = Image.open(LOGO_NAME)
logo_with , logo_height = Image.size



# create folder

os.mkdir(NEW_FOLDER_NAME )

run_scr_folder = input('Enter your folder path : ')
for filename in os.listdir(run_scr_folder):
    if not(filename.endswith('.png' , 'jpg'  ) or filename==LOGO_NAME):
        continue  # skip non-JPG and png files
    img = Image.open(f'{run_scr_folder}/{filename}')
    width , height = img.size

    img.paste(width-logo_with , height-logo_height)

    img.save(os.path.join(NEW_FOLDER_NAME ,filename))


