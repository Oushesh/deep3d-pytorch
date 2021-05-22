'''
TODO: import conversion of movie to frames --> movie2Left_right
      import eval.py --> Neural Network depth and right equivalent image generation
      import animate.py --> ovelay both output to get the 3D videos.
'''

from utils import *
from eval import eval_output
import animate
def main():
    config_dir = r'config.yaml'
    configs = parse_config(config_dir)
    eval_output(configs)
    animate()
    return None
if __name__ == '__main__':
    main()