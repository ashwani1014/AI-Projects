from pathlib import Path
import random
import shutil

SOURCE = Path("data/PetImages")
DESTINATION = Path("data")

classes = ["Cat", "Dog"]

train_ratio = 0.70
val_ratio = 0.15
test_ratio = 0.15

random.seed(42)

for class_name in classes:

    images = list((SOURCE / class_name).glob("*.jpg"))

    random.shuffle(images)

    total = len(images)

    train_end = int(total * train_ratio)
    val_end = train_end + int(total * val_ratio)

    train_images = images[:train_end]
    val_images = images[train_end:val_end]
    test_images = images[val_end:]

    print(f"\n{class_name}")
    print("Train:", len(train_images))
    print("Validation:", len(val_images))
    print("Test:", len(test_images))

    for split_name, split_images in [
        ("train", train_images),
        ("val", val_images),
        ("test", test_images)
    ]:

        destination = DESTINATION / split_name / class_name
        destination.mkdir(parents=True, exist_ok=True)

        for image in split_images:
            shutil.copy2(image, destination / image.name)

print("\nDataset split completed!")