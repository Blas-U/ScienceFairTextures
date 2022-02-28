import numpy as np

def subSample(numRun, fraction, fileName, dx):
    #read file, open data.
    with open(fileName) as file:
        data = file.readlines()
        for i in range(len(data)):
            data[i] = float(data[i]) # change from string to floating point numbers.
            #print(i,data[i])
    numdata = len(data)
    popavg = np.average(data)
    popstdev = np.std(data)
    print("popavg =",popavg)
    print("popstdev =",popstdev)
    print("numdata =", numdata)

    out50a=[]
    out50s=[]

    nbetween = 0

    for i in range(numRun):
        n = int(numdata*fraction) #50% of the TextureData
        d = np.random.choice(data, n, False)
        print(d)
        print(n)
        sampleAvg = np.average(d)
        samplestdev = np.std(d)
        out50a.append(sampleAvg)
        out50s.append(samplestdev)
        print(f"{n}, {sampleAvg}, {samplestdev}")
        if ((sampleAvg >= -40 - dx) and (sampleAvg <= -40 + dx)):
            nbetween += 1
    percentBet = nbetween/numRun
    print(percentBet)
    #print(out50a)
    pop50avgAvg = np.average(out50a)
    print("pop50avgAvg", pop50avgAvg)
    print()





subSample(10, .5, "TextureData.csv", .25)
subSample(10, .75, "TextureData.csv", .25)
