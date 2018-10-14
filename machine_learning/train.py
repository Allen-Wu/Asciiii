import torch
import os

from dataset import AsciiSketchDataset
from MLP import MultiLayerPerceptron


def train():
    train_dataset = AsciiSketchDataset("train")
    valid_dataset = AsciiSketchDataset("valid")
    train_data_loader = torch.utils.data.DataLoader(train_dataset, 32, shuffle=True, drop_last=False)
    valid_data_loader = torch.utils.data.DataLoader(valid_dataset, 32, shuffle=True, drop_last=False)

    model = MultiLayerPerceptron()
    optimizer = torch.optim.SGD(model.parameters(), lr=1)
    criterion = torch.nn.CrossEntropyLoss()
    lr_scheduler = torch.optim.lr_scheduler.StepLR(optimizer, step_size=40, gamma=0.2)

    for epoch in range(100):
        for inputs, target in train_data_loader:
            optimizer.zero_grad()
            output = model(inputs)
            loss = criterion(output.double(), target)

            loss.backward()
            optimizer.step()

            _, predict = torch.max(output, 1)
            num_data = torch.numel(predict)
            acc = (predict == target).sum().item() / num_data

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

        print("!!!!!!!!!!!!!!!!! VALID:", acc)

        model.train()


train()