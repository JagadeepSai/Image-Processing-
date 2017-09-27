from matplotlib import pyplot as plt
import numpy as np
import sys
import cv2
import math

inp = str(sys.argv)
inp = str(sys.argv[1:])
inp=str(inp[2:-2])


A=cv2.imread(inp,cv2.IMREAD_GRAYSCALE)
Initial_Treshold=155
A_shape=A.shape
while 1:
	L=[0,0]
	R=[0,0]
	for i in list(range(A_shape[0])):
		for j in list(range(A_shape[1])):
			if A[i][j] > Initial_Treshold:
				L=[L[0]+A[i][j],L[1]+1]
			else:
				R=[R[0]+A[i][j],R[1]+1]
	New_Treshold=math.floor(0.5*(L[0]/L[1]+R[0]/R[1]))
	if (New_Treshold == Initial_Treshold):
		break
	else :
		Initial_Treshold=New_Treshold


MAP=lambda r: 255 if r > Initial_Treshold else 0
print(Initial_Treshold)
FUNC=np.vectorize(MAP)
ANS=FUNC(A)
plt.figure(frameon=False)
plt.set_cmap('hot')
plt.axis('off')
plt.imshow(ANS,cmap='gray')


plt.savefig('Out_1_Thresholding.png',bbox_inchs='tight')