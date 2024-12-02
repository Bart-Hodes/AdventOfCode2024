f = open("input.txt", "r")

count = 0
for line in f:
    levels = line.strip("\n").split(" ")

    levels = [int(level) for level in levels]

    previousLevel = levels[0]
    
    decreasingValid = all(
            (levels[i] - levels[i + 1] >= 1) and (levels[i] - levels[i + 1] <= 3)
            for i in range(len(levels) - 1)
        )
    increasingValid = all(
        (levels[i + 1] - levels[i] >= 1) and (levels[i + 1] - levels[i] <= 3)
        for i in range(len(levels) - 1)
    )
    
    if decreasingValid or increasingValid:
        count += 1
print(count)
