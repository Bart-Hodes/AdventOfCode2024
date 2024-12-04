f = open("input.txt", "r")

count = 0
historianOneLocationList = []
historianTwoLocationList = []
for line in f:
    split = line.strip("\n").split("   ")

    historianOneLocationList.append(int(split[0]))
    historianTwoLocationList.append(int(split[1]))

historianOneLocationList.sort()
historianTwoLocationList.sort()

for idx in range(len(historianOneLocationList)):
    count += abs(historianOneLocationList[idx] - historianTwoLocationList[idx])
print(count)
