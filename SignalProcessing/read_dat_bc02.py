# -*- coding: utf-8 -*-
"""
Created on Mon Oct 11 08:37:15 2021

@author: BBarsch
"""

# -*- coding: utf-8 -*-
"""
Created on Sun Oct 10 21:49:56 2021

@author: BBarsch

Resources:
https://neurokit2.readthedocs.io/en/latest/examples/ecg_delineate.html
https://python-heart-rate-analysis-toolkit.readthedocs.io/en/latest/algorithmfunctioning.html#peak-detection

Smooth Data:
    https://www.delftstack.com/howto/python/smooth-data-in-python/
"""


import wfdb
import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import savgol_filter
import scipy.signal
from scipy.signal import chirp, find_peaks, peak_widths

signals, fields = wfdb.rdsamp("rec_1")
print(len(signals[:]))

# x = np.linspace(0, 20,len(signals[:]))

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
# smth = smth * -1

# R Peaks
indexes, maxes = scipy.signal.find_peaks(smth, height=0.35, distance=1)

# T Peaks:
# indexes, maxes = scipy.signal.find_peaks(smth, height=(0.1,0.25), distance=1)

mymax = list(maxes['peak_heights'])
mytime = list(indexes/500)
myindexes = list(indexes)

segment = []
segment_r = []
segment_inv = []
segment_p = []


for i in range(len(mymax)):
    data = []    
    data_r = []
    data_inv = []
    data_p = []
    new_segment = smth[myindexes[i]-150:myindexes[i]+200]
    r_peaks = smth[myindexes[i]-15:myindexes[i]+15]
    p_peaks = smth[myindexes[i]-130:myindexes[i]-35]
    for j in range(len(new_segment)):
        data.append((new_segment[j]))
        data_inv.append((new_segment[j])*-1)
        
    for j in range(len(r_peaks)):
        data_r.append(r_peaks[j])
        
    for j in range(len(p_peaks)):
        data_p.append(p_peaks[j])        
            
    segment.append(data)
    segment_r.append(data_r)
    segment_inv.append(data_inv)
    segment_p.append(data_p)
    # plt.plot(segment_p[i], label='seg1')
    # plt.show()


seg_val = 23
# R Peaks
seg_index_r, seg_val_r = scipy.signal.find_peaks(segment[seg_val], height=0.35, distance=1)
seg_val_r = list(seg_val_r['peak_heights'])
seg_index_r = list(seg_index_r)

# T Peaks:
seg_index_t, seg_val_t = scipy.signal.find_peaks(segment[seg_val], height=(0.1,0.25), distance=1)
seg_val_t = list(seg_val_t['peak_heights'])
seg_index_t = list(seg_index_t)
try:
    seg_val_t_max = max(seg_val_t)
    seg_val_t_max_index = segment[seg_val].index(seg_val_t_max)
except:
    seg_val_t_max = 1
    seg_val_t_max_index = 1
    print("error")

# Q Peak
peaks, _ = find_peaks(segment_r[seg_val])
results_full = peak_widths(segment_r[seg_val], peaks, rel_height=1)
# 150 - 15
Q_i = results_full[2] + 135
Q_v = results_full[1]

# S Peak
seg_index_s, seg_val_s = scipy.signal.find_peaks(segment_inv[seg_val], height=(0.05), distance=1)
seg_val_s = list(seg_val_s['peak_heights'])
seg_index_s = list(seg_index_s)
seg_val_s_max = max(seg_val_s)
seg_val_s_max_index = segment_inv[seg_val].index(seg_val_s_max)
seg_val_s_max = seg_val_s_max*-1

# P Peak
seg_index_p, seg_val_p = scipy.signal.find_peaks(segment_p[seg_val], height=(-0.1,0.15), distance=1)
seg_val_s = list(seg_val_p['peak_heights'])
seg_index_s = list(seg_index_p)
seg_val_p_max = max(seg_val_s)
seg_val_p_max_index = segment[seg_val].index(seg_val_p_max)


plt.plot(segment[seg_val], label='seg1')
plt.plot(seg_index_r,seg_val_r, '*')
# plt.plot(seg_index_t,seg_val_t, '*')
plt.plot(seg_val_t_max_index,seg_val_t_max, '*')
plt.plot(Q_i,Q_v, '*')
plt.plot(seg_val_s_max_index,seg_val_s_max, '*')
plt.plot(seg_val_p_max_index,seg_val_p_max, '*')
plt.legend(["Segment","R","T","Q","S","P"])
plt.show()

# plt.hlines(*results_full[1:], color="C3")

# print(segment[1])





# plt.plot(sig01, label='linear')
# plt.plot(sig02, label='linear2')
# plt.plot(x, smth, label='linear3')
# plt.plot(smth, label='linear3')
# plt.plot(myindexes, mymax, '*')
