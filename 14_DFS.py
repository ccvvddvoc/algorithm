# DFS는 스택, 재귀 두 가지 방법으로 구현 가능하다

# DFS by recursion
# 접근과 방문은 다르다 ! 

# DFS 접근
def dfs(cur_node) : 
    if cur_node is None :
        return 
    dfs(cur_node.left)
    dfs(cur_node.right)

# 방문의 종류
# 1) 전위순회 (preorder)
# 2) 중위순회 (inorder)
# 3) 후위순회 (postorder)
# -> 접근 순서는 모두 같다

# 전위순회 : 자식 노드를 방문하기 전에 자기 자신을 먼저 방문
# 자기 자신 -> left child -> right child 순으로 방문
def preorder(cur_node) :
    if cur_node is None : 
        return
    print(cur_node.value)
    preorder(cur_node.left)
    preorder(cur_node.right)

# 중위순회 : left child -> 자기 자신 -> right child 순으로 방문
# left, right는 바뀌어도 상관 X
def inorder(cur_node) :
    if cur_node is None : 
        return
    inorder(cur_node.left)
    print(cur_node.value)
    inorder(cur_node.right)

# 후위순회 : left child -> right child -> 자기 자신 순으로 방문
# left, right는 바뀌어도 상관 X
def postorder(cur_node) :
    if cur_node is None :
        return
    postorder(cur_node.left)
    postorder(cur_node.right)
    print(cur_node.value)

# 전위순회 : A B D G H E C F
# 중위순회 : G D H B E A C F
# 후위순회 : G H D E B F C A