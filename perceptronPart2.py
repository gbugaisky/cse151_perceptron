import numpy as np
from itertools import izip

"""
The steps:
    1. Read the file for each label, creating a vector for elements of that label
    2. create the perceptron for that label vs everything else
    3. 
"""


class oneVsAll :
    c0 = [[]]
    c1 = [[]]
    c2 = [[]]
    c3 = [[]]
    c4 = [[]]
    c5 = [[]]
    c6 = [[]]
    c7 = [[]]
    c8 = [[]]
    c9 = [[]]
    
    data = [[]]

    c = np.array([])

    def __init__(self):
        #1. bundle them all up
        data = self.getData()

        #2. for each feature vector, create the classifier
        self.c = np.array([self.perceptron(data, 0),
        self.perceptron(data, 1),
        self.perceptron(data, 2),
        self.perceptron(data, 3),
        self.perceptron(data, 4),
        self.perceptron(data, 5),
        self.perceptron(data, 6),
        self.perceptron(data, 7),
        self.perceptron(data, 8),
        self.perceptron(data, 9)])
        
    def getData(self):
        w = np.array([])
        i = 0
        with open("hw2train.txt", 'r') as file:
            for line in file:
                templine = map(int, line.split())
                if i == 0:
                    i = 1
                    w = templine 
                elif i == 1:
                   w = np.vstack((w, templine))
        return w
    
    def perceptron(self, data, label):
        w = np.array([0] * 785)
        for d in data:
            l = d[len(d) - 1]
            featurevec = d[:-1]
            if l == label:
        		l = 1
            else:
        		l = -1
            if (l * np.dot(w[:-1], featurevec)) <= 0:
                temparray = np.array([l * x for x in d])
                w = map(sum, izip(w, temparray))
                w[len(w)-1] = label
        return w 

    def match(self, test):
        labels = np.array([])
        t = np.array(test[:-1])
        for featurevec in self.c:
            l = featurevec[len(featurevec)-1] #get the label
            f = np.array(featurevec[:-1])      #discard the label
            if (np.dot(t, f)) > 0:
               labels = np.hstack((labels, [l]))
        return labels


if __name__ == "__main__":
    #A. Create the one vs all linear classifier
    oVa = oneVsAll()

    """
    Now we have the classifiers
    """

    #B. Initialize the confusion matrix
    confusion = [[0] * 10, [0]*10, [0]*10, [0]*10, [0]*10, [0]*10, [0]*10, [0]*10, [0]*10, [0]*10, [0]*10]
   
    #C. Make the confusion matrix
    with open("hw2test.txt", 'r') as file:
        for line in file:
            templine = map(int, line.split())
            label = templine[len(templine) - 1]

            #Now we need ot see which this matches
            matches = oVa.match(templine)

            #for each match, increment the appropriate portion of the table
            if len(matches) == 0:    #if it's empty
                confusion[10][label] += 1;
            else :
                for m in matches:
                    if m == 0 :
                        print "  " + str(m)
                    confusion[int(m)][label] += 1;

    i = 0
    print " \t0\t1\t2\t3\t4\t5\t6\t7\t8\t9"
    totals = [0]*11
     
    for c in confusion:
        i = 0
        for b in c:
            totals[i] += b
            i += 1
    
    i = 0
    for c in confusion:
        s = str(i) + "\t"
        j = 0
        for b in c:
            if (totals[j] == 0) :
                s = s + str(b) + "\t"
            else :
                s = s + str((float(b))/(float(totals[j])))[:7] + "\t"
            j += 1
        print s
        i += 1
