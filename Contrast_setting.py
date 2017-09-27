from matplotlib import pyplot as plt
import numpy as np
import sys, getopt
import cv2

inp = str(sys.argv[1:])
inp=str(inp[2:-2])


A=cv2.imread(inp,cv2.IMREAD_GRAYSCALE)


a=0
b=255
d=np.amax(A)
c=np.amin(A)
MAP=lambda r:(r-c)*(b-a)/(d-c)+a
FUNC=np.vectorize(MAP)
ANS=FUNC(A)
plt.figure(frameon=False)
plt.set_cmap('hot')
plt.axis('off')
plt.imshow(ANS,cmap='gray')


plt.savefig('Out_1_Contrast_setting.png',bbox_inchs='tight')