import torch
import torch.nn as nn
import torch.optim as optim

from dataset import train_loader, val_loader
from model import CatDogCNN


# 1. Device
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

print("Using:", device)


# 2. Create model
model = CatDogCNN()
model = model.to(device)


# 3. Loss function
criterion = nn.CrossEntropyLoss()


# 4. Optimizer
optimizer = optim.Adam(
    model.parameters(),
    lr=0.001
)


# 5. Number of epochs
epochs = 5


# 6. Training
for epoch in range(epochs):

    model.train()

    running_loss = 0.0
    correct = 0
    total = 0

    for images, labels in train_loader:

        # Move data to CPU/GPU
        images = images.to(device)
        labels = labels.to(device)

        # Remove old gradients
        optimizer.zero_grad()

        # Forward pass
        outputs = model(images)

        # Calculate loss
        loss = criterion(outputs, labels)

        # Backpropagation
        loss.backward()

        # Update weights
        optimizer.step()

        # Statistics
        running_loss += loss.item()

        _, predicted = torch.max(outputs, 1)

        total += labels.size(0)
        correct += (predicted == labels).sum().item()

    train_accuracy = 100 * correct / total

    print(
        f"Epoch [{epoch + 1}/{epochs}] "
        f"Loss: {running_loss / len(train_loader):.4f} "
        f"Accuracy: {train_accuracy:.2f}%"
    )