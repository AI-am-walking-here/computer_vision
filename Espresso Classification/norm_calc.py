import torch
from torchvision import datasets
from torchvision import transforms

# Usefull if creating own NN

# Define directories
data_dir = './data'
train_dir = f'{data_dir}/train_set'
quiz_dir = f'{data_dir}/quiz_set'
test_dir = f'{data_dir}/test_set'

# Normalization = ( x-min(x) / max(x)-min(x) )

def main():
    # Load dataset without any normalization
    dataset = datasets.ImageFolder(data_dir, transform=transforms.Compose([
        transforms.Resize((400,400)),
        transforms.ToTensor()
    ]))

    # Create a DataLoader
    dataloader = torch.utils.data.DataLoader(dataset, batch_size=64, num_workers=6)

    mean = 0.
    std = 0.
    for images, _ in dataloader: # Data loader returns (images, labels) labels arn't important
        batch_samples = images.size(0) # Batch size 
        color_channels = images.size(1) # Num of color channels
        images = images.view(batch_samples, color_channels, -1) # Auto-infer remaining dimension using (-1)
        std += images.std(2).sum(0) # Calcs std at 2nd dimension

    mean /= len(dataloader.dataset)
    std /= len(dataloader.dataset)

    print(mean) # Output: Tensor([0.7754, 0.7763, 0.7836]) 
    print(std) # Output: Tensor([0.3839, 0.3824, 0.3702]) 
    

if __name__ == '__main__':
    main()