import torch
import torchvision

model = torchvision.models.resnet18(pretrained=True)
model = model.eval()

traced_model = torch.jit.trace(model, torch.rand(1, 3, 224, 224))
traced_model.save("pretrained_resnet18.pt")
