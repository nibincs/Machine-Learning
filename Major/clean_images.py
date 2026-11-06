from PIL import Image
import os

dataset_path = "dataset/organized"

bad_files = []

for root, dirs, files in os.walk(dataset_path):
    for file in files:
        path = os.path.join(root, file)

        try:
            img = Image.open(path)
            img.verify()
        except Exception:
            bad_files.append(path)

print(f"Found {len(bad_files)} corrupted images")

for file in bad_files:
    print("Removing:", file)
    os.remove(file)

print("Cleaning completed")