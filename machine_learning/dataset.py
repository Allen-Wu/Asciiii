'''
A wrapper for AsciiSketch.
'''

import os
# import psutil

from torchvision import transforms

import torch
from torch.utils.data.dataset import Dataset

PATH = "AsciiOri/"

class AsciiSketchDataset(Dataset):
    def __init__(self, split):
        assert split in ['train', 'valid']
        self.n = 130 if split == "train" else 20
        # path = os.path.dirname(os.path.realpath(__file__)) + '\AsciiSketch'
        filenames = os.listdir(PATH)
        self.nlabel = len(filenames)
        self.data = []
        for filename in filenames:
            temp = torch.load(os.path.join(PATH, filename))
            if split == "train":
                self.data += [temp[0:130]]
            else:
                self.data += [temp[130:150]]
        self.data = torch.cat(self.data, dim=0)
        mean = 0.1910
        # tensor(156.9250, dtype=torch.float64)
        # tensor(156.4212, dtype=torch.float64)
        self.transform = transforms.Compose([
            lambda x: (x - mean),
            lambda x: x.view(-1),  # Flatten
        ])

    def __len__(self):
        return self.nlabel * self.n

    def __getitem__(self, idx):
        label = idx % self.nlabel
        index = label * self.n + (idx//self.nlabel)

        sample = [self.transform(self.data[index]).float(), label]
        return sample
