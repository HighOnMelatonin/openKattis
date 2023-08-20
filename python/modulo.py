nums = []
for i in range(10):
    nums.append(int(input()))
    
rems = []
for num in nums:
    rem = int(num)%42
    if not rem in rems:
        rems.append(rem)
        
    else:
        continue
    
print(len(rems))
