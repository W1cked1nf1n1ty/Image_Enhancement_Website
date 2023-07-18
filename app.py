import sys
import cv2
import matplotlib.pyplot as plt
import array as arr
import numpy as np
import matplotlib.image as mpimg

imgdestination=sys.argv[1]
# img = mpimg.imread('./uploads/Screenshot (6).png')
img = cv2.imread(imgdestination)

def v_flip(a):
    w, h, c = a.shape
    p=a.copy()
    # plt.imshow(a)
    # plt.show()
    for x in range(w-1):
        for y in range(h-1):
          for k in range(c):
            p[x,y]=a[w-x-1,y]
    # plt.imshow(p)
    # plt.show()
    cv2.imwrite('./static/content/imgv_flip.png',p)
    


def h_flip(a):
    w, h, c = a.shape # Get the width, height and channels of the image array
    p=a.copy()
    # plt.imshow(a)
    # plt.show()
    for x in range(w-1):
        for y in range(h-1):
          for k in range(c):
            p[x,y]=a[x,h-y-1]
    # plt.imshow(p)
    # plt.show()
    cv2.imwrite('./static/content/imgh_flip.png',p)
    


def invert(a):
    w, h, c = a.shape
    op=a.copy()
    # plt.imshow(a)
    # plt.show()
    op = 255 -a
    # plt.imshow(op)
    # plt.show()
    cv2.imwrite('./static/content/imginvert.png',op)


def log(a):
  # plt.imshow(a)
  # plt.show()
  c = 255/(np.log(1 + np.max(a))) #SCALING FACTOR
  op = np.zeros_like(a) #create an empty array with the same shape as a
  for i in range(3): #loop over the RGB channels
    op[:,:,i] = c * np.log(1 + a[:,:,i]) #apply the log transformation to each channel
  # plt.imshow(op)
  # plt.show()
  cv2.imwrite('./static/content/imglog.png',op)


def gamma(a):
  # plt.imshow(a)
  # plt.show()
  for gamma in [0.1, 0.5, 0.798, 1.2, 2.2]:
    op = np.zeros_like(a) #create a new output array for each gamma
    for i in range(3): #loop over the RGB channels
      op[:,:,i] = np.array(255*(a[:,:,i] / 255) ** gamma, dtype = 'uint8') #apply the gamma transformation to each channel
  # plt.imshow(op) #plot the output image
  # plt.show() #show the plot
  cv2.imwrite('./static/content/imggamma.png',op)


# def brighten(a, scale):
#   # plt.imshow(a)
#   # plt.show()
#   op = a.copy()
#   w, h, c = a.shape # Get the width, height and channels of the image array
#   for i in range(w):
#     for j in range(h):
#       for k in range(c): # Loop over the RGB channels
#         op[i, j, k] = np.clip(a[i, j, k] + scale, 0, 255) # Add the scale and clip the values
#   # plt.imshow(op)
#   # plt.plot()
#   cv2.imwrite('./content/imgbrighten.png',op)

v_flip(img)
h_flip(img)
invert(img)
log(img)
gamma(img)
# brighten(img,0.66)








