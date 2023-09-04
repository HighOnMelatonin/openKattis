# Messy lists

n = input()
line = input()

nums = line.split(' ')

# Some sorting algorithm
sortednums = []
for item in nums:
    sortednums.append(item)

def merge(array):
    if len(array) > 1:
        mid = len(array)//2

        left = array[:mid]
        right = array[mid:]

        merge(left)
        merge(right)

        i = j = k = 0
        while i < len(left) and j < len(right):
            if int(left[i]) < int(right[j]):
                array[k] = left[i]
                i += 1

            else:
                array[k] = right[j]
                j += 1

            k += 1

        while i < len(left):
            array[k] = left[i]
            k += 1
            i += 1

        while j < len(right):
            array[k] = right[j]
            k += 1
            j += 1


output = 0
merge(sortednums)

for i in range(len(sortednums)):
    if sortednums[i] == nums[i]:
        continue
    
    else:
        output += 1

print(output)

# Incomplete solution, failed a few test cases, exceeded runtime