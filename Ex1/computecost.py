import math
import numpy as np

def computecost(X,y,theta):
	J=0
	m=len(y)
	y=np.asarray(y)
	for i in range(0,m):
		J=J+pow(np.transpose(theta) * np.transpose(X[i,1])-y[i],2)
	J=J/(2*m)
	return J[0]
