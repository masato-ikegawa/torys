import torch
import torch.nn as nn
from torch.utils.data import Dataset
from torchvision import datasets, transforms
import torch.nn.functional as F
import torch.optim as optim
import torchvision.utils as vutils
import torchvision

import numpy as np
import matplotlib.pyplot as plt

from model_mnist_gan import *

netD = Discriminator()
netG = Generator()

#学習結果を読み込んで、
netD.load_state_dict(torch.load('./netD.pth', map_location=lambda storage, loc: storage))
netG.load_state_dict(torch.load('./netG.pth', map_location=lambda storage, loc: storage))

#推論モードに設定（Dropout、BN、他の無効化）.to(device)は12/04追加。
netD.eval()
netG.eval()
