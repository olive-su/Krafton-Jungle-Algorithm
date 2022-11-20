class FixedStack:

    class Empty(Exception): # 빈 배열 접근 시
        pass

    class Full(Exception): # 가득 찬 배열 접근 시
        pass

    def __init__(self, capacity): # 스택 초기화
        self.stack = [None] # 스택 본체
        self.capacity = capacity # 스택 크기
        self.ptr = 0 # 스택 포인터

    def __len__(self): # 스택에 들어있는 데이터 개수
        return self.ptr

    def is_empty(self): # 스택이 비어 있는지 판단(bool)
        return self.ptr <= 0
    
    def is_full(self): # 스택이 가득 차 있는지 판단(bool)
        return self.ptr >= self.capacity
    
    def push(self, value): # 스택에 요소 삽입
        if self.is_full():
            raise FixedStack.Full
        self.stack[self.ptr] = value
        self.ptr += 1

    def pop(self): # 스택에서 데이터 꺼냄
        if self.is_empty():
            raise FixedStack.Empty
        self.ptr -= 1
        return self.stack[self.ptr]
    
    def peek(self): # 스택의 top요소 확인
        if self.is_empty():
            raise FixedStack.Empty
        return self.stack[self.ptr - 1]
   
    def clear(self): # 스택의 모든 데이터 삭제
        self.ptr = 0

    def find(self, value): # 스택에서 value를 찾아 인덱스를 반환 
        for i in range(self.ptr - 1, -1, -1):
            if self.stack[i] == value:
                return i
        return -1

    def count(self, value): # 스택에 있는 value의 개수를 반환
        c = 0
        for i in range(self.ptr):
            if self.stack[i] == value:
                c += 1
        return c
    
    def __contains__(self, value): # 스택에 value가 있는지 판단
        return self.count(value)
    
    def dump(self): # 스택 안의 모든 데이터를 바닥부터 꼭대기 순으로 출력
        if self.is_empty():
            print('스택이 비어 있습니다.')
        else:
            print(self.stack[:self.ptr])


