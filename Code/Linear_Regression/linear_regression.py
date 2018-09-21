import numpy as np
import copy

def F_X(W,X1):
    return np.dot(W.T,X1)
        
def mylinridgereg(X, Y, lamda=0.1):
    n=len(X)
    d=len(X[0])
    W=np.matmul(    np.matmul(  np.linalg.inv(    np.matmul(X.T,X)+lamda*np.identity(d)   ),X.T ),Y )
    return W

def mylinridgeregeval(X,W):
    return np.matmul(X,W)

def meansquarederr(T, Tdash):
    tmp=T-Tdash
    tmp=tmp[:,0]
    output=0
    n = len(tmp)
    for x in tmp:
        output=output+x**2
    return output/n
