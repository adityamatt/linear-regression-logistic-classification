import numpy as np
import statistics as stat
import random
import pickle
import matplotlib.pyplot as plt 

#A function to get the dataset of NX(d+1) dimension in matrix form
def get_data_set(input_location):
    with open (input_location) as dic:
        content=dic.readlines()
    content = [x.strip() for x in content]
    output=list()
    output_Y=list()
    for x in content:
        tmp_list=list()
        tmp_list.append(1)
        x=x.split(",")
        if (x[0]=="F"):
            tmp_list.append(1)
            tmp_list.append(0)
            tmp_list.append(0)
        elif x[0]=="M":
            tmp_list.append(0)
            tmp_list.append(1)
            tmp_list.append(0)
        else:
            tmp_list.append(0)
            tmp_list.append(0)
            tmp_list.append(1)
        for di in x[1:-1]:
            tmp_list.append(float(di))
        output.append(tmp_list)
        output_Y.append([int(x[-1])])
    
    output=np.array(output)
    output_Y=np.array(output_Y)
    
    return output,output_Y

#A functio to standardize a column of dataset with given mean and standard deviation
def standardize(dataset,column,mean,std):
    for x in dataset:
        x[column]=(x[column]-mean)/std

#A function to find the mean of a column of a matrix
def mean_std(dataset,column):
    tmp=dataset[:,column]
    return stat.mean(tmp),stat.stdev(tmp)

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

#A function to save variables to given location
def save(X,Y,file_location):
    with open(file_location, 'w') as f:
        pickle.dump(X,f)
        pickle.dump(Y,f)

#A function to laod variables from given location
def load(file_location):
    with open(file_location, 'r') as f:
        X=pickle.load(f)
        Y=pickle.load(f)
    return X,Y
def save_variable(X,file_name):
    with open(file_name,'w') as f:
        pickle.dump(X,f)
        
def load_variable(file_name):
    with open(file_name,'r') as f:
        X=pickle.load(f)
    return X

def error(input_data):
    #Printed Error
    return [4.864,4.863,4.862,4.861,4.8605,4.860,4.8585,4.858]
