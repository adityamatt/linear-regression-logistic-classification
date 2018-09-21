import matplotlib.pyplot as plt
import statistics as stat
import pickle

execfile("variables.py")
execfile("utility.py")
execfile("linear_regression.py")
#X,Y=get_data_set(input_training_location_linear)
#training,training_Y,test,test_Y=partition(X,Y,80)
#save(training,training_Y,training_data)
#save(test,test_Y,test_data)

test,test_Y=load(test_data)

training,training_Y=load(training_data)

lamda=[0.0,0.1, 0.4, 0.7, 1.0, 1.3, 1.6, 1.9, 2.2, 2.5, 2.8]
fraction=[0.03, 0.05, 0.08, 0.1, 0.15, 0.2, 0.5,1.0]

#Script to create graph variables and save them, takes around 45 min

#num_lamda=len(lamda)
#num_fraction=len(fraction)
#graph_counter=1;
#for f in fraction:
#    print "Fraction value",f
#    training_mse_avg=list()
#    test_mse_avg=list()
#    for l in lamda:
#        training_mse=list()
#        test_mse=list()
#        for i in range(100):
#            training1,training_Y1,validation,validation_Y=partition(training,training_Y,f*100)
#            for j in range(1,len(training[0])):
#                mean,std=mean_std(training,j)
#                standardize(training,j,mean,std)
#                standardize(test,j,mean,std)
#            W=mylinridgereg(training,training_Y,l)
#            training_mse.append(meansquarederr(mylinridgeregeval(training,W),training_Y))
#            test_mse.append(meansquarederr(mylinridgeregeval(test,W),test_Y))
#        training_mse_avg.append(stat.mean(training_mse))
#        test_mse_avg.append(stat.mean(test_mse))
#    plt.subplot(4,2,graph_counter)
#    plt.plot(lamda,training_mse_avg,color='red',marker='X',label='Training')
#    plt.plot(lamda,test_mse_avg,color='green',marker='o',label='Test')
#    plt.xlabel("Lambda values")
#    plt.ylabel("Mean Square Error")
#    plt.title("Fraction value="+str(f))
#    plt.legend()
#    graph_counter=graph_counter+1
#    save_variable(training_mse_avg,"./variables/training_mse_f"+str(f)+".txt")
#    save_variable(test_mse_avg,"./variables/test_mse_f"+str(f)+".txt")
#plt.show()
            
 
###Script to load the graph variables and plot the graph for different f for varying Lamda

plt.subplots_adjust( wspace=0.5, hspace=0.5)
graph_counter=1;
for f in fraction:
    training_file_name="./variables/training_mse_f"+str(f)+".txt"
    test_file_name="./variables/test_mse_f"+str(f)+".txt"
    training_mse_avg=load_variable(training_file_name)
    training_mse_avg=load_variable(training_file_name)
    test_mse_avg=load_variable(test_file_name)
    plt.plot(lamda,training_mse_avg,color='red',marker='X',label='Training')
    plt.plot(lamda,test_mse_avg,color='green',marker='o',label='Test')
    plt.xlabel("Lambda values")
    plt.ylabel("Mean Square Error")
    plt.title("Fraction value="+str(f))
    plt.legend()
    graph_counter=graph_counter+1
    plt.show()
    plt.figure()


###Script to load the graph variables and plot minimum average mean squared testing error versus the training set fraction values.
#minimum_training_error=list()
#minimum_labda_values=list()
#for f in fraction:
#    training_file_name="./variables/training_mse_f"+str(f)+".txt"
#    training_mse_avg=load_variable(training_file_name)
#    l=lamda[0]
#    min_error=training_mse_avg[0]
#    for i in range(len(training_mse_avg)):
#        if training_mse_avg[i]<=min_error:
#            min_error=training_mse_avg[i]
#            l=lamda[i]
#    minimum_training_error.append(min_error)
#    minimum_labda_values.append(l)
#    minimum_training_error=error(minimum_training_error)
#plt.ylim((min(minimum_training_error), max(minimum_training_error)))
#plt.plot(fraction,minimum_training_error,marker='x')
#plt.xlabel('Fraction values')
#plt.ylabel('minimum  avg training MSE error')
#plt.legend()
#plt.show()


##Modelling using best lamda and fraction
##CHoosing lamda on a hunch that dataset is very sensitive to penalizing

###Script to load the create predicted vs actual in training
#lamda=0.000001
#f=1
#training1,training_Y1,validation,validation_Y=partition(training,training_Y,f*100)
#for j in range(1,len(training[0])):
#    mean,std=mean_std(training,j)
#    standardize(training,j,mean,std)
#    standardize(test,j,mean,std)
#W=mylinridgereg(training,training_Y,lamda)
#plt.figure()
#predicted=np.matmul(training,W)
#output=training_Y.T
#output=output[0]
#predicted=predicted.T
#predicted=predicted[0]
#plt.ylim(0, 30)
#plt.xlim(0, 30)
#plt.scatter(output,predicted,color='red')
#plt.xlabel("Actual Output Values")
#plt.ylabel("Predited Values")
#plt.title("Predicted Values vs Actual Values for Training Set")
#plt.show()

####Script to load the create predicted vs actual in test
#lamda=0.000001
#f=1
#training1,training_Y1,validation,validation_Y=partition(training,training_Y,f*100)
#for j in range(1,len(training[0])):
#    mean,std=mean_std(training,j)
#    standardize(training,j,mean,std)
#    standardize(test,j,mean,std)
#W=mylinridgereg(training,training_Y,lamda)
#plt.figure()
#predicted=np.matmul(test,W)
#output=test_Y.T
#output=output[0]
#predicted=predicted.T
#predicted=predicted[0]
#plt.ylim(0, 30)
#plt.xlim(0, 30)
#plt.scatter(output,predicted,color='green')
#plt.xlabel("Actual Output Values")
#plt.ylabel("Predited Values")
#plt.title("Predicted Values vs Actual Values for Test Set")
#plt.show()
