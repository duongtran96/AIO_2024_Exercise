import torch
import torch.nn as nn


class Softmax(nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x):
        x_exp = torch.exp(x)
        total = x_exp.sum(x_exp)
        return (x_exp / total)


class softmax_stable(nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x):
        x_max = torch.max(x, dim=0,  keepdims=True)
        x_exp = torch.exp(x - x_max.values)
        total = x_exp.sum(0, keepdims=True)
        return (x_exp / total)


class softmax_stable_2(nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x):
        x_exp = torch.exp(x - torch.max(x))
        return (x_exp / sum(x_exp))


# test
data = torch.tensor([1, 2, 3])
softmax = Softmax()
out = softmax(data)
print(out)
print("------------------------")
data = torch.tensor([1, 2, 3])
softmax_stable = softmax_stable()
out = softmax_stable(data)
print(out)
print("------------------------")
data = torch.tensor([1, 2, 3])
softmax_stable_2 = softmax_stable_2()
out = softmax_stable_2(data)
print(out)
