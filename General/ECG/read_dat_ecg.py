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
segment_r = []
segment_p = []
segment_s = []

seg_upp = 200
seg_lower = 150
r_lower = 15
r_upper = 15
s_upper = 25
p_lower = 130
p_upper = 35


for i in range(len(mymax)):
    data = []    
    data_r = []
    data_p = []
    data_s = []
    new_segment = smth[myindexes[i]-seg_lower:myindexes[i]+seg_upp]
    r_peaks = smth[myindexes[i]-r_lower:myindexes[i]+r_upper]
    s_peaks = smth[myindexes[i]:myindexes[i]+s_upper]
    p_peaks = smth[myindexes[i]-p_lower:myindexes[i]-p_upper]
    for j in range(len(new_segment)):
        data.append((new_segment[j]))
        
    for j in range(len(r_peaks)):
        data_r.append(r_peaks[j])
        
    for j in range(len(p_peaks)):
        data_p.append(p_peaks[j])    
    
    for j in range(len(s_peaks)):
        data_s.append(s_peaks[j])  
            
    segment.append(data)
    segment_r.append(data_r)
    segment_p.append(data_p)
    segment_s.append(data_s)

for i in range(len(mymax)):
    seg_val = i
    plt.figure(seg_val)
    # R Peaks
    seg_index_r, seg_val_r = scipy.signal.find_peaks(segment[seg_val], height=0.35, distance=1)
    seg_val_r = list(seg_val_r['peak_heights'])
    seg_index_r = list(seg_index_r)
    
    # T Peaks:
    seg_index_t, seg_val_t = scipy.signal.find_peaks(segment[seg_val], height=(0.1,0.33), distance=1)
    seg_val_t = list(seg_val_t['peak_heights'])
    seg_index_t = list(seg_index_t)
    # if there is a duplicate value in the list corresponding to R, then locate T using:
    try:
        seg_val_t_max = max(seg_val_t)
        seg_val_t_max_index = segment[seg_val].index(seg_val_t_max)
        for i in range(len(segment[seg_val])):
            if segment[seg_val][i] == seg_val_t_max:
                seg_val_t_max_index = i
        
    except:
        seg_val_t_max = 1
        seg_val_t_max_index = 1
        print("error")
    
    # Q Peak
    peaks, _ = find_peaks(segment_r[seg_val])
    results_full = peak_widths(segment_r[seg_val], peaks, rel_height=1)
    # 150 - 15
    Q_i = results_full[2] + seg_lower - r_lower 
    Q_v = float(results_full[1])
    
    # S Peak
    segmin_s_val = min(segment_s[seg_val])
    segmin_s_index = segment[seg_val].index(segmin_s_val)
    
    # P Peak
    seg_index_p, seg_val_p = scipy.signal.find_peaks(segment_p[seg_val], height=(-0.1,0.15), distance=1)
    seg_val_s = list(seg_val_p['peak_heights'])
    seg_index_s = list(seg_index_p)
    seg_val_p_max = max(seg_val_s)
    seg_val_p_max_index = segment[seg_val].index(seg_val_p_max)
    
    #Plot
    
    plt.plot(segment[seg_val], label='seg1')
    plt.plot(seg_index_r,seg_val_r, 'x')
    plt.plot(seg_val_t_max_index,seg_val_t_max, '+')
    plt.plot(Q_i,Q_v, '*')
    plt.plot(segmin_s_index,segmin_s_val, 'o')
    plt.plot(seg_val_p_max_index,seg_val_p_max, '*')
    plt.legend(["Segment","R","T","Q","S","P"])
    plt.grid() 
    
    plt.title('Seg #: ' + str(seg_val) + ' P = '+str(round(seg_val_p_max,4))+', Q = '+str(round(Q_v,3))+', R = '+str(round(seg_val_r[0],3))+', S = '+str(round(segmin_s_val,3))+', T= '+str(round(seg_val_t_max,4)))

    plt.show()

