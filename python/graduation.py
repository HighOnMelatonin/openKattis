# Graduation
'''
Create a stack for every column, as the cursor parses through the column, add every unique letter to the stack

If a letter in the column 
'''
line = input()
n, m, k = line.split(' ')

lines = []
for i in range(int(n)):
    line = input()
    lines.append(line)

hats = [[]]
j = 0
letters = []    # letters that already have a hat associated
letterDict = {} # shows the index of the letter in "hats"
for i in range(int(m)):
    exists = False
    column = [] #Column contains all the unique letters in the column
    for line in lines:
        if line[i] in letterDict:
            exists = True
            j = letterDict[line[i]]

        elif not line[i] in column:
            column.append(line[i])

    if exists:
        hats[j] += column

    else:
        j += 1
        for item in column:
            letterDict.update({item: j})
        hats.append(column)


print(hats)
print(len(hats) - 1)

'''
Fails test case 5:

3 5 5
ABECE
BCDAE
CADBA

Expected output: 1

'''
