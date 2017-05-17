#!/usr/bin/python
#Import data and functions from scikit-learn packets, import plotting function from matplotlib 
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn import svm 

#load the digits and asign it to digits
digits = datasets.load_digits()

#C-Support Vector Classification: svm.SVC 
#First parameter: gamma: usually one over the length of the trainning list
#Second parameter: Penalty parameter C of the error term.

clf = svm.SVC(gamma=0.0001, C=100)
print(len(digits.data))
#load trainning data sets to two vectors X and y
x,y = digits.data[:-10], digits.target[:-10]

#Apply the neural network to the data set 
clf.fit(x,y)

#print the prediction 
print('Prediction: ', clf.predict(digits.data[-5]))
#print the picture of the digit 
plt.imshow(digits.images[-5], cmap=plt.cm.gray_r, interpolation = "nearest")
#show the digit with matplotlib 
plt.show()