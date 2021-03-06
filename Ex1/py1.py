import matplotlib.pyplot as plt
import numpy as np
from computecost import computecost
from graddesc import gradientdescent
from mpl_toolkits.mplot3d import Axes3D
np.seterr(divide='ignore', invalid='ignore')
f=open('ex1data2.txt','r')
a=f.readlines()
x=[]
y=[]
j=0

#################################Splitting of data into x and y######################

for i in a:
	u=i.split(',')
	x.append(u[:1])
	y.append(u[1:2])
print ("x: \n",x)
print ("y: \n",y)

#################################Plotting of data##################################
plt.figure(1)
plt.subplot(x,y,'rx',10)
#plt.axis([500,4500,50000,300000])
plt.show()
m=len(x)
#print(x)

################################Cost functions####################################
X=np.column_stack((np.ones((m,1)),x))
#print(X)
theta=np.zeros((2,1))
#print(theta)on
iterations=1500
alpha=0.01
#print(X)
X=np.array(X,np.float)
y=np.array(y,np.float)
theta=np.array(theta,np.float)
ans=computecost(X,y,theta)
print('The computed cost is:')
print(ans)

################################Gradient Descent###################################
theta=gradientdescent(X,y,theta,alpha,iterations)
plt.subplot(X[:,1:2],np.dot(X,theta),'-')
plt.show()
predict1=np.asarray([1,3.5])*theta
predict2=np.asarray([1,7])*theta
print('Predicting...')
print(predict1,predict2)
theta0_vals=np.linspace(-10,10,num=100)
theta1_vals=np.linspace(-1,4,num=100)
J_vals=np.zeros((len(theta0_vals),len(theta1_vals)))

for i in range(0,len(theta0_vals)-1):
	for j in range(0,len(theta1_vals)-1):
		t=[theta0_vals[i],theta1_vals[j]]
		J_vals[i,j]=computecost(X,y,t)

J_vals=np.matrix.transpose(J_vals)
J_vals=np.array(J_vals).reshape(len(theta0_vals),len(theta1_vals))
#print(np.shape(theta0_vals),np.shape(theta1_vals),np.shape(J_vals))
fig = plt.figure()
Axes3D = fig.add_subplot(111, projection='3d')
#Axes3D.plot_surface(theta0_vals, theta1_vals, J_vals)		
#plt.contour(theta0_vals,theta1_vals,J_vals,np.logspace(-2,3,num=20))
#plt.plot(theta[0],theta[1],'ro')
#plt.show()
