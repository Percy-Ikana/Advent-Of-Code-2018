fabric = [[[]]]
claims = set()

with open('Day 3/data.dat', "r") as data:
    for input in data:
        claim_id = int(input.split(" ")[0][1:])
        claims.add(claim_id)
        offset = [int(x) for x  in input.split('@')[1].split(':')[0].split(',')]
        size = [int(x) for x in input.split(':')[1].split('x')]

        if len(fabric) < offset[0]+size[0]:
            for i in range(offset[0]+size[0]-len(fabric)):
                fabric.extend([[[]]])

        for x in range(size[0]):
            for y in range(size[1]):
                if len(fabric[x+offset[0]]) < offset[1]+size[1]:
                    for i in range(offset[1]+size[1]-len(fabric[x+offset[0]])):
                        fabric[x+offset[0]].extend([[]])
                fabric[x+offset[0]][y+offset[1]].append(claim_id)

    count = 0
    for x in fabric:
        for y in x:
            if len(y) > 1:
                count += 1
                for z in y:
                    if z in claims:
                        claims.remove(z)

    with open("Day 3/result 2.dat", "w") as result:
        result.write(str(claims))