
with open ('t.txt', 'r') as f:
    j = f.read()

count = 0

for each in j:
    if each == '(':
        count += 1
    else:
        count = count - 1

print count
