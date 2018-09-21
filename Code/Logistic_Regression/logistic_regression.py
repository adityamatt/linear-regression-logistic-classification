import numpy as np
from numpy.linalg import *

def sigmoid(x):
    return 1.0/(1+np.exp(-x))

def sigmoid_derivative(x):
    return x*(1-x)

def iterativeLogistic(dataset,Y,alpha=0.00001,l=1,max_iter=10000):
    W=list()
    n=len(dataset)
    d=len(dataset[0])
    for i in range(d):
        W.append([0.0])
    W=np.array(W)
    num=1
    while (num<=max_iter):
        gradient=np.matmul(dataset.T ,sigmoid( np.matmul(dataset,W) ) -Y )+l*W
        W=W-alpha*gradient
        num=num+1
    return W

def newtonRaphson(X,Y,max_iter=10000,l=30):
    W=list()
    n=len(X)
    d=len(X[0])
    for i in range(d):
        W.append([0.0])
    W=np.matrix(W)
    num=1
    while (num<=max_iter):
        num=num+1
        R=list()
        for x in X:
            WT=np.array(W.T)
            R.append(sigmoid_derivative(np.dot(WT[0],x)))
        R=np.diag(R)
        H=np.matmul(X.T,R)
        H=np.matmul(H,X)
        if det(H+l*np.eye(H.shape[0]))!=0:
            gradient=np.matmul(inv(H+l*np.eye(H.shape[0]) ) ,np.matmul( X.T, np.matmul(X,W) - Y ) )
        else:
            gradient=np.matmul(pinv(H+l*np.eye(H.shape[0]) ) ,np.matmul( X.T, np.matmul(X,W) - Y ) )
        W=W-gradient
    return W



def accuracy(W,X,Y):
    match=0.0
    output=sigmoid(np.matmul(X,W))
    output=np.where(output>=0.5,1,0)
    for i in range(len(Y)):
        if (Y[i]==output[i]):
            match=match+1
    return match*100/len(Y)
