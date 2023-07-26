import torch
from torchvision import datasets
from torchvision import transforms

# Define directories
data_dir = './data'
train_dir = f'{data_dir}/train_set'
quiz_dir = f'{data_dir}/quiz_set'
test_dir = f'{data_dir}/test_set'

def main():
    # Load your dataset without any normalization
    dataset = datasets.ImageFolder(data_dir, transform=transforms.Compose([
        transforms.Resize((400,400)),
        transforms.ToTensor()
    ]))

    # Create a DataLoader
    dataloader = torch.utils.data.DataLoader(dataset, batch_size=64, num_workers=6)

    mean = 0.
    std = 0.
    for images, _ in dataloader:
        batch_samples = images.size(0) # batch size (the last batch can have smaller size!)
        images = images.view(batch_samples, images.size(1), -1)
        mean += images.mean(2).sum(0)
        std += images.std(2).sum(0)

    mean /= len(dataloader.dataset)
    std /= len(dataloader.dataset)

    print(mean) #tensor([0.7754, 0.7763, 0.7836]) output
    print(std) #tensor([0.3839, 0.3824, 0.3702]) output
    

if __name__ == '__main__':
    main()