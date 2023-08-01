import torch
import os
import torch.nn as nn
from torchvision import models
from torch.optim import Adam
from data_loader import dataloaders  # You need to provide this module
import time

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# Load the pretrained model
mobilenet = models.mobilenet_v3_small(pretrained=True)

# Freeze model weights
for param in mobilenet.parameters():
    param.requires_grad = False

# Change the final layer of MobileNet Model for Transfer Learning
num_features = mobilenet.classifier[3].in_features
num_classes = 3  # Set this to the number of classes in your problem
mobilenet.classifier[3] = nn.Linear(num_features, num_classes)

mobilenet = mobilenet.to(device)

loss_function = nn.CrossEntropyLoss()
optimizer = Adam(mobilenet.parameters(), lr=0.001)

def train_model(model, loss_function, optimizer, num_epochs=25):
    for epoch in range(num_epochs):
        print('Epoch {}/{}'.format(epoch, num_epochs - 1))
        print('-' * 10)

        for phase in ['train', 'quiz']:
            if phase == 'train':
                model.train()
            else:
                model.eval()

            running_loss = 0.0
            running_corrects = 0

            for inputs, labels in dataloaders[phase]:
                inputs = inputs.to(device)
                labels = labels.to(device)

                start_time = time.time()
                optimizer.zero_grad()

                with torch.set_grad_enabled(phase == 'train'):
                    outputs = model(inputs)
                    _, preds = torch.max(outputs, 1)
                    loss = loss_function(outputs, labels)

                    if phase == 'train':
                        loss.backward()
                        optimizer.step()

                end_time = time.time()
                print(f"Elapsed time: {end_time - start_time} s")

                running_loss += loss.item() * inputs.size(0)
                running_corrects += torch.sum(preds == labels.data)

            epoch_loss = running_loss / len(dataloaders[phase].dataset)
            epoch_acc = running_corrects.double() / len(dataloaders[phase].dataset)

            print('{} Loss: {:.4f} Acc: {:.4f}'.format(phase, epoch_loss, epoch_acc))

    return model

def main():
    global mobilenet  # Declare mobilenet as a global variable
    mobilenet = train_model(mobilenet, loss_function, optimizer, num_epochs=25)

    # Create the folder 'trained models' if it doesn't exist
    save_folder = 'trained models'
    os.makedirs(save_folder, exist_ok=True)

    # Save the model to the specified path
    save_path = os.path.join(save_folder, 'mobilenet_trained_model.pth')
    torch.save(mobilenet.state_dict(), save_path)

if __name__ == '__main__':
    main()