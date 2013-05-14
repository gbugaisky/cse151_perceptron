import math
import numpy as np
from itertools import izip

def perceptron(trainfile, testfile):
	#m = 1
	w = [0] * 784
	with open(trainfile, 'r') as file:
		for line in file:
			templine = map(int, line.split())
			label = templine[len(templine) - 1]
			featurevec = templine[:-1]
			if label == 0:
				label = -1
			else:
				label = 1

			if (label * np.dot(w, featurevec)) <= 0:
				temparray = [label * x for x in featurevec]
				w = map(sum, izip(w, temparray))

	#print w

	#get the error for the algorithm (Open testfile, and run)
	error = 0
	linecount = 0
	with open(testfile, 'r') as test:
		for line in test:
			linecount += 1
			templine = map(int, line.split())
			label = templine[len(templine) - 1]
			featurevec = templine[:-1]
			if label == 0:
				label = -1
			else:
				label = 1
			if (label * np.dot(w, featurevec)) <= 0:
				error += 1

	#print out the error
	print "Error on perceptron:", error, "/", linecount

def votedperceptron(trainfile, testfile):
	#create the voted perceptron classifier (var vote)
	w = [0] * 784
	c = 1
	vote = list() #Blank 2D list for holding later results
	with open(trainfile, 'r') as file:
		for line in file:
			templine = map(int, line.split())
			label = templine[len(templine) - 1]
			featurevec = templine[:-1]
			if label == 0:
				label = -1
			else:
				label = 1

			if (label * np.dot(w, featurevec)) <= 0:
				vote.append([w,c])
				temparray = [label * x for x in featurevec]
				w = map(sum, izip(w, temparray))
				c = 1
			else:
				c += 1

	#print "Starting Error Check (This takes a while)..."
	#get test error for voted perceptron
	error = 0
	linecount = 0
	with open(testfile, 'r') as test:
		for line in test:
			linecount += 1
			templine = map(int, line.split())
			label = templine[len(templine) - 1]
			featurevec = templine[:-1]
			if label == 0:
				label = -1
			else:
				label = 1
			summation = 0

			#NOTE: copysign gives us the sign of the equation (we use 1 to fit our label)
			for element in vote:
				summation += (element[1] * math.copysign(1, np.dot(element[0], featurevec)))
			if math.copysign(1, summation) != label:
				error += 1
	print "Error on voted perceptron:", error, "/", linecount

def averageperceptron(trainfile, testfile):
	#create the average perceptron classifier (var aver)
	w = [0] * 784
	c = 1
	aver = [0] * 784#Blank list for holding later results
	with open(trainfile, 'r') as file:
		for line in file:
			templine = map(int, line.split())
			label = templine[len(templine) - 1]
			featurevec = templine[:-1]
			if label == 0:
				label = -1
			else:
				label = 1

			if (label * np.dot(w, featurevec)) <= 0:
				temphold = [c * x for x in w]
				aver = map(sum, izip(aver, temphold))
				temparray = [label * x for x in featurevec]
				w = map(sum, izip(w, temparray))
				c = 1
			else:
				c += 1

	#print "Starting Error Check (This takes a while)..."
	#get test error for average perceptron
	error = 0
	linecount = 0
	with open(testfile, 'r') as test:
		for line in test:
			linecount += 1
			templine = map(int, line.split())
			label = templine[len(templine) - 1]
			featurevec = templine[:-1]
			if label == 0:
				label = -1
			else:
				label = 1
			
			#do dot product and see if it equals label
			if math.copysign(1, np.dot(aver, featurevec)) != label:
				error += 1
	print "Error on average perceptron:", error, "/", linecount

if __name__ == "__main__":
	print "Error: (Training Suite)"
	perceptron(".\\hw4train.txt", ".\\hw4train.txt")
	votedperceptron(".\\hw4train.txt", ".\\hw4train.txt")
	averageperceptron(".\\hw4train.txt", ".\\hw4train.txt")
	print "Error: (Test Suite)"
	perceptron(".\\hw4train.txt", ".\\hw4test.txt")
	votedperceptron(".\\hw4train.txt", ".\\hw4test.txt")
	averageperceptron(".\\hw4train.txt", ".\\hw4test.txt")