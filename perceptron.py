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

	print w

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

if __name__ == "__main__":
	perceptron(".\\hw4train.txt", ".\\hw4train.txt")