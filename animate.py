'''
Ref: https://medium.com/swlh/how-to-convert-a-2d-movie-to-3d-d54ec5f9f233
Ref: stackoverflow with PIL: https://stackoverflow.com/questions/753190/programmatically-generate-video-or-animated-gif-in-python
'''

import os
from PIL import Image
import cv2
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
        print (cv2_imgs)
        #color_converted = cv2.cvtColor(cv2_imgs,cv2.COLOR_BGR2RGB)
        pil_image = Image.fromarray(cv2_imgs) #convert to PIL Image
        frames.append(pil_image)
    frames[0].save(output,format= 'GIF',append_images= frames[1:], save_all=True,loop=0, fps= 100)
    return None


def create_gif(inputPath, outputPath, delay, finalDelay, loop):
    # grab all image paths in the input directory
    imagePaths = sorted(list(paths.list_images(inputPath)))

    # remove the last image path in the list
    lastPath = imagePaths[-1]
    imagePaths = imagePaths[:-1]
    # construct the image magick 'convert' command that will be used
    # generate our output GIF, giving a larger delay to the final
    # frame (if so desired)
    cmd = "convert -delay {} {} -delay {} {} -loop {} {}".format(
        delay, " ".join(imagePaths), finalDelay, lastPath, loop,
        outputPath)
    os.system(cmd)

if __name__ == '__main__':
    '''
    dir = 'results/animate/output/movie'
    output = 'results/animate/output/movie/output.gif'
    animate(dir, output)
    '''
    input_path = 'results/animate/output/movie'
    create_gif()

#TODO: check for handling of large files --> Kafka
#TODO; avoid copying files for transfer between cv2 to PIL format. Find a diffeent solution