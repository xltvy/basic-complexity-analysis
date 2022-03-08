import time
import glob

#Code of the given pseudocode
def function(X):

    y = 0

    n = len(X)

    for i in range(0, n):
        if X[i]==0:
            for j in range(i, n):
                k = n
                while k >= 1:
                    y = y+1
                    k = k/2
        else:
            for m in range(i, n):
                for t in range (1, n+1):
                    x = n
                    while x > 0:
                        x = x-t
                        y = y+1

    return(y)

input_list = glob.glob('*.txt') #List that contains every input file name
input_list.sort()   #Sorts the list according to file names

"""
Divides the list into pieces of 7 input files.
First of the seven denotes the input for best-case execution.
Second of the seven denotes the input for worst-case execution.
Last five of the seven denote the input for five average-case executions.
"""
for f in range(0, len(input_list), 7):

    slice = input_list[f:f+7]   #Seven input file in order

    avg_time = 0    #Stores the sum of average-case inputs' execution times in seconds
    c = ""  #Denotes the case (either best, worst, or average)
    s = 0   #Denotes the input size

    """
    Counter keeps the record of in which part of the
    7 input file slice the algorithm is currently in.
    After the algorithm is executed for each input file,
    counter is incremented by one. 
    """
    counter = 0
    for i in slice:

        X = []  #List that contains the inputs from input file
        #List X is filled
        input_file = open(i, 'r')
        for line in input_file:
            X.append(int(line.strip()))
        """
        Conditional operation to check in which input file the algorithm
        currently executes
        """
        if counter == 0:
            #Best case
            c = "best"
            s = len(X)
            start_time = time.time()
            function(X)
            t = (time.time() - start_time)
            #Time is measured and the result will be printed to the CLI
            print('Case: {0} Size: {1} Elapsed Time: {2}'.format(c, s, t))
        elif counter == 1:
            #Worst case
            c = "worst"
            s = len(X)
            start_time = time.time()
            function(X)
            t = (time.time() - start_time)
            #Time is measured and the result will be printed to the CLI
            print('Case: {0} Size: {1} Elapsed Time: {2}'.format(c, s, t))
        else:
            #Average case
            c = "average"
            s = len(X)
            start_time = time.time()
            function(X)
            t = (time.time() - start_time)
            #Time is measured and the result will be stored in avg_time
            avg_time += t   #Each average time measurement will be added together

        counter += 1    #Counter is incremented by one
        X = []  #Input list X is reset

    t = avg_time/5  #Average time of execution is calculated considering 5 input files
    #Average time is measured and the result will be printed to the CLI
    print('Case: {0} Size: {1} Elapsed Time: {2}'.format(c, s, t))
