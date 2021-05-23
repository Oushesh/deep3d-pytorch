import os
import torch
import torch.utils.data as data
import cv2
from PIL import Image

'''
Use openCV avoid using skimage. 
cv2 is more optimised for large files.
'''

#TODO: In future: in_transforms can be used like with albumentations library to make online affine transformation before batching
class MyDataset(data.Dataset):
	def __init__(self, root, in_transforms=None, orig_size = (384, 1280),small_size=(96,320)):
		self.leftpath = os.path.join(root,'left')
		self.leftimg = os.listdir(self.leftpath)

		self.rightpath = os.path.join(root,'right')
		self.rightimg = os.listdir(self.rightpath)

		self.leftimg.sort()
		self.rightimg.sort()

		self.orig_size = orig_size
		self.small_size = small_size

	def __len__(self):
		return len(self.leftimg)

	def __getitem__(self, index):
		leftImage = cv2.imread(os.path.join(self.leftpath, self.leftimg[index]))

		leftImage_orig = cv2.resize(leftImage,self.orig_size)/255.0
		leftImage_small = cv2.resize(leftImage, self.small_size)/255.0

		#rightImage_orig = cv2.imread(os.path.join(self.rightpath, self.rightimg[index]))
		#rightImage_orig = cv2.resize(rightImage_orig, self.orig_size)/255.0

		left_orig = torch.from_numpy(leftImage_orig)
		left_orig = left_orig.permute([-1,1,0])

		left_small = torch.from_numpy(leftImage_small)
		left_small = left_small.permute([-1,1,0])

		#right_orig = torch.from_numpy(rightImage_orig)
		#right_orig = right_orig.permute([-1,1,0])

		#return left_orig, left_small, right_orig
		return left_orig,left_small







