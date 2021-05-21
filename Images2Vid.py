'''
Usually the name of the img_dir will tell you
the title/context of the images. Thus,
the video output will bear the same name.
Input: img_dir: directory conatining images
Output: converted video from list of images
'''
import cv2
import os

def make_video(img_dir):
    all_imgs = os.listdir(img_dir)
    all_imgs.sort(key=lambda x: int(x[:x.find('.')]))
    imgs_for_video = []
    for img in all_imgs:
        img = cv2.imread(os.path.join(img_dir, img))
        height, width, layers = img.shape
        size = (width, height)
        imgs_for_video.append(img)

    fourcc = cv2.VideoWriter_fourcc(*'MP4V')  # Be sure to use lower case
    out = cv2.VideoWriter('output.avi', fourcc, 10.0, (width, height)) #TODO: change the output name based on context.

    for i in range(len(imgs_for_video)):
        print(i)
        out.write(imgs_for_video[i])
    out.release()
    return None


if __name__ == "__main__":
    img_dir =
    make_video(img_dir)