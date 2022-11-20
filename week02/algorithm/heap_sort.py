
def heap_sort(arr):
    def down_heap(arr, left, right):
        temp = arr[left]

        parent = left # 왼쪽 노드를 부모로 설정
        while parent < (right + 1) // 2: # 힙으로 만드려는 범위를 넘어가는 지 검사
            cl = parent * 2 + 1 # 왼쪽 자식이 들어갈 인덱스
            cr = cl + 1 # 오른쪽 자식이 들어갈 인덱스
            # 자식 노드 중 큰 값을 child에 담음
            if cr <= right and arr[cr] > arr[cl]: # 자식 노드의 균형이 맞는 경우 (left_child < right_child)
                child = cr
            else: # 자식 노드의 균형이 안맞는 경우 (left_child > right_child) or 부모 - 자식 쌍 x
                child = cl
            
            if temp >= arr[child]: # 부모 노드가 자식 노드보다 큰 경우(힙 균형 상태 OK)
                break
            # 부모 노드가 자식 노드보다 작은 경우
            arr[parent] = arr[child] # 자식 노드와 부모 노드 위치 swap
            parent = child # 새로운 부모 노드(인덱스) 설정
        arr[parent] = temp

    n = len(arr)

    for i in range((n - 1) // 2, -1, -1): # 절반 위치부터 진행
        down_heap(arr, i, n - 1) # 현재 ~ 마지막 인덱스
    
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        down_heap(arr, 0, i - 1)

heap_sort([1, 2, 4, 4, 3, 5, 5, 6])
