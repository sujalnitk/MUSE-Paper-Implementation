import torch
import torch.nn as nn
import torch.optim as optim 
import numpy 

class Discriminator(nn.Module):

  def __init__(self , input_dim):
    super().__init__()
    self.model = nn.Sequential(
        nn.Linear(input_dim , 2048),
        nn.LeakyReLU(0.2),
        nn.Dropout(0.4),
        nn.Linear(2048 , 1),
        nn.Sigmoid()
    )

  def forward(self , x):
    return self.model(x)
  
