# Honeycomb Walk
'''
Some notes:

For even numbers:
Imagine a polygon with n number of nodes, the starting point can be any one of those nodes, since the 
polygon is a closed loop, as long as the n is the number of nodes, starting at any node will end at that
starting node.

Reverse the direction of movement along the nodes

n*2

Rotate the polygon along the starting point, since its a hexagonal cell

n*2*6

Straight paths passing through the center, going one step back and forth in the 6 directions
n*2*6 + 6**2

Finally, add 6 for the 6 straight lines the bee can travel across (for even numbers)

For odd numbers:
Every odd number can be reduced to 3 + 2n, where 2n is an even number, so odd numbers can make straight lines after
making a triangle with 3 nodes.

'''

# num refers to the number of test cases to follow
num = int(input())

def polygons(n):
    return n*2*6

def triangles(n):
    return n*6

output = []
for i in range(num):
    n = int(input())
    odd = n%2
    if n == 2:
        total = 6

    elif n == 1:
        total = 0
    
    elif not odd:
        total = polygons(n) + 6**(n/2) + 6

    else:
        total = n*2*6

    output.append(int(total))

for total in output:
    print(total)

#works for n = 2, 3 and 4
