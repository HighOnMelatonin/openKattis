# refrigerator Transport

'''
n number of refrigerators to be delivered

Car A costs pa per trip and can load ka refrigerators per trip

Car B costs pb per trip and can load kb refrigerators per trip
'''

# input is separated by spaces
line = str(input())
a, b, c, d, e = line.split(' ')
pa, ka, pb, kb, n = int(a), int(b), int(c), int(d), int(e)

tripsA = 0
tripsB = 0
if pb >= pa:
    tripsB = int(n//kb)
    rem = n%kb
    if rem:
        tripsB += 1

else:
    tripsA = int(n//pb)
    rem = n%pb
    if rem:
        tripsA += 1

cost = tripsA*pa + tripsB*pb
output = [tripsA, tripsB, cost]

lowest = False
while not lowest:
    if pb >= pa:
        tripsB = output[1] - 1
        rem = n - kb*tripsB
        tripsA = int(rem//ka)
        if rem%ka:
            tripsA += 1

        cost = tripsA*pa + tripsB*pb
        if cost < output[2]:
            output = [tripsA, tripsB, cost]

        else:
            lowest = True

    else:
        tripsA = output[0] - 1
        rem = n - ka*tripsA
        tripsB = int(rem//kb)
        if rem%kb:
            tripsB += 1

        cost = tripsA*pa + tripsB*pb
        if cost < output[2]:
            output = [tripsA, tripsB, cost]

        else:
            lowest = True

print(int(output[0]), int(output[1]), int(output[2]))
