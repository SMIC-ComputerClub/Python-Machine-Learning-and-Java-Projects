#!/usr/bin/python
#Import data and functions from scikit-learn packets, import plotting function from matplotlib 
from sklearn.neural_network import MLPClassifier 
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn import svm 

#load the digits and asign it to digits
digits = datasets.load_digits()

#Use MLPClassifier (provided by sci-kit learn) to create a Neural Network with five layers (supervised learning) 
#lbfgs: stochastic gradient descent
#hidden_layer_sizes: five hidden units and two hidden layer
#alpha: regulation penalty 
clf = MLPClassifier(solver='lbfgs', alpha=1e-5, hidden_layer_sizes=(5,2), random_state = 4)

#load trainning data sets to two vectors X and y
X,y = digits.data[:-10], digits.target[:-10]

#Apply the neural network to the data set 
clf.fit(X,y)

#print the prediction 
print('Prediction: ', clf.predict(digits.data[-2]))
#print the picture of the digit 
plt.imshow(digits.images[-2], cmap=plt.cm.gray_r, interpolation = "nearest")
#show the digit with matplotlib 
plt.show()