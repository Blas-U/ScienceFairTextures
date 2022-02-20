import numpy as np

def subSample(n, fraction):
    for i in range(n):
        n = int(numdata*fraction) #50% of the TextureData
        d = np.random.choice(data, n)
        #print(d)
        #print(n)
        sampleAvg = np.average(d)
        samplestdev = np.std(d)
        out50a.append(sampleAvg)
        out50s.append(samplestdev)
        print(f"{n}, {sampleAvg}, {samplestdev}")
    print(out50a)
    pop50avgAvg = np.average(out50a)
    print("pop50avgAvg", pop50avgAvg)




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

out50a=[]
out50s=[]

#test 10 times.
for i in range(10):
    n = int(numdata*.5) #50% of the TextureData
    d = np.random.choice(data, n)
    #print(d)
    #print(n)
    sampleAvg = np.average(d)
    samplestdev = np.std(d)
    out50a.append(sampleAvg)
    out50s.append(samplestdev)
    print(f"{n}, {sampleAvg}, {samplestdev}")
print(out50a)
pop50avgAvg = np.average(out50a)
print("pop50avgAvg", pop50avgAvg)

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
    d = np.random.choice(data, n, False)
    print(d)
    print(n)
    sampleAvg = np.average(d)
    samplestdev = np.std(d)
    print(f"{n}, {sampleAvg}, {samplestdev}")
