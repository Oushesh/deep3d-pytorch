'''
TODO: import conversion of movie to frames --> movie2Left_right
      import eval.py --> Neural Network depth and right equivalent image generation
      import animate.py --> ovelay both output to get the 3D videos.
'''

from utils import *
from eval import eval_output
from animate import *

def main():
    config_dir = r'config.yaml'
    configs = parse_config(config_dir)
    animate_list = eval_output(configs)
    print ('length of animate list',len(animate_list))
    output = 'test.gif'
    img_list2_animate(animate_list,output)
    print ('Successfully created GIF')
    return None

if __name__ == '__main__':
    main()

#TODO: tested the main functionality, dataloader checking for left and right number of images
