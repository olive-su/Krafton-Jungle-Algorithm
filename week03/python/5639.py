# time : 

import sys

input = sys.stdin.readline
arr = []
tree = {} # 부모 노드, 왼쪽 자식, 오른쪽 자식
arr = []
root = None

while True:
    try:
        command = int(input())
        tree[command] = [None, None, None]
        if root == None: root = command # 루트 노드 저장
        arr.append(command)
    except:
        break    

# 트리 생성
parent = None
for i in range(len(arr) - 1): # i의 자식노드 기입, i + 1의 부모 노드 기입
    now_node = arr[i]
    next_node = arr[i + 1]
    if next_node < now_node: # 왼쪽 노드
        parent = now_node
        
        tree[parent][1] = next_node
    else:
        if now_node < next_node < parent: # 오른쪽 노드
            parent = now_node
        else:
            while parent < next_node:
                if parent == root: break # 루트노드의 경우 부모노드가 없으므로 중단
                if next_node < tree[parent][0] or tree[parent][2] != None:
                    break
                parent = tree[parent][0] 
        tree[parent][2] = next_node
    
    tree[next_node][0] = parent

print(tree)
print(len(tree))

# 후위 순회
def postorder(target):
    if tree[target][1] != None:
        postorder(tree[target][1])
    if tree[target][2] != None:
        postorder(tree[target][2])
    print(target)

postorder(root)