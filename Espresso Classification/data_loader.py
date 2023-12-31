import torch
from torchvision import transforms
from torchvision.datasets import ImageFolder

# Set random seed for reproducibility
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
    'train': torch.utils.data.DataLoader(image_datasets['train'], batch_size=32, shuffle=True, num_workers=4),
    'quiz': torch.utils.data.DataLoader(image_datasets['quiz'], batch_size=32, shuffle=False, num_workers=4),
    'test': torch.utils.data.DataLoader(image_datasets['test'], batch_size=32, shuffle=False, num_workers=4),
}