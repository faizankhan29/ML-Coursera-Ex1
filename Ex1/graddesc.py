import numpy as np
import math
from computecost import computecost
def gradientdescent(X,y,theta,alpha,numiters):
	m=len(y)
	J_hist=np.zeros((numiters,1))
	for iter1 in range(0,numiters):
		temp0=0
		temp1=0
		for i in range(0,m):
			temp0=temp0+(theta * X[i,1:]-y[i])
			temp1=temp1+(theta * X[i,1:]-y[i])*X[i,1:2]
		theta[0]=theta[0] - ((alpha/m)*temp0[0])
		#print("theta0:",theta[0])
		theta[1]=theta[1] - ((alpha/m)*temp1[1])
		#print("theta1:",theta[1])
		J_hist=computecost(X,y,theta)[iter1]
		#print(J_hist)
		return(theta[0],theta[1])
