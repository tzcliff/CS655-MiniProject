import torch
import torch.nn as nn
import numpy as np
import torch.nn.functional as F
import requests

from torchvision.models import resnet50
from torchvision import transforms
from PIL import Image
from torchvision.transforms.transforms import CenterCrop

class ImageRecognition():
    def __init__(self, inputPath):
        self.preprocess = transforms.Compose([
            transforms.Resize(256),
            transforms.CenterCrop(224),
            transforms.ToTensor(),
            transforms.Normalize(
                mean = [0.485, 0.456, 0.406],
                std = [0.229, 0.224, 0.225]
            )
        ])

        LABEL_JSON_URL = "https://s3.amazonaws.com/mlpipes/pytorch-quick-start/labels.json"
        labelDict = requests.get(LABEL_JSON_URL).json()
        self.labels = {int(k): v for k, v in labelDict.items()}

        self.model = self._getModel()
        self.input = self._loadImage(inputPath)
        self.softmax = nn.Softmax(dim = 1)  

    def _loadImage(self, path):
        img = Image.open(path)
        imgTensor = self.preprocess(img)
        imgTensor.unsqueeze_(0)

        return imgTensor

    def _getModel(self):
        return resnet50(pretrained = True).eval()

    def predict(self):
        """
        Predict the category (cat or dog) of the current image
        """
        out = self.model(self.input)
        pred = self.softmax(out)

        idx = torch.argmax(pred, dim = 1).item()
        category = self.labels[idx]
        score = pred[0, idx]

        result = "Top-1 predicted category: {} ({:.1f}%)".format(category, score * 100)

        return result

# Debug
for animal in ['cat', 'dog']:
    for i in range(4):
        path = "../data/{}{}.jpg".format(animal, i + 1)
        print(ImageRecognition(path).predict())
