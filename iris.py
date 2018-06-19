 #! /usr/bin/python3
import os
import numpy
from sklearn import tree
from sklearn import datasets
from sklearn.datasets import load_iris

iris=load_iris()
dir(iris)
print(iris.target_names)
#print(iris.target)
#print(iris.data)
print(iris.feature_names)
#storing the data of setosa in the variabble
setosa=iris.data[0:50]
print(setosa)
#storing the value of target into s_sata
s_data=iris.target[0:50]
print(s_data)
#printing the size of data of setosa
print(s_data.size)
x=[0,50,100]
#separating the data to train and data to test by deleting the [0,50,100] elements from the data
only_target_training=numpy.delete(iris.target,x)
only_data_training=numpy.delete(iris.data,x,axis=0)
print(only_target_training)
print(only_target_training.size)
#data to test
test_target=iris.target[x]
print(test_target)
test_data=iris.data[x]
print(test_data)
#calling algo....training the system
algo=tree.DecisionTreeClassifier()
algo_trained=algo.fit(only_data_training,only_target_training)
#testing
output=algo_trained.predict(test_data)
#output
print(output)
