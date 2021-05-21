import cv2
import torch
from model import *
from dataloader import *
from utils import *

'''
In any doubt consult: config.yaml for the parameters.
eval_output --> 
Input: configs as input
Ouput: written generated right stereo file from Neural Network
'''

def eval_output(configs):
    if not os.path.exists(configs['RES_DIR']):
        os.makedirs(configs['RES_DIR'])

    device = torch.device(configs['device'])

    if configs['device']== 'cpu':
        model = Deep3d(device=device).to(device)
        model.load_state_dict(torch.load(configs['weight_file'], map_location=device))
    elif configs['device']=='gpu':
        model = Deep3d(device=device).to(device)
        model.load_state_dict(torch.load(configs['weight_file']))

    test_dataset = MyDataset(configs['dataroot'], in_transforms=None)
    test_dataloader = torch.utils.data.DataLoader(test_dataset, batch_size=configs['batch'], shuffle=False)
    model.eval()

    # Loop over Dataloader and Inference
    for i, data in enumerate(test_dataloader):
        with torch.no_grad():
            left_orig = data[0].to(device).float()
            left = data[1].to(device).float()
            # right = data[2].to(device).float()
            output = model(left)
            # Reshape to 3D Tensor.
            left_orig = Tensor2img(left_orig[0, :, :, :])
            left = Tensor2img(left[0, :, :, :])
            # right = Tensor2img(right[0,:,:,:])
            output = Tensor2img(output[0, :, :, :])

            cv2.imwrite(configs['RES_DIR'] + str(i) + '_right_generated.png', output)
            cv2.imwrite(configs['RES_DIR'] + str(i) + '_left.png', left)
            # cv2.imwrite(configs['RES_DIR'] + str(i) + '_right.png', right)
    return None

if __name__ == '__main__':
    config_dir = r'config.yaml'
    configs = parse_config(config_dir)
    eval_output(configs)