freqency = 0

with open('Day 1/changes.dat', "r") as data:
    for line in data:
        freqency += int(line)

with open("Day 1/result.dat", "w") as result:
    result.write(str(freqency))