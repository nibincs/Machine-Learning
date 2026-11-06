import pandas as pd
import os
import shutil

df = pd.read_csv("dataset/HAM10000_metadata.csv")

image_folders = [
    "dataset/HAM10000_images_part_1",
    "dataset/HAM10000_images_part_2"
]

output_folder = "dataset/organized"

os.makedirs(output_folder, exist_ok=True)

for disease in df["dx"].unique():
    os.makedirs(os.path.join(output_folder, disease), exist_ok=True)

for _, row in df.iterrows():
    image_name = row["image_id"] + ".jpg"
    disease = row["dx"]

    source = None

    for folder in image_folders:
        path = os.path.join(folder, image_name)

        if os.path.exists(path):
            source = path
            break

    if source:
        destination = os.path.join(output_folder, disease, image_name)

        if not os.path.exists(destination):
            shutil.copy(source, destination)

print("Dataset organized successfully")