from matplotlib import pyplot as plt
import numpy as np
import cv2
import math
import sys
inp = str(sys.argv)
inp = str(sys.argv[1:])
inp=str(inp[2:-2])

A=cv2.imread(inp,cv2.IMREAD_GRAYSCALE)
sigma=3
A_shape=A.shape
def Gau(x,y,s):
	return (1/(s*math.sqrt(2*math.pi)))*math.exp((x**2+y**2)/(-2*(s**2)))
a1=Gau(-1,-1,sigma)
a2=Gau(0,-1,sigma)
a3=Gau(1,-1,sigma)

a4=Gau(-1,0,sigma)
a5=Gau(0,0,sigma)
a6=Gau(1,0,sigma)

a7=Gau(-1,1,sigma)
a8=Gau(0,1,sigma)
a9=Gau(1,1,sigma)

sum=a1+a2+a3+a4+a5+a6+a7+a8+a9

a1=a1/sum
a2=a2/sum
a3=a3/sum
a4=a4/sum
a5=a5/sum
a6=a6/sum
a7=a7/sum
a8=a8/sum
a9=a9/sum

final=np.zeros(A_shape)


for i in list(range(A_shape[0]-1)):
	for j in list(range(A_shape[1]-1)):
		if(i==0 or j==0 ) :
			continue
		else :
			final[i][j]=A[i-1][j-1]*a1+A[i][j-1]*a2+A[i+1][j-1]*a3 \
			+ A[i-1][j]*a4+A[i][j]*a5+A[i+1][j]*a6 \
			+ A[i-1][j+1]*a7+A[i][j+1]*a8+A[i+1][j+1]*a9




plt.figure(frameon=False)
plt.set_cmap('hot')
plt.axis('off')
plt.imshow(final,cmap='gray')


plt.savefig('Out_1_gausian_blur.png',bbox_inchs='tight')