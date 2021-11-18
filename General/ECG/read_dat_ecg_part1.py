# -*- coding: utf-8 -*-
"""
Resources:
https://neurokit2.readthedocs.io/en/latest/examples/ecg_delineate.html
https://python-heart-rate-analysis-toolkit.readthedocs.io/en/latest/algorithmfunctioning.html#peak-detection

Smooth Data:
    https://www.delftstack.com/howto/python/smooth-data-in-python/
    
Find Peaks:
    https://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.find_peaks.html
    
Peak Detection:
    https://pythonawesome.com/overview-of-the-peaks-dectection-algorithms-available-in-python/
    https://plotly.com/python/peak-finding/
    https://peakutils.readthedocs.io/en/latest/
    
WFDB:
    https://github.com/MIT-LCP/wfdb-python

Dr Emlyn Clay - Analyzing the ElectroCardioGram (ECG)
https://www.youtube.com/watch?v=WyjGCEWU4zY
"""


import wfdb
import matplotlib.pyplot as plt
import numpy as np
import scipy.signal
from scipy.signal import find_peaks, peak_widths

signals, fields = wfdb.rdsamp("rec_1")

sig01 = []
sig02 = []
for i,val in enumerate(signals):
    sig01.append(signals[i,0])
    sig02.append(signals[i,1])
    
def smooth(y, box_pts):
    box = np.ones(box_pts)/box_pts
    y_smooth = np.convolve(y, box, mode='same')
    return y_smooth

smth = smooth(sig02,10)  

# R Peaks
indexes, maxes = scipy.signal.find_peaks(smth, height=0.35, distance=1)

# T Peaks:
mymax = list(maxes['peak_heights'])
fs = 500
mytime = list(indexes/fs)
myindexes = list(indexes)

segment = []

seg_upp = 200
seg_lower = 150


for i in range(len(mymax)):
    data = []    
 
    new_segment = smth[myindexes[i]-seg_lower:myindexes[i]+seg_upp]

    for j in range(len(new_segment)):
        data.append((new_segment[j]))
             
    segment.append(data)

for i in range(len(mymax)):
    seg_val = i
    plt.figure(seg_val)
    # R Peaks
    seg_index_r, seg_val_r = scipy.signal.find_peaks(segment[seg_val], height=0.35, distance=1)
    seg_val_r = list(seg_val_r['peak_heights'])
    seg_index_r = list(seg_index_r)
      
    #Plot
    
    plt.plot(segment[seg_val], label='seg1')
    plt.plot(seg_index_r,seg_val_r, 'x')
    plt.legend(["Segment"])
    plt.grid() 
    
    plt.title('Seg #: ' + str(seg_val))
    plt.title('Seg #: ' + str(seg_val) + ' R = '+str(round(seg_val_r[0],3)))
  

    plt.show()

