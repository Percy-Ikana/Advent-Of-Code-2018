from string import ascii_lowercase

with open('Day 5/data.dat', "r") as data:
    input_base = str(data.read())

min_length = len(input_base)
for y in ascii_lowercase:
    input = input_base
    input = input.replace(f'{y}',"")
    input = input.replace(f'{y.upper()}',"")
    removed = True
    while removed:
        removed = False
        length = len(input)
        for x in ascii_lowercase:
            input = input.replace(f'{x}{x.upper()}',"")
            input = input.replace(f'{x.upper()}{x}',"")
        if length  > len(input):
            removed = True
    if len(input) < min_length:
        min_length = len(input)


with open('Day 5/results 2.dat', "w") as results:
    results.write(str(min_length))