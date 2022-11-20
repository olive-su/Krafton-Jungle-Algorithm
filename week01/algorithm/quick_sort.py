array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(arr, start, end):
    if start >= end:
        return 

    pivot = start
    left = start + 1
    right = end

    while left <= right:
        while left <= end and arr[left] <= arr[pivot]:
            left += 1
        while right > start and arr[right] >= arr[pivot]:
            right -= 1
        if left > right: # left는 pivot보다 큰 경우, right는 pivot보다 작은 경우
            arr[right], arr[pivot] = arr[pivot], arr[right]
        else:
            arr[left], arr[right] = arr[right], arr[left]
    
    quick_sort(arr, start, right - 1)
    quick_sort(arr, right + 1, end)


def quick_sort2(arr):
    if len(arr) <= 1:
        return

    pivot = arr[len(arr) // 2]
    lesser_arr, equal_arr, greater_arr = [], [], []
    for a in arr:
        if a < pivot: lesser_arr.append(a)
        elif a == pivot: equal_arr.append(a)
        else: greater_arr.append(a)
    
    return quick_sort2(lesser_arr) + equal_arr + quick_sort2(greater_arr)

def quick_sort3(arr, left, right):
    pl = left
    pr = right
    pivot = arr[(left + right) // 2]

    while pl <= pr:
        while arr[pl] < pivot: pl += 1
        while arr[pr] > pivot: pr -= 1
        if pl <= pr:
            arr[pl], arr[pr] = arr[pr], arr[pl]
            pl += 1
            pr -= 1
    
    if left < pr: quick_sort3(arr, left, pr)
    if pl < right: quick_sort3(arr, pl, right)
    return arr
    

quick_sort(array, 0, len(array) - 1)
print(array)