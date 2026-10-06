from pathlib import Path
from PIL import Image

dataset_path = Path("data/PetImages")

for class_name in ["Cat", "Dog"]:

    class_path = dataset_path / class_name

    print(f"\nChecking {class_name} images...")

    count = 0

    for image_path in class_path.glob("*.jpg"):

        try:
            with Image.open(image_path) as img:
                img.verify()

            count += 1

        except Exception:
            print("Invalid:", image_path)

    print(f"Checked: {count} images")