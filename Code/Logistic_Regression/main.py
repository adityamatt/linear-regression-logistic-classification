execfile("variables.py")
execfile("utility.py")
execfile("logistic_regression.py")  
     
X,Y=get_dataSet(input_training_location_logistic)
#training,training_Y,test,test_Y=partition(X,Y,20)
#save(training,training_Y,training_data)
#save(test,test_Y,test_data)
training,training_Y=load(training_data)
test,test_Y=load(test_data)

W1=iterativeLogistic(training,training_Y)
print "Accuracy of Gradient Descent is",accuracy(W1,test,test_Y)

W2=newtonRaphson(training,training_Y)
print "Accuracy of Newton Raphson is",accuracy(W2,test,test_Y)


plt=draw_graph_points(X,Y)
draw_graph_boundary(plt,W1,X,"Gradient Descent Boundary","green")
draw_graph_boundary(plt,W2,X,"Newton Raphson","yellow")
plt.legend()
plt.show()


#order=6

#X_basis_training=increase_basis(training,order)
#X_basis_test=increase_basis(test,order)


#W1=iterativeLogistic(X_basis_training,training_Y)
#W2=newtonRaphson(X_basis_training,training_Y)

#print "Accuracy of Gradient Descent is",accuracy(W2,X_basis_test,test_Y)
#print "Accuracy of Newton Raphson is",accuracy(W1,X_basis_test,test_Y)

#plotboundary(W2)
#plt=plotboundary(W2,plt)
#plt=plotboundary(W1,plt)
#plt.show()
##W2=newtonRaphson(X_basis,Y,num_iteration,lamda)
##print W2
##for w in W2:
##    print w
##print "\n"
##print accuracy(W1,X_basis,Y)
##print W

