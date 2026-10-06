import torch

from dataset import test_loader
from model import CatDogCNN


# 1. Device
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

print("Using:", device)


# 2. Create model
model = CatDogCNN()
model = model.to(device)


# 3. Load trained weights
model.load_state_dict(
    torch.load("models/cat_dog_cnn.pth", map_location=device)
)


# 4. Evaluation mode
model.eval()


# 5. Count correct predictions
correct = 0
total = 0


# 6. No gradient required
with torch.no_grad():

    for images, labels in test_loader:

        images = images.to(device)
        labels = labels.to(device)

        # Prediction
        outputs = model(images)

        # Get predicted class
        _, predicted = torch.max(outputs, 1)

        # Statistics
        total += labels.size(0)
        correct += (predicted == labels).sum().item()


# 7. Calculate accuracy
test_accuracy = 100 * correct / total


print(f"Test Accuracy: {test_accuracy:.2f}%")