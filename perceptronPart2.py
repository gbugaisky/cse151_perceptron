import numpy as np


"""
The steps:
    1. Read the file for each label, creating a vector for elements of that label
    2. create the perceptron for that label vs everything else
    3. 
"""

def main(self):
    #A. Create the one vs all linear classifier
    oVa = oneVsAll()


    """
    Now we have the classifiers
    """

    #B. Initialize the confusion matrix
    confusion = [[0] * 11, [0]*11, [0]*11, [0]*11, [0]*11, [0]*11, [0]*11, [0]*11, [0]*11, [0]*11]
   
    #C. Make the confusion matrix
    with open("hwk2test.txt", 'r') as file:
        for line in file:
            templine = map(int, line.split(" "))
            label = templine[len(templine) - 1]
            featurevec = templine[:-1]

            #Now we need ot see which this matches
            matches = oVa.match(featurevec)

            #for each match, increment the appropriate portion of the table
            if matches == []:    ##if it's empty
                confusion[10][label] += 1;
            for m in matches:
               confusion[m][label] += 1;



    for c in confusion
        for b in c
            print b + " "
        print "\n"



if __name__ == "__main__":
    main()


class oneVsAll :
    c0 = [][]
    c1 = [][]
    c2 = [][]
    c3 = [][]
    c4 = [][]
    c5 = [][]
    c6 = [][]
    c7 = [][]
    c8 = [][]
    c9 = [][]

    def self:
        #1. bundle them all up
        data = open()

        #2. for each feature vector, create the classifier
        c0 = perceptron(data, 0)
        c1 = perceptron(data, 1)
        c2 = perceptron(data, 2)
        c3 = perceptron(data, 3)
        c4 = perceptron(data, 4)
        c5 = perceptron(data, 5)
        c6 = perceptron(data, 6)
        c7 = perceptron(data, 7)
        c8 = perceptron(data, 8)
        c9 = perceptron(data, 9)

    
    def open(self):
        w = []
        with open("hwk2train.txt", 'r') as file:
            for line in file:
                templine = map(int, line.split(" "))
                featurevec = templine[:-1]
                np.vstack(w, featurevec)

        return w

    
    def perceptron(self, data, label):
        c = [][]
        for d in data:
			l = templine[len(templine) - 1]
			featurevec = templine[:-1]
			if l == label:
				l = 1
			else:
				l = -1

			if (l * np.dot(w, featurevec)) <= 0:
				temparray = [label * x for x in featurevec]
                c += temparray
