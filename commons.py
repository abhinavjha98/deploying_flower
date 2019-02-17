import io
import torch
import torch.nn as nn
from torchvision import models
from PIL import Image
import torchvision.transforms as transforms

def get_model():
	checkpoint = 'checkpoints.pth'
	model = models.vgg19(pretrained=True);
	model.classifier = nn.Linear(500,102)
	model.load_state_dict(torch.load(checkpoint,map_location='cpu'),strict=False)
	#cc = torch.load(checkpoint, torch.cuda.device('cpu'))
	#model.load_state_dict(cc['state_dict'])
	model.eval()
	return model

def get_tensor(image_bytes):
	my_transforms = transforms.Compose([transforms.Resize(255),
		transforms.CenterCrop(224),
		transforms.ToTensor(),
		transforms.Normalize(
			[0.485,0.456,0.406],
			[0.229,0.224,0.225])])
	image = Image.open(io.BytesIO(image_bytes))
	return my_transforms(image).unsqueeze(0)