#!/usr/bin/env python
#Day 2 part 2
total = 0

with open('day2.txt', 'r') as f:
    line = f.read()

lines = line.split('\n')
lines = lines[:-1] #Strip newline at the end of text

for each in lines:
    sides = map(int, each.split('x'))
    smallest = sorted(sides)[:2]
    perimeter = smallest[0] * 2 + smallest[1] * 2

    volume = sides[0] * sides[1] * sides[2]
    #l, w, h = map(int, each.split('x'))
    # Get smallest sides
    #smallest = sorted(l, w, h)[:2]
    total += perimeter + volume
print total
