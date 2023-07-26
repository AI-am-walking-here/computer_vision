import random

# Import PyTorch
import torch
from torch import nn

# Import torchvision
import torchvision
from torchvision import datasets
from torchvision.datasets import ImageFolder

from torchvision import transforms
from torchvision.transforms import ToTensor

# Import matplotlib for visualization
import matplotlib.pyplot as plt

# # Check versions
# print(torch.__version__)
# print(torchvision.__version__)

random.seed(117)
torch.manual_seed(117)


# Define directories
data_dir = './data'
train_dir = f'{data_dir}/train_set'
quiz_dir = f'{data_dir}/quiz_set'
test_dir = f'{data_dir}/test_set'

# Data transforms dictionary
data_transforms = {
    'train': transforms.Compose([
        transforms.RandomHorizontalFlip(),
        transforms.RandomVerticalFlip(),
        transforms.RandomRotation(15),
        transforms.ToTensor(),
        transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
        ]),

    'quiz': transforms.Compose([
        transforms.ToTensor(),
        transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
    ]),

    'test': transforms.Compose([
        transforms.ToTensor(),
        transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
    ]),
}

# Load datasets with ImageFolder
image_datasets = {
    'train': ImageFolder(train_dir, data_transforms['train']),
    'quiz': ImageFolder(quiz_dir, data_transforms['quiz']),
    'test': ImageFolder(test_dir, data_transforms['test']),
}

# Create dataloaders
dataloaders = {
    'train': torch.utils.data.DataLoader(image_datasets['train'], batch_size=4, shuffle=True, num_workers=6),
    'quiz': torch.utils.data.DataLoader(image_datasets['quiz'], batch_size=4, shuffle=False, num_workers=6),
    'test': torch.utils.data.DataLoader(image_datasets['test'], batch_size=4, shuffle=False, num_workers=6),
}

