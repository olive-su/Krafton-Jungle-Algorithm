class Node:
    
    '''
    @key : 키
    @vale : 값
    @left : 왼쪽 자식 포인터
    @right : 오른쪽 자식 포인터
    '''
    def __init__(self, key, value, left, right):
        self.key = key
        self.value = value
        self.left = left
        self.right = right

class BinarySearchTree:
    # 노드가 없는 상태의 이진 검색 트리 초기화
    def __init__(self):
        self.root = None 


    # 검색(순환적 형태)
    def interative_search(self, key):
        p = self.root
        while True:
            if p is None:
                return None
            if key == p.key:
                return p.value
            elif key < p.key:
                p = p.left
            else:
                p = p.right

    # 검색(재귀적 형태)
    def recursive_search(self, key):
        p = self.root
        if p is None:
            return None
        if key < p.key:
            return recursive_search(p.left, key)
        else: return recursive_search(p.right, key)

    # 삽입
    def add(self, key, value):
        def add_node(node, key, value):
            if key == node.key:
                return False
            elif key < node.key:
                if node.left is None:
                    node.left = Node(key, value, None, None)
                else:
                    add_node(node.left, key, value)
            else:
                if node.right is None:
                    node.right = Node(key, value, None, None)
                else:
                    add_node(node.right, key, value)
            
            return True

        if self.root is None: # 루트 노드가 빈 상태일 경우
            self.root = None(key, value, None, None)
            return True
        else:
            return add_node(self.root, key, value)

    '''
    @p : 현재 스캔 중인 노드
    @parent : p의 부모 노드
    @is_left_child : p가 parent의 왼쪽 자식 노드인지
    '''
    def remove(self, key):
        p = self.root
        parent = None
        is_left_child = True

        # 삭제하려는 노드 검색
        while True:
            if p is None: # 해당 키가 트리 내에 존재하지 않음
                return False
            
            if key == p.key: # 키와 동일한 노드 검색 완료
                break
            else:
                parent = p # 가지를 내려가므로 부모 노드의 포인터를 자식 노드로 변경
                if key < p.key:
                    is_left_child = True
                    p = p.left
                else:
                    is_left_child = False
                    p = p.right
        
        # CASE 2
        if p.left is None: # 왼쪽 자식이 없는 경우 / CASE 1이 이루어지는 부분
            if p is self.root:
                self.root = p.right
            elif is_left_child:
                parent.left = p.right
            else:
                if p is self.root:
                    self.root = p.right
                elif is_left_child:
                    parent.left = p.right
                else:
                    parent.right = p.right
        elif p.right is None: # 오른쪽 자식이 없는 경우
            if p is self.root:
                self.root = p.left
            elif is_left_child:
                parent.left = p.left
            else:
                parent.right = p.left
        
        # CASE 3
        else:
            parent = p
            left = p.left
            is_left_child = True
            while left.right is not None: # 왼쪽 서브트리 내에서 가장 큰 노드를 검색
                parent = left
                left = left.right
                is_left_child = False
            
            p.key = left.key # swap
            p.value = left.value
            if is_left_child:
                parent.left = left.left
            else:
                parent.right = left.left
        return True