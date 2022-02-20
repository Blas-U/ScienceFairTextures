import numpy as np

#read file, open data.
with open("TextureData.csv") as file:
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

#create array to store data
means = []

#test with 10 data points.
for i in range(100000):
    n = int(numdata*.5)
    d = np.random.choice(data, n)
    #print(d)
    #print(n)
    sampleAvg = np.average(d)
    means.append(sampleAvg)
    samplestdev = np.std(d)
#    print(f"{n}, {sampleAvg}, {samplestdev}")

range = (np.amax(means) - np.amin(means))
print("Range =", range)
