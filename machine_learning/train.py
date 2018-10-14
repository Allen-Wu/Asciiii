import torch
import os
from matplotlib import pyplot as plt
import numpy as np

from dataset import AsciiSketchDataset
from MLP import MultiLayerPerceptron

label_to = {0: ' ', 1: '~', 2: '<', 3: '.', 4: '(', 5: '_', 6: '/', 7: ')', 8: 'Y', 9: '-', 10: '#', 11: ':', 12: '=',
            13: '`', 14: 'T', 15: '+', 16: '\\', 17: '^', 18: '|', 19: '[', 20: '>', 21: ']', 22: 'V', 23: '"', 24: 'X',
            25: ','}


def train():
    train_dataset = AsciiSketchDataset("train")
    valid_dataset = AsciiSketchDataset("valid")
    train_data_loader = torch.utils.data.DataLoader(train_dataset, 128, shuffle=True, drop_last=False)
    valid_data_loader = torch.utils.data.DataLoader(valid_dataset, 128, shuffle=True, drop_last=False)

    model = MultiLayerPerceptron()
    optimizer = torch.optim.SGD(model.parameters(), lr=1)
    criterion = torch.nn.CrossEntropyLoss()
    lr_scheduler = torch.optim.lr_scheduler.StepLR(optimizer, step_size=10, gamma=0.2)
    for epoch in range(100):
        for inputs, target in train_data_loader:
            optimizer.zero_grad()
            output = model(inputs)
            loss = criterion(output.double(), target)

            loss.backward()
            optimizer.step()

            _, predict = torch.max(output, 1)
            num_data = torch.numel(predict)

            # print("train>>> lr:", lr_scheduler.get_lr()[0], "; loss:", loss.item(), "; acc:", acc)

        model.eval()
        torch.save({
            'model': model.state_dict(),
            'optimizer': optimizer.state_dict(),
            'lr_scheduler': lr_scheduler.state_dict()
        },
            os.path.join("save", 'checkpoint-{}.bin'.format(epoch))
        )

        acc = 0
        for data in valid_data_loader:
            inputs, target = data
            output = model(inputs)
            _, predict = torch.max(output, 1)
            acc += (predict == target).sum().item()

        acc /= len(valid_dataset)

        if epoch % 10 == 0:
            perm = torch.randperm(valid_dataset.__len__())
            idx = perm[:9]
            inputs, targets = valid_dataset[idx]
            inputs = inputs.view(9, -1)

            outputs = model(inputs)
            _, predict = torch.max(outputs, 1)

            for i in range(9):
                plt.subplot(3, 3, i+1)
                plt.imshow(inputs[i].reshape(16, 8), cmap=plt.cm.Greys)
                plt.title('target:{}. predict:{}.'.format(label_to[targets[i].item()], (label_to[predict[i].item()])))
                plt.xticks([])
                plt.yticks([])

            plt.show()

        # print("!!!!!!!!!!!!!!!!! VALID:", acc)

        model.train()

    idx = torch.tensor([i for i in range(26)])
    inputs, targets = valid_dataset[idx]
    inputs = inputs.view(26, -1)

    outputs = model(inputs)
    _, predict = torch.max(outputs, 1)

    for i in range(26):
        plt.imshow(inputs[i].reshape(16, 8), cmap=plt.cm.Greys)
        plt.title('target:{}. predict:{}.'.format(label_to[targets[i].item()], (label_to[predict[i].item()])))
        plt.xticks([])
        plt.yticks([])

        plt.savefig("model_cmp/{}.png".format(i))
        plt.close()


train()