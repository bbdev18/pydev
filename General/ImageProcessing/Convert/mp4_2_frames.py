'''
Ref
https://theailearner.com/2018/10/15/extracting-and-saving-video-frames-using-opencv-python/
'''
import cv2
 
# Opens the Video file

cap= cv2.VideoCapture('D:/vid/video0.mp4')
i=100
while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == False:
        break
    cv2.imwrite('D:/vidout/frame0_'+str(i)+'.jpg',frame)
    i+=1
 
cap.release()
cv2.destroyAllWindows()
