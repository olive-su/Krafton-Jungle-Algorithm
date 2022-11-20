array = [42, 32, 24, 60, 15]

def selection_sort(arr):
    for i in range(len(arr)):
        target = arr[i]
        target_idx = i
        for j in range(i + 1, len(arr)):
            if target > arr[j]:
                target = arr[j]
                target_idx = j
        arr[i], arr[target_idx] = target, arr[i]

    return arr

print(selection_sort(array))