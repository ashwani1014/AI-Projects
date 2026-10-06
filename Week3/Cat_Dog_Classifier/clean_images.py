import os
from PIL import Image

data_dir = "data"
corrupted_files = []

for root, dirs, files in os.walk(data_dir):
    for file in files:
        if file.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
            path = os.path.join(root, file)
            try:
                img = Image.open(path)
                img.verify()
            except Exception as e:
                print(f"Corrupted image found: {path}")
                corrupted_files.append(path)

for path in corrupted_files:
    try:
        os.remove(path)
        print(f"Removed: {path}")
    except Exception as e:
        print(f"Failed to remove {path}: {e}")

print(f"Cleanup complete. Removed {len(corrupted_files)} corrupted images.")
