array = [2, 2, 3, 3, 5, 2]
counts = {}
maximum_count = 0
occuring = None

for num in array:
    if num in counts:
        counts[num] += 1
    else:
        counts[num] = 1

for num in counts:
    if counts[num] > maximum_count:
        maximum_count = counts[num]
        occuring = num

print(occuring)