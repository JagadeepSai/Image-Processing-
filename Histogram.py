from matplotlib import pyplot as plt
import numpy as np
import sys
import cv2
from itertools import repeat
import math
inp = str(sys.argv)
inp = str(sys.argv[1:])
inp=str(inp[2:-2])


A=cv2.imread(inp,cv2.IMREAD_GRAYSCALE)

A_shape=A.shape;

a=np.amax(A)
b=np.amin(A)

His=list(repeat(0,a-b+1))

for i in list(range(A_shape[0])):
	for j in list(range(A_shape[1])):
		His[A[i][j]  -b]+=1

NormHis=map(lambda x: x/(A_shape[1]*A_shape[0]), His)


Cdf =  np.cumsum(list(NormHis))
Cdf= list(Cdf)

MAP=lambda r: math.floor(Cdf[r-b]*(b-a+1))
FUNC=np.vectorize(MAP)
ANS=FUNC(A)
plt.figure(frameon=False)
plt.set_cmap('hot')
plt.axis('off')
plt.imshow(ANS,cmap='gray')#,vmin=np.amin(ANS))


plt.savefig('Out_1_Histogram.png',bbox_inchs='tight')