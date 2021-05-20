'''
Ref: https://medium.com/swlh/how-to-convert-a-2d-movie-to-3d-d54ec5f9f233
Ref: stackoverflow with PIL: https://stackoverflow.com/questions/753190/programmatically-generate-video-or-animated-gif-in-python
'''

import os
from PIL import Image

import glob
import cv2
'''
Input: dir: directory of images 
Output: 
'''
def animate(dir, output):
    frames = []
    for img in os.listdir(dir):
        #if img.endswith('.jpg') or img.lower.endswith('.png'):
        # new_frame = cv2.imread(os.path.join(dir,img))
        new_frame = Image.open(os.path.join(dir, img))
        frames.append(new_frame)
    frames[0].save(output, format='GIF', append_images=frames[1:], save_all=True, duration=300, loop=100)

if __name__ == '__main__':
    dir = 'results/animate/output/movie'
    output = 'results/animate/output/movie/output.gif'
    animate(dir, output)

#Refactor here and then work it out
#TODO: Perform the stereoscopic test on small video scenes
#TODO: check for handling of large files