# time : 70'
import sys

input = sys.stdin.readline
n = int(input())
tree = {}
visited = [False] * 27
inorder_arr, postorder_arr = '', ''

# 딕셔너리 초기화
for alpha in range(ord('A'), ord('Z') + 1):
    tree[chr(alpha)] = ['.', '.', '.']

# 부모 노드, 왼쪽 자식 노드, 오른쪽 자식 노드 순으로 삽입
for _ in range(n):
    p, l, r = input().split()
    tree[p][1], tree[p][2] = l, r # 자식 노드 삽입
    if l != '.':
        tree[l][0] = p # 왼쪽 자식 노드에 부모 노드 삽입
    if r != '.':
        tree[r][0] = p # 오른쪽 자식 노드에 부모 노드 삽입

left_leaf_node = 'A' # 왼쪽 단말 노드 탐색
while tree[left_leaf_node][1] != '.':
    left_leaf_node = tree[left_leaf_node][1]

def preorder(t):
    rst = t
    p, l, r = tree[t]
    if l != '.': # 왼쪽 자식 노드 
        rst += preorder(l)
    if r != '.': # 오른쪽 자식 노드 
        rst += preorder(r)
    return rst

def inorder(t):
    global inorder_arr

    p, l, r = tree[t]
    if not visited[ord(l) - ord('A')] and l != '.': # 왼쪽 자식 노드 
        inorder(l)
    visited[ord(t) - ord('A')] = True 
    inorder_arr += t
    if not visited[ord(r) - ord('A')] and r != '.': # 오른쪽 자식 노드 
        inorder(r)

def postorder(t):
    global postorder_arr

    p, l, r = tree[t]
    if not visited[ord(l) - ord('A')] and l != '.': # 왼쪽 자식 노드 
        postorder(l)
    if not visited[ord(r) - ord('A')] and r != '.': # 오른쪽 자식 노드 
        postorder(r)
    visited[ord(t) - ord('A')] = True 
    postorder_arr += t

print(preorder('A'))
visited = [False] * 27
inorder('A')
print(inorder_arr)
visited = [False] * 27
postorder('A')
print(postorder_arr)
        


