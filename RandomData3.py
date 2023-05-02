import numpy as np

#read file, open data.
with open("SMA-7_for_Blas.csv", encoding='utf-8-sig') as file:
    data = file.readlines()
    print(data)
    for i in range(len(data)):
        data[i] = float(data[i].strip()) # change from string to floating point numbers.
        #print(i,data[i])
numdata = len(data)
popavg = np.average(data)
popstdev = np.std(data)
print("popavg =",popavg)
print("popstdev =",popstdev)
print("numdata =", numdata)


#peramiters
Fraction = .50 #% of data
nTimes = 10 #number of times subsampled



#test with 10 data points.
for i in range(nTimes):
    n = int(numdata*Fraction)
    d = np.random.choice(data, n)
    print()
    print(f'Iteration: {i +1}')
    print(d)
    print(n)
    sampleAvg = np.average(d)
    samplestdev = np.std(d)
    print(f"Number of Samples: {n}, Average: {sampleAvg}, Standard Deviation: {samplestdev}")

# for i in range(10):
#     n = int(numdata*.75)
#     d = np.random.choice(data, n)
#     #print(d)
#     #print(n)
#     sampleAvg = np.average(d)
#     samplestdev = np.std(d)
#     print(f"{n}, {sampleAvg}, {samplestdev}")

# for i in range(1):
#     n = int(numdata*1)
#     d = np.random.choice(data, n)
#     #print(d)
#     #print(n)
#     sampleAvg = np.average(d)
#     samplestdev = np.std(d)
#     print(f"{n}, {sampleAvg}, {samplestdev}")
