with open('Day 4/data.dat', "r") as data:
    input = [x for x in data]

input.sort()

watches = []

guards = {}

for line in input:
    info = line.replace("[", "").replace(']','').split(" ")
    if info[2] == 'Guard':
        #number, date, time, list of times asleep, times fallen asleep, total min
        watches.append([int(info[3][1:]), info[0], info[1], [], 0, 0])
        if int(info[3][1:]) not in guards.keys():
            guards[int(info[3][1:])] = [0,[0]*60]
    if info[2] == 'falls':
        watches[-1][3].append([int(info[1].split(':')[1])])
    if info[2] == 'wakes':
        for min in range(watches[-1][3][watches[-1][4]][0]+1, int(info[1].split(':')[1])):
            watches[-1][3][watches[-1][4]].append(min)
        watches[-1][5] += watches[-1][3][watches[-1][4]][-1] - watches[-1][3][watches[-1][4]][0] + 1
        guards[watches[-1][0]][0] += (watches[-1][3][watches[-1][4]][-1] - watches[-1][3][watches[-1][4]][0] + 1)
        for x in watches[-1][3][watches[-1][4]]:
            guards[watches[-1][0]][1][x] += 1
        watches[-1][4] += 1
        
maxx = 0
for  x in guards.keys():
    if guards[x][0] > maxx: 
        maxx = guards[x][0]
        guard = x
        min = guards[x][1].index(max(guards[x][1]))



with open("Day 4/result.dat", "w") as result:
    result.write(f'{guard}\n{min}')
