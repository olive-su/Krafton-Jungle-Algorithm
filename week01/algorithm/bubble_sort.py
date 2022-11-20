array = [42, 32, 24, 60, 15]

def bubble_sort(arr):
    for i in range(len(arr)):
        k = 0

        # 스캔 범위 제한
        while k < len(arr) - 1:
            for j in range(k, len(arr) - 1 - i):
                if arr[j] > arr[j + 1]:
                    last = j
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
            k = last
    return arr

print(bubble_sort(array))