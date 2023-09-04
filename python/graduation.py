# Graduation
'''
Number of unique classes in a column
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
letterDict = [] # shows the index of the letter in "hats"
for i in range(int(m)):
    exists = False
    # checks if there are repeated letters in the column (i.e. 'A' appeared twice in the column)
    for line in lines:
        if line[i] in hats[j]:
            exists = True

        else:

            if exists:
                hats[j] += [line[i]]

            else:
                hats.append([line[i]])
                j += 1
                exists = True

print(hats)
print(len(hats) - 1)
