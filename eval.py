import cv2
import torch

from torchvision.utils import make_grid, save_image
from torch.optim import lr_scheduler
from torchvision import datasets, models, transforms
from tensorboardX import SummaryWriter

from model import *
from dataloader import *

RES_DIR = 'results/'
if not os.path.exists(RES_DIR):
    os.makedirs(RES_DIR)

dataroot = 'data/test/'
weight_file = 'data/99_20_view_syn_weights_l1with_scheduler.pth'
batch = 1

#device = torch.device('cuda')
device = torch.device('cpu')
print(device)

#GPU
'''
model = Deep3d(device=device).to(device)
model.load_state_dict(torch.load(weight_file))
'''
model = Deep3d(device=device).to(device)
model.load_state_dict(torch.load(weight_file,map_location=device))

#Debugging
'''
for param_tensor in model.state_dict():
    print(param_tensor, "\t", model.state_dict()[param_tensor].size())
'''

test_dataset = MyDataset(dataroot, in_transforms = None)
test_dataloader = torch.utils.data.DataLoader(test_dataset, batch_size = batch, shuffle = False)
model.eval()

def Tensor2img(tensor):
    tensor = tensor.cpu().permute([1,-1,0]).numpy()*255.0
    return tensor

for i, data in enumerate(test_dataloader):
    with torch.no_grad():
        left_orig = data[0].to(device).float()
        left = data[1].to(device).float()
        right = data[2].to(device).float()
        output = model(left)
        #Reshape to 3D Tensor.
        left_orig = Tensor2img(left_orig[0,:,:,:])
        left = Tensor2img(left[0,:,:,:])
        #right = Tensor2img(right[0,:,:,:])
        output = Tensor2img(output[0,:,:,:])

        cv2.imwrite(RES_DIR + str(i) + '_output.png', output)
        cv2.imwrite(RES_DIR + str(i) + '_left.png', left)
        #cv2.imwrite(RES_DIR + str(i) + '_right.png', right)
