import torch.nn as nn


class CatDogCNN(nn.Module):

    def __init__(self):
        super().__init__()

        self.features = nn.Sequential(

            # Block 1
            nn.Conv2d(3, 32, kernel_size=3, padding=1),
            nn.ReLU(),
            nn.MaxPool2d(2),

            # Block 2
            nn.Conv2d(32, 64, kernel_size=3, padding=1),
            nn.ReLU(),
            nn.MaxPool2d(2),

        )

        self.classifier = nn.Sequential(

            nn.Flatten(),

            nn.Linear(64 * 56 * 56, 128),
            nn.ReLU(),

            nn.Linear(128, 2)
        )

    def forward(self, x):

        x = self.features(x)

        x = self.classifier(x)

        return x