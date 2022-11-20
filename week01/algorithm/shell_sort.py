array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

def shell_sort(arr):
    n = len(arr)
    gap = n // 2
    while gap > 0: # gap을 바꿔서 다시 루프 수행
        for i in range(gap, n):
            j = i - gap # pair : (j, i)
            tmp = arr[i]
            while j >= 0 and arr[j] > tmp: # arr[j] > arr[i]
                arr[j + gap] = arr[j]
                j -= gap
            arr[j + gap] = tmp
        gap //= 2

    return arr

print(shell_sort(array))