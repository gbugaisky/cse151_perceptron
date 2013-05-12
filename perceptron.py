import numpy as np

def perceptron(filename):
	m = 1
	w = [0] * 784
	with open(filename, 'r') as file:
		for line in file:
			templine = map(int, line.split(" "))
			label = templine[len(templine) - 1]
			featurevec = templine[:-1]
			if label == 0:
				label = -1
			else:
				label = 1

			if (label * np.dot(w, featurevec)) <= 0:
				temparray = [label * x for x in featurevec]
				w += temparray


if __name__ == "__main__":
	perceptron()