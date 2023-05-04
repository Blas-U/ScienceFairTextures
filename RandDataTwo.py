import numpy as np

def subSample(numRun, fraction, data, dx):   #
    '''numRun (integer) - The number of times a sub-populatoin is created.
       fraction (Float) - The percentage of data (As a fraction) being taken in each sub-population.
       fileName (String) - Name of the input file with the data in one value per line.
       dx (Float)- The amount of spread within averages.'''
    #Read file, open data.

    numdata = len(data) #Finding the number of samples.
    popavg = np.average(data) #Finding the average of the full population of samples.
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

def subSampleWA(numRun, fraction, data, dx):   #
    '''numRun (integer) - The number of times a sub-populatoin is created.
       fraction (Float) - The percentage of data (As a fraction) being taken in each sub-population.
       fileName (String) - Name of the input file with the data in one value per line.
       dx (Float)- The amount of spread within averages.'''

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

pairs = []
out50a=[] 
out50s=[]

#read file, open data.
with open("NewData.csv") as file:
    data = file.readlines()

    for i in range(1,len(data)):
        d1,d2 = data[i].split('\t')
        d1 = float(d1)
        d2 = float(d2)
        pairs.append(f'{d1},{d2}')
        out50a.append(d1)
        out50s.append(d2)
    print(pairs)
        # print(i,d1, d2)
# print(out50a, out50s)

n = int(len(pairs)*.5) #50% of the TextureData
d = np.random.choice(pairs, n, False) 
sumA = 0 
sumBA = 0
for i in range(len(d)):
    sumA += float(d[i].split(',')[1])
    sumBA += float(d[i].split(',')[1]) * float(d[i].split(',')[0])
    Wave = sumBA/sumA
print(sumA, sumBA, Wave)
