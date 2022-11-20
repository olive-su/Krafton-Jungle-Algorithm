array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]
buff = [None] * len(array) # 작업용 배열

def merge_sort(arr, left, right):
    if left < right:
        center = (left + right) // 2

        merge_sort(arr, left, center) # 배열의 앞 부분 병합된 상태
        merge_sort(arr, center + 1, right) # 배열의 뒷 부분 병합된 상태

        p = j = 0 # buff의 포인터
        i = k = left # arr의 포인터

        # 원본 배열(arr)를 수정하기 위해 배열의 앞부분을 모두 buff로 복사한다.
        while i <= center:
            buff[p] = arr[i]
            p += 1
            i += 1
        
        # 배열 a의 뒷부분(arr[center + 1:]과 앞부분(현재 buff에 있는 상태)의
        # 각 원소를 비교해가며 다시 arr채워넣음
        while i <= right and j < p:
            if buff[j] <= arr[i]:
                arr[k] = buff[j]
                j += 1
            else:
                arr[k] = arr[i]
                i += 1
            k += 1

        # 만약 buff가 남았다면 해당 부분은 그냥 arr 맨 뒤에 붙여줌
        while j < p:
            arr[k] = buff[j]
            k += 1
            j += 1
    
    return arr
        
print(merge_sort(array, 0, len(array) - 1))