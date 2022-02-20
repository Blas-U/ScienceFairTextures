import numpy as np

#read file, open data.
with open("Science Fair - Sheet3(1).csv") as file:
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

#test with 10 data points.
for i in range(10):
    n = int(numdata*.50)
    d = np.random.choice(data, n)
    #print(d)
    #print(n)
    sampleAvg = np.average(d)
    samplestdev = np.std(d)
    print(f"{n}, {sampleAvg}, {samplestdev}")

for i in range(10):
    n = int(numdata*.75)
    d = np.random.choice(data, n)
    #print(d)
    #print(n)
    sampleAvg = np.average(d)
    samplestdev = np.std(d)
    print(f"{n}, {sampleAvg}, {samplestdev}")

for i in range(1):
    n = int(numdata*1)
    d = np.random.choice(data, n)
    #print(d)
    #print(n)
    sampleAvg = np.average(d)
    samplestdev = np.std(d)
    print(f"{n}, {sampleAvg}, {samplestdev}")
