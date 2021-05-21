'''
This file contains utitlity functions
needed for computation.
'''
import yaml

def parse_config(config_dir):
    with open(config_dir) as file:
        config_list = yaml.load(file,Loader=yaml.FullLoader)
    return config_list

def Tensor2img(tensor):
    tensor = tensor.cpu().permute([1,-1,0]).numpy()*255.0
    return tensor


