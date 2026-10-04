from pathlib import Path

cat_path = Path("data/PetImages/Cat")
dog_path = Path("data/PetImages/Dog")

print("Cats:", len(list(cat_path.glob("*.jpg"))))
print("Dogs:", len(list(dog_path.glob("*.jpg"))))