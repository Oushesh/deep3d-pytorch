'''
Ref: https://medium.com/swlh/how-to-convert-a-2d-movie-to-3d-d54ec5f9f233
1. Most movies contain a 3D layer.
2. We extract frames sequentially, even for left, odd for right
3. This method can be used to build dataset for the project in the future.
'''

import os
import cv2
from PIL import Image

def movie2leftright(dir,category):
    output = 'output/movie'
    for filename in os.listdir(os.path.join(dir,category)):
        videocap = cv2.VideoCapture(os.path.join(os.path.join(dir,category),filename))
        state, image = videocap.read()
        count = 0
        while state:
            if count%200000==0:
                left = image[:image.shape[0]//2,:,:][:,:,::-1]
                left = Image.fromarray(left)
                left.resize((left.size[0], left.size[1] * 2)).save(os.path.join(os.path.join(dir,output),'movie')+ filename + str(count) + '_left' + '.jpg')

                right = image[image.shape[0]//2:,:,:][:,:,::-1]

                right = Image.fromarray(right)
                right.resize((right.size[0], right.size[1] * 2)).save(os.path.join(os.path.join(dir,output),'movie')+ filename + str(count) + '_right' + '.jpg')
                count+=200000
        return None

if __name__ == '__main__':
    dir = 'results/animate'
    category = 'input/movie'
    movie2leftright(dir,category)

