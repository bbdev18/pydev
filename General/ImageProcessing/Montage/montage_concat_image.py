# import cv2 library
import cv2

# read the images
img1 = cv2.imread('video0_000.jpg',0)
img2 = cv2.imread('video0_001.jpg',0)
img3 = cv2.imread('video0_002.jpg',0)
img4 = cv2.imread('video0_003.jpg',0)
img5 = cv2.imread('video0_004.jpg',0)
img6 = cv2.imread('video0_005.jpg',0)
img7 = cv2.imread('video0_006.jpg',0)
img8 = cv2.imread('video0_007.jpg',0)
img9 = cv2.imread('video0_008.jpg',0)
img10 = cv2.imread('video0_009.jpg',0)
# img2 = cv2.imread('/video0/video0_001.jpg')

# cv2.imshow('image',img1)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# define a function for vertically 
# concatenating images of the 
# same size  and horizontally
def concat_vh(list_2d):
    
      # return final image
    return cv2.vconcat([cv2.hconcat(list_h) 
                        for list_h in list_2d])
# image resizing
img1_s = cv2.resize(img1, dsize = (0,0),
                    fx = 0.5, fy = 0.5)
img2_s = cv2.resize(img2, dsize = (0,0),
                    fx = 0.5, fy = 0.5)
img3_s = cv2.resize(img3, dsize = (0,0),
                    fx = 0.5, fy = 0.5)
img4_s = cv2.resize(img4, dsize = (0,0),
                    fx = 0.5, fy = 0.5)
img5_s = cv2.resize(img5, dsize = (0,0),
                    fx = 0.5, fy = 0.5)
img6_s = cv2.resize(img6, dsize = (0,0),
                    fx = 0.5, fy = 0.5)
img7_s = cv2.resize(img7, dsize = (0,0),
                    fx = 0.5, fy = 0.5)
img8_s = cv2.resize(img8, dsize = (0,0),
                    fx = 0.5, fy = 0.5)
img9_s = cv2.resize(img9, dsize = (0,0),
                    fx = 0.5, fy = 0.5)



  
# function calling
img_tile = concat_vh([[img1_s, img2_s, img3_s],
	[img4_s, img5_s, img6_s],
	[img7_s, img8_s, img9_s],     
                      
                      ])
# show the output image
cv2.imshow('video0_montage_subset.jpg', img_tile)
cv2.waitKey(0)
cv2.destroyAllWindows()
