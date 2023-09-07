# Messy lists

n = int(input())
line = input()

nums = line.split(' ')

# Some sorting algorithm
sortednums = []
for i in nums:
    sortednums.append(i)

def quick(array, start, end):
    if start < end:
        low = start
        high = end
        pivot = array[end]

        while low < high:
            while high > 0 and array[high] >= pivot:
                high -= 1

            while low < end and array[low] < pivot:
                low += 1

            if low < high:
                array[high], array[low] = array[low], array[high]

        array[low], array[end] = array[end], array[low]

        quick(array,start, low - 1)
        quick(array, low + 1, end)

    return array

output = 0
sortednums = quick(sortednums, 0, len(sortednums) - 1)

for i in range(n):
    if sortednums[i] != nums[i]:
        output += 1

print(output)

# Incomplete solution, failed a few test cases