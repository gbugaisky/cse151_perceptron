import numpy as np


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
        w = np.array([0] * 784)
        for d in data:
            l = d[len(d) - 1]
            featurevec = d[:-1]
            if l == label:
        		l = 1
            else:
        		l = -1
            if (l * np.dot(w, featurevec)) <= 0:
                temparray = np.array([label * x for x in featurevec])
                w += temparray
        return w 

    def match(self, test):
        labels = np.array([])
        t = np.array(test)
        for featurevec in self.c:
            l = test[len(test)-1] #get the label
            f = np.array(featurevec)      #discard the label
            if (np.dot(t, f)) > 0:
               labels = np.hstack((labels, [l])); 
        return labels


if __name__ == "__main__":
    #A. Create the one vs all linear classifier
    oVa = oneVsAll()

    """
    Now we have the classifiers
    """

    #B. Initialize the confusion matrix
    confusion = [[0] * 11, [0]*11, [0]*11, [0]*11, [0]*11, [0]*11, [0]*11, [0]*11, [0]*11, [0]*11]
   
    #C. Make the confusion matrix
    with open("hw2test.txt", 'r') as file:
        for line in file:
            templine = map(int, line.split())
            label = templine[len(templine) - 1]
            featurevec = templine[:-1]

            #Now we need ot see which this matches
            matches = oVa.match(featurevec)

            #for each match, increment the appropriate portion of the table
            if matches == []:    ##if it's empty
                confusion[label][10] += 1;
            else :
                for m in matches:
                    confusion[label][m] += 1;

    i = 0
    for c in confusion:
        s = str(i) + " "
        for b in c:
            s = s + str(b) + " "
        print s
        i += 1
