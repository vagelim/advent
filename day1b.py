with open ('t.txt', 'r') as f:
    j = f.read()

count = 0

for i, each in enumerate(j):
    if count == -1:
        print i
        break
        
    if each == '(':
        count += 1
    else:
        count = count - 1
