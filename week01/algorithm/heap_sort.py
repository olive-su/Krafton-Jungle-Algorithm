array = [6, 4, 3, 7, 1, 9, 8]

def heap_sort(arr):    
    # left ~ right 힙으로 만들기
    def heapify(arr, left, right):
        temp = arr[left] # 루트 노드

        parent = left
        while parent < (right + 1) // 2:
            cl = parent * 2 + 1 # 왼쪽 자식
            cr = cl + 1 # 오른쪽 자식
            child = cr if cr <= right and arr[cr] > arr[cl] else cl # 더 큰 자식
            if temp >= arr[child]: # 루트 노드 그대로 유지 가능
                break
            arr[parent] = arr[child] # 루트 노드와 자식 노드 교환 필요
            parent = child # 루트 노드 인덱스와 자식 노드 인덱스 교환
        arr[parent] = temp

    n = len(arr)

    # arr[i] ~ arr[n - 1]을 힙으로 만들기
    for i in range((n - 1) // 2, -1, -1):
        heapify(arr, i, n - 1)
    
    for i in range(n - 1, 0, -1):
        # 최댓값인 arr[0]와 마지막 원소를 교환
        arr[0], arr[i] = arr[i], arr[0]
        # arr[0] ~ arr[i - 1]을 힙으로 만들기
        heapify(arr, 0, i - 1)
    
heap_sort(array)
print(array)