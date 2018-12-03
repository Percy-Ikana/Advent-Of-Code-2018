
with open('Day 2/data.dat', "r") as data:
    data = [x for x in data]

for x in range(0,len(data) - 1):
    for y in range(x+1,len(data)):
        diffrent = [z for z in range(len(data[x])-1) if data[x][z] != data[y][z]]
        if len(diffrent) == 1:
           with open("Day 2/result 2.dat", "w") as result:
                result.write(data[x][:diffrent[0]] + data[x][diffrent[0]+1:])