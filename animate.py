'''
Ref: https://medium.com/swlh/how-to-convert-a-2d-movie-to-3d-d54ec5f9f233
Ref: stackoverflow with PIL: https://stackoverflow.com/questions/753190/programmatically-generate-video-or-animated-gif-in-python
'''

import os
from PIL import Image
import cv2
import imageio
'''
Input: dir: directory of images 
Output: .gif file --> Usage of PIL library --> conversion CV2 to PIL
needed. Image.fromarray() as well as colour conversion from cv2 BGR 
to PIL RGB
'''
def animate(dir, output):
    frames = []
    for img in os.listdir(dir):
        if img.lower().endswith('.jpg') or img.lower().endswith('.png'):
            new_frame = Image.open(os.path.join(dir, img))
            frames.append(new_frame)
    frames[0].save(output, format='GIF', append_images=frames[1:], save_all=True, duration=0, loop=0, fps=100)
    return None

'''
with Imageio
Input: list of imgs of type [left,output]
Output: name of .gif file
'''

def img_list2_animate(animate_list,output):
    frames = []
    for cv2_imgs in animate_list:

        pil_image = Image.fromarray(cv2_imgs) #convert to PIL Image
        frames.append(pil_image)
    frames[0].save(output,format= 'GIF',append_images= frames[1:], save_all=True,loop=0, fps= 100)
    return None

def create_gif(output_Path,animate_list):
    frames = []
    #Create color conversion from BGR to RGB
    for cv2_imgs in animate_list:
        frames.append(cv2.cvtColor(cv2_imgs,cv2.COLOR_BGR2RGB))
    imageio.mimsave(output_Path,frames)
    return None

'''
if __name__ == '__main__':
    dir = 'results/animate/output/movie'
    output = 'results/animate/output/movie/output.gif'
    animate(dir, output)
    output_path ='results/animate/output/movie/output.gif'
    create_gif(input_path,output_path)
'''
#TODO: check for handling of large files --> Kafka
#TODO; avoid copying files for transfer between cv2 to PIL format. Find a diffeent solution
#TODO: write functions to append