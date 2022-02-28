import numpy as np #Importing a module for doing math calculations in python

def subSample(numRun, fraction, fileName, dx):   #
    '''numRun (integer) - The number of times a sub-populatoin is created.
       fraction (Float) - The percentage of data (As a fraction) being taken in each sub-population.
       fileName (String) - Name of the input file with the data in one value per line.
       dx (Float)- The amount of spred within averages.'''
    #Read file, open data.
    with open(fileName) as file:
        data = file.readlines()
        for i in range(len(data)):
            data[i] = float(data[i]) #Change from string to floating point numbers.
    numdata = len(data) #Finding the number of samples.
    popavg = np.average(data) #Finding the average of the full pupulation of samples.
    popstdev = np.std(data) #Finding the standard deviation of the full population of samples.
    print("popavg =",popavg)
    print("popstdev =",popstdev)
    print("numdata =", numdata)

    outAverage=[] #Creating arrays to store the results.
    outStDeviation=[]

    nbetween = 0 #Initializing the counter for the number of times the average of the data set goes over or under dx.

    for i in range(numRun): #creating a loop
        n = int(numdata*fraction) #50% of the TextureData
        d = np.random.choice(data, n, False) #Selecting random data and not repeating.
        sampleAvg = np.average(d) #Finding the average of the sub-population.
        samplestdev = np.std(d) #Finding the standard deviation of the sub-population.
        outAverage.append(sampleAvg) #Recording averages from each sub-population.
        outStDeviation.append(samplestdev)
        if ((sampleAvg >= -40 - dx) and (sampleAvg <= -40 + dx)): #Checking if the sample average is within dx+dx.
            nbetween += 1 #Adding 1 to nbetween for every inbetween number.
    percentBet = nbetween/numRun #Finding one percentage for what is inside the dx range.
    print(f'Percentage = {percentBet}')
    #print(outAverage)
    popavgAvg = np.average(outAverage) #Finding the average of the averages
    print("popavgAvg", popavgAvg)
    print()





subSample(100000, .5, "TextureData.csv", .25)
subSample(100000, .75, "TextureData.csv", .25)
