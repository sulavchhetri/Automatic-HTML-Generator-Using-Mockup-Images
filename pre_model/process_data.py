import os
import shutil
from pathlib import Path

test_path = os.path.join(Path(__file__).parent , "data", "train")

labels_path = os.path.join(Path(__file__).parent , "labels")
images_path = os.path.join(Path(__file__).parent , "images")

files = os.listdir(test_path)

for index, item in enumerate(files):
    old_path = os.path.join(test_path, item)
    file_name = item.split(".jpg")
    if len(file_name) ==2 :
        file_name = index
        new_path = os.path.join(test_path, str(file_name)+ ".jpg")
        os.rename(old_path,new_path)
        shutil.move(new_path, images_path )
    else:
        file_name = index -1
        new_path = os.path.join(test_path, str(file_name)+ ".txt")
        os.rename(old_path, new_path)
        shutil.move(new_path, labels_path)
