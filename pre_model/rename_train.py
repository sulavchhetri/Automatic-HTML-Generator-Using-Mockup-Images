import os
from pathlib import Path

images_path = os.path.join(Path(__file__).parent , "train", "images")
labels_path = os.path.join(Path(__file__).parent , "train", "labels")

files = os.listdir(images_path)

for item in files:
    old_path = os.path.join(images_path , item)
    file_name = int(item.split(".")[0]) + 1
    new_path = os.path.join(images_path,str(file_name)+'.jpg')
    os.rename(old_path, new_path)


labels = os.listdir(labels_path)
for item in labels:
    old_path = os.path.join(labels_path , item)
    file_name = int(item.split(".")[0]) + 1
    new_path = os.path.join(labels_path,str(file_name)+'.txt')
    os.rename(old_path, new_path)

