import torch
import torchvision

from PIL import Image
from torchvision.transforms import Compose, ToTensor, Normalize, Resize

img = Image.open("dog-12.jpg")
tfs = Compose([Resize(224), ToTensor(), Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])])
x = tfs(img).reshape(1, 3, 224, 224)

loaded_model = torch.jit.load("pretrained_resnet18.pt")
y = loaded_model(x)
print(torch.max(y, dim=1)[1].item())
