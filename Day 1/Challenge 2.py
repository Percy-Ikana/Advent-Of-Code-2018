freqency = 0

duplicate = False
result_set = set()
result_set.add(freqency)

with open('Day 1/changes.dat', "r") as data_file:
    data = data_file.readlines()
    data = [int(x) for x in data]
while not duplicate:
    for line in data:
        freqency += line
        if freqency in result_set:
            duplicate = True
            break
        else:
            result_set.add(freqency)

with open("Day 1/result 2.dat", "w") as result:
    result.write(str(freqency))