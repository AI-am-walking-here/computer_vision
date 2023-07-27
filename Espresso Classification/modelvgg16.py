import torch
import torch.nn as nn
from torchvision import models
from torch.optim import Adam
from torch.autograd import Variable
from data_loader import dataloaders

def main():
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

    # Load the pretrained model
    vgg16 = models.vgg16(pretrained=True)

    # Freeze model weights
    for param in vgg16.features.parameters():
        param.requires_grad = False

    # Change the final layer of VGG16 Model for Transfer Learning
    fc_features = vgg16.classifier[6].in_features
    vgg16.classifier[6] = nn.Linear(fc_features, 3)

    vgg16 = vgg16.to(device)
    print(next(vgg16.parameters()).device)

    criterion = nn.CrossEntropyLoss()
    optimizer = Adam(vgg16.parameters(), lr=0.001)

    def train_model(model, criterion, optimizer, num_epochs=25):
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
                    print(inputs.device)

                    optimizer.zero_grad()

                    with torch.set_grad_enabled(phase == 'train'):
                        outputs = model(inputs)
                        _, preds = torch.max(outputs, 1)
                        loss = criterion(outputs, labels)

                        if phase == 'train':
                            loss.backward()
                            optimizer.step()

                            # Add synchronization after backward pass
                            torch.cuda.synchronize()

                    running_loss += loss.item() * inputs.size(0)
                    running_corrects += torch.sum(preds == labels.data)

                epoch_loss = running_loss / len(dataloaders[phase].dataset)
                epoch_acc = running_corrects.double() / len(dataloaders[phase].dataset)

                print('{} Loss: {:.4f} Acc: {:.4f}'.format(phase, epoch_loss, epoch_acc))

        return model

    vgg16 = train_model(vgg16, criterion, optimizer, num_epochs=25)

    torch.save(vgg16.state_dict(), 'vgg16_trained_model.pth')

if __name__ == '__main__':
    main()