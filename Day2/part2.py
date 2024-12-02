########################################################################
###################### BROKEN CODE ####################################
########################################################################


f = open("input.txt", "r")
    
count = 0
for idx, line in enumerate(f):
    levels = line.strip("\n").split(" ")
    print(levels)
    
    levels = [int(level) for level in levels]
    levelsCopy = levels.copy()
    
    dampener = False
    decreasingValid = True
    
    # Since our list can dynamically change, we need to use a while loop
    i = 0
    while i < len(levels) - 1:
        if (levels[i] - levels[i + 1] >= 1) and (levels[i] - levels[i + 1] <= 3):
            i += 1
        elif not dampener:
            if i == 0 and (levels[i+1] - levels[i + 2] >= 1 and levels[i+1] - levels[i + 2] <= 3):
                levels.pop(i)
            else:
                levels.pop(i+1)
            dampener = True
        else:
            decreasingValid = False
            break
    
    levels = levelsCopy
    increasingValid = True
    dampener = False
    
    i = 0
    while i < len(levels) - 1:
        if (levels[i + 1] - levels[i] >= 1) and (levels[i + 1] - levels[i] <= 3):
            i += 1
        elif not dampener:
            if i == 0 and (levels[i+2] - levels[i + 1] >= 1 and levels[i+2] - levels[i + 1] <= 3):
                levels.pop(i)
            else:
                levels.pop(i+1)
            dampener = True
        else:
            increasingValid = False
            break

    if decreasingValid or increasingValid:
        print(f"{idx+1} Valid sequence")
        count += 1
        print(count)
    else:
        print(f"{idx+1} Invalid sequence")
print(count)