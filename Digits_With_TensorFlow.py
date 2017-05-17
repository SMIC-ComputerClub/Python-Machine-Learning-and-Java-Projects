#!/usr/bin/python

#import tensorflow package and import data from tensorflow 
import tensorflow as tf 

#Import data
from tensorflow.examples.tutorials.mnist import input_data
mnist = input_data.read_data_sets("MNIST_data/", one_hot=True)

#Model starts here!
#A placehooder for the neural network (the first layer)
x = tf.placeholder(tf.float32, [None, 784])

#Weight of each input: each of the pixel (784 pixels in total) will have different weight to a specific tensor (10 outputs in total)
W = tf.Variable(tf.zeros([784, 10]))
#bias of each pixel: trying to make the result more independent of the evidence (input)
b = tf.Variable(tf.zeros([10]))

#The main algorithm that refines the weights and bias of the pixel, turing the result into the final ten output
#Softmax will automatically calculate the percentage of the evidence inside the whole pixel, and everything in the final ten results will result into a group of decimals that add up to 1
y = tf.nn.softmax(tf.matmul(x, W) + b)

#Trainning starts here!
#Using cross-entropy algorithm, where the cross-entropy needs to be reduced
#Cross-entropy function is given by the summation of true distribution times the log of predicted distribution
#True distribution is marked by z
z = tf.placeholder(tf.float32, [None, 10])

#this is the cross_entropy function provided by tensorflow
cross_entropy = tf.reduce_mean(-tf.reduce_sum(z * tf.log(y), reduction_indices=[1]))

#Using gradientDescentOptimizer to reduce the cross_entropy (gradient descent is bascially to find the local minimum without using derivative in this case)
train_step = tf.train.GradientDescentOptimizer(0.5).minimize(cross_entropy)


sess = tf.InteractiveSession()

tf.global_variables_initializer().run()

for _ in range(1000):
	#Randomly select 100 evidences to train and change the weight of each pixel
	batch_xs, batch_ys = mnist.train.next_batch(100) 
	#Start of the trainning step (in which it used gradient descent
	#Evidences are assigned above	
	sess.run(train_step, feed_dict={x: batch_xs, z: batch_ys})

#Check the accuracy of this trainned model
correct_prediction = tf.equal(tf.argmax(y,1), tf.argmax(z,1))

accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))

print(sess.run(accuracy, feed_dict={x: mnist.test.images, z: mnist.test.labels}))