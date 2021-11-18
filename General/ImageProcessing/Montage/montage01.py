# -*- coding: utf-8 -*-
"""
Created on Fri Nov  5 21:47:55 2021

Ref
https://note.nkmk.me/en/python-skimage-util-montage/
https://www.pyimagesearch.com/2017/05/29/montages-with-opencv/
"""

# import numpy as np

import skimage.util
import skimage.io 

import glob
import os

# print(os.getcwd())

image_list = []

for filename in glob.glob('D:/vidout/*'):
	# print(filename)
	img = skimage.io.imread(filename)
	image_list.append(img)


# a = skimage.io.imread('video0_000.jpg')

m = skimage.util.montage(image_list, multichannel=True)
skimage.io.imsave('output2.jpg',m)
# skimage.io.imshow(m)


# a = np.arange(1, 7).reshape(2, 3)
# print(a)
# # [[1 2 3]
# #  [4 5 6]]

# b = a * 10
# print(b)
# # [[10 20 30]
# #  [40 50 60]]

# c = a * 100
# print(c)
# # [[100 200 300]
# #  [400 500 600]]
# m = skimage.util.montage([a, b, c])
# print(m)
