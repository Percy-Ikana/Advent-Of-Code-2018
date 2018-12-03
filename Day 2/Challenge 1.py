from string import ascii_lowercase

two_count = 0
three_count = 0

with open('Day 2/data.dat', "r") as data:
    for line in data:
        double = False
        triple = False
        for letter in ascii_lowercase:
            if line.count(letter) == 2 and not double:
                two_count +=1
                double = True
            if line.count(letter) == 3 and not triple:
                three_count +=1
                triple = True
            if double and triple:
                break

with open("Day 2/result.dat", "w") as result:
    result.write(str(two_count*three_count))