from model import RNN
import train
import utils
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import Dataset, DataLoader
from torch import cuda
from torchvision import datasets
from torchvision import transforms

def main():

    device = "cuda" if cuda.is_available() else "cpu"
    train_dataset = datasets.MNIST(root='dataset/', train=True,
                                   transform=transforms.ToTensor(), download=True)
    test_dataset = datasets.MNIST(root='dataset/', train=False,
                                   transform=transforms.ToTensor(), download=True)
    train_loader = DataLoader(dataset=train_dataset, batch_size=64, shuffle=True)
    test_loader = DataLoader(dataset=test_dataset, batch_size=64, shuffle=True)
    
    model = RNN(input_size=28, hidden_size=256, num_layers=2, num_classes=10)
    criterion = nn.CrossEntropyLoss()
    optimizer = optim.Adam(model.parameters(), lr=1e-3)

    train_losses = train.train(model=model, dataloader=train_loader, epochs=2, optimizer=optimizer, loss_fn=criterion)
    utils.plot_xy(title="Loss over iterations", 
                  x=list(range(len(train_losses))), 
                  y=train_losses)
    
    # TODO: Save checkpoint of the model for later use

if __name__ == "__main__":
    main()