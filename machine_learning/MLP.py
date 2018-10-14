import torch
from torch import nn
from collections import OrderedDict


class _print(nn.Module):
    def __init__(self):
        super(_print, self).__init__()

    @staticmethod
    def forward(x):
        print(x.shape)
        return x


class MultiLayerPerceptron(nn.Sequential):
    def __init__(self):
        all_layers = OrderedDict()

        n_ins = [128, 256, 256, 256, 104]
        n_outs = [256, 256, 256, 104, 26]

        for i in range(len(n_ins)):
            all_layers['block' + str(i)] = self.get_block(n_ins[i], n_outs[i])

        super().__init__(all_layers)

    def get_block(self, n_in, n_out):
        return nn.Sequential(
            nn.BatchNorm1d(n_in, eps=1e-07, affine=True), nn.ReLU(), nn.Linear(n_in, n_out)
        )
