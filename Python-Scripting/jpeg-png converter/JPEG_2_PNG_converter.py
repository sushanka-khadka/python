import sys
import os
from PIL import Image

# grab the first and the second argument
image_folder= sys.argv[1]   # 0 is the file name
output_folder= sys.argv[2]

# check if exists / if not create it
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# loop through the directory
for file_name in os.listdir(image_folder):
    print(f"{image_folder}/{file_name}")
    img= Image.open(f"{image_folder}/{file_name}")
    # clean_filename= file_name.split('.')[0]    or
    clean_filename= os.path.splitext(file_name)[0]
    # convert jpeg to png and save
    img.save(f"{output_folder}/{clean_filename}.png",'PNG')