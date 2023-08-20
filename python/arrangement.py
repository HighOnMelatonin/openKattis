n = int(input())
m = int(input())

num = m//n
rem = m%n


# output
for i in range(rem):
    print("*"*(num + 1))

for i in range(n - rem):
    print("*"*num)
