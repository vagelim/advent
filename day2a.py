#Day 2 part 1

total = 0
with open('day2.txt', 'r') as f:
    line = f.read()

lines = line.split('\n')
lines = lines[:-1]
for each in lines:
    t = each.split('x')
    l, w, h = int(t[0]), int(t[1]), int(t[2]) # This is ugly, don't look at it

    small = min ( (l * w) , (w * h) , (h * l)) # Get smallest surface area
    sa = 2 * l * w + 2 * l * h + 2 * w * h
    total +=  (sa + small)


print total
