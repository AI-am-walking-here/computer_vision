import torch
import os
import torch.nn as nn
from torchvision import models
from torch.optim import Adam
from data_loader import dataloaders
import time

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# Load the pretrained model
weights = models.VGG16_Weights.IMAGENET1K_V1 # '.DEFAULT' would also work
vgg16 = models.vgg16(weights=weights)


# Freeze model weights
for param in vgg16.features.parameters():
    param.requires_grad = False

# Change the final layer of VGG16 Model for Transfer Learning
in_features = vgg16.classifier[6].in_features
vgg16.classifier[6] = nn.Linear(in_features, 3)

vgg16 = vgg16.to(device)

loss_function = nn.CrossEntropyLoss()
optimizer = Adam(vgg16.parameters(), lr=0.001)

def train_model(model, loss_function, optimizer, num_epochs=25):
    global vgg16  # Declare vgg16 as a global variable

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
    global vgg16  # Declare vgg16 as a global variable
    vgg16 = train_model(vgg16, loss_function, optimizer, num_epochs=25)

    # Create the folder 'trained models' if it doesn't exist
    save_folder = 'trained models'
    os.makedirs(save_folder, exist_ok=True)

    # Save the model to the specified path
    save_path = os.path.join(save_folder, 'vgg16_trained_model.pth')
    torch.save(vgg16.state_dict(), save_path)

if __name__ == '__main__':
    main()