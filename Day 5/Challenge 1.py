from string import ascii_lowercase

with open('Day 5/data.dat', "r") as data:
    input = str(data.read())

removed = True

while removed:
    removed = False
    length = len(input)
    for x in ascii_lowercase:
        input = input.replace(f'{x}{x.upper()}',"")
        input = input.replace(f'{x.upper()}{x}',"")
    if length  > len(input):
        removed = True

with open('Day 5/results.dat', "w") as results:
    results.write(str(len(input)))