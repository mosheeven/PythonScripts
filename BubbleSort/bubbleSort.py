def sort(arr):
    while True:
        flag = False
        for num in range(0, len(arr)-1):
            if arr[num] > arr[num+1]:
                arr[num], arr[num+1] = arr[num+1], arr[num]
                flag = True
        if not flag:
            return arr

# Best O(n)
print(sort([1, 2, 3, 4, 6]))

# Avarage O(n^2)
print(sort([4, 2, 3, 1, 6, 5]))

# Worst O(n^2)
print(sort([6, 5, 4, 3, 2, 1]))
