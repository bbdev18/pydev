# -*- coding: utf-8 -*-
"""
Created on Thu Oct 21 14:14:21 2021

@author: BBarsch
"""

import matplotlib.pyplot as plt
import numpy as np
import csv
import time

# start = time.time()


x_data = np.loadtxt("data.csv", delimiter=',')

avergval = 0
avg = 10


# for i in x_data:
#     print(i)
    
numbers = [1, 2, 3, 7, 9]

window_size = 3


i = 0

data_list = x_data.tolist()

numbers = data_list

moving_averages = []


    
while i < len(numbers) - window_size + 1:

    this_window = numbers[i : i + window_size]

    window_average = sum(this_window) / window_size

    moving_averages.append(window_average)

    i += 1


# print(moving_averages)

plt.plot(x_data[0:100])
plt.plot(moving_averages[0:100])
plt.show()

