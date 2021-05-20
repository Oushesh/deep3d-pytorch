'''
Function serving between
img and pytorch tensor
By preference use cv2
Folder:
    - original: original image files
    - tensor: output pytorch tensors
'''


import os
import torch
import skimage.io as io
import cv2

def img2Tensor(dir):
    tensor_dir = os.path.join(dir,'tensor')
    for file in os.listdir(tensor_dir):
        img = io.imread(os.path.join(tensor_dir,file))
        tensor = img/255.0
        tensor = torch.from_numpy(tensor)
        tensor = tensor.permute([-1, 0, 1])
        tensor = tensor.float()
    return tensor

def Tensor2img(tensor,dir):
    converted_dir = os.path.join(dir,'converted')
    for file in os.listdir(converted_dir):
        tensor = tensor.permute([1,-1,0]).numpy()*255.0
        cv2.imwrite(os.path.join(converted_dir,file),tensor)
    return tensor

if __name__ == '__main__':
    dir = 'data/Tensor2Img/'
    tensor=img2Tensor(dir)
    output_img = Tensor2img(tensor,dir)
