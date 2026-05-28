# packages
import os
from PIL import Image

# data path
path_to_sets_folder = "C:/Users/jfung/Files/Datasets/set_images/"

# read in images from games 1-8 with sets up to four
for set in os.listdir(path_to_sets_folder): # loop through game sets in data
    set_path = os.path.join(path_to_sets_folder, set)
    # error handling
    if not os.path.isdir(set_path):
        print(f"No set path at {set_path}")
        continue
    for posession in os.listdir(set_path): # loop through posessions in set
        pos_path = os.path.join(set_path, posession)
        if not pos_path.lower().endswith(".png"):
            print(f"no image path at {pos_path}")
            continue
        img = Image.open(pos_path).convert("RGB")
        # resize
        img = img.resize((1024, 512))
        #save
        img.save(pos_path, format = "PNG")
        print(f"Resized image: {pos_path}" )

