import statistics
import math
import numpy as np
from numpy import *
from matplotlib import pyplot as plt
import random
import pickle
from scipy import optimize

#A function to return dataset X and Y
def get_dataSet(input_training_location):
    with open (input_training_location) as dic:
        content=dic.readlines()
    content = [x.strip() for x in content]
    data_set=list()
    output=list()
    for line in content:
        tmp_list=list()
        tmp_list.append(1)
        line=line.split(",")
        tmp_list.append(float(line[0]))
        tmp_list.append(float(line[1]))
        data_set.append(tmp_list)
        output.append([int(line[2])])
    data_set=np.array(data_set)
    output=np.array(output)
    return data_set,output
#A function to return graph of Points
def draw_graph_points(X,Y):
    x1_positive=list()
    x2_positive=list()
    x1_negative=list()
    x2_negative=list()
    for i in range(len(X)):
        if Y[i]==1:
            x1_positive.append(X[i][1])
            x2_positive.append(X[i][2])
        else:
            x1_negative.append(X[i][1])
            x2_negative.append(X[i][2])
    plt.scatter(x1_positive,x2_positive,color='blue',label='positive class')
    plt.scatter(x1_negative,x2_negative,color='red' ,label='negative class')
    plt.title("Distribution of Two classes accross dataset")
    plt.xlabel("x1 Attribute")
    plt.ylabel("x2 Attribute")
    plt.legend() 
    return plt

    
#A function to generate count numbers between a and b:
def get_random(a,b,count):
    output=list()
    if (count>b-a+1):
        print "ERROR REQUEST for ",count,"Numbers between ",a," and ",b,"Returning Empty List"
        return output
    if (count<(b-a+1)/2):
        while (len(output)!=count):
            tmp = random.randint(a,b)
            if tmp not in output:
                output.append(tmp)
        output.sort()
        return output
    while (len(output)!=b-a+1-count):
        tmp = random.randint(a,b)
        if tmp not in output:
                output.append(tmp)
    new_output=list()
    for x in range(a,b+1):
        if x not in output:
            new_output.append(x)
    new_output.sort()
    return new_output
                

#A function to parition a dataset into training and test set
def partition(dataset,Y,percentage_test):
    training_set=list()
    training_Y=list()
    test_set=list()
    test_Y=list()
    n = len(dataset)
    select=round(percentage_test*n/100)
    selected=get_random(0,len(dataset)-1,select)
    for i in range(len(dataset)):
        if i in selected:
            training_set.append(dataset[i])
            training_Y.append([Y[i][0]])
        else:
            test_set.append(dataset[i])
            test_Y.append([Y[i][0]])
    training_set=np.array(training_set)
    training_Y=np.array(training_Y)
    test_set=np.array(test_set)
    test_Y=np.array(test_Y)
    return training_set,training_Y,test_set,test_Y
    

#A function to increase basis of X
def increase_basis(X,k):
    X_new=list()
    for x in X:
        tmp_list=list()
        x1=x[1]
        x2=x[2]
        for i in range(k+1):
            for j in range(k+1-i):
                tmp_list.append((x1**i)*(x2**j))
        X_new.append(tmp_list)
    X_new=np.array(X_new)
    return X_new
    
    
#A function to draw 2 attribute boundary
def draw_graph_boundary(plt,W,X,lbl,clr):
    W_new=np.squeeze(np.asarray(W))
    #W0+W1X1+W2X2=0
    for i in range(len(W_new)):
        W_new[i]=float(W_new[i])
        
    X1=list()
    X2=list()
    for x in X:
        X1.append(x[1])
    for x in X1:
        tmp=-(W_new[0]+W_new[1]*x)/W_new[2]
        X2.append(tmp)
    plt.plot(X1,X2,label=lbl,color=clr)

#A function to save two variable to a file
def save(X,Y,file_name):
    with open(file_name,'w') as f:
        pickle.dump([X,Y],f)

# A function to load two variables from a file
def load(file_name):
    with open(file_name,'r') as f:
        X,Y=pickle.load(f)
    return X,Y
#A function to draw linear boundary for 2 degree ONLY:
def plotboundary(W,plt):
    f=lambda x, y: (W[0,0]+W[1,0]*y+W[2,0]*y**2+W[3,0]*x+W[4,0]*x*y+W[5,0]*x**2)
    y_range=linspace(-1, 1, 100)
    x_range=[optimize.fmin(f,0,args=(y,), disp=0) for y in y_range]
    xr=linspace(-8,8)
    yr=linspace(-8,8)
    X, Y=meshgrid(xr, yr)
    Z=f(X, Y)
    plt.plot(x_range, y_range, 'k')
    return plt
