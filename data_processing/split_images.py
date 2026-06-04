# packages
import os
import pandas as pd
import random

# data 
base = os.path.abspath(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
filepath_xlsx = os.path.join(base, "data", "setters.xlsx")
df = pd.read_excel(filepath_xlsx)
splits = ["train", "val", "test"]

# loop through set folders in data/set_images and separate into set_locs
set_folder_path = os.path.join(base, "data", "set_images")
for set in os.listdir(set_folder_path):
    # if path to unlabeled images exists(data/set_images) label
    indiv_set_images_dir = os.path.join(set_folder_path, set)
    if os.path.exists(indiv_set_images_dir):
        # collect_images 
        images = [img for img in os.listdir(indiv_set_images_dir) if img.lower().endswith(".png")]
        random.seed(256)
        random.shuffle(images)
        # split
        split_dir = os.path.join(base, "data", "split")
        for split in splits:
            os.makedirs(os.path.join(split_dir, split), exist_ok = True)
            






