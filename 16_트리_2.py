# 트리 문제는 level order, postorder가 가장 자주 나옴

## ------ 문제 -------
# 문제에서 이진 트리가 하나 주어진다. 주어진 이진 트리의 최대 깊이를 반환해라

## ------- 제약조건 ---------
# 0 <= node 개수 <= 10^4 --> N^2으로 풀면 안된다
# -100 <= Node.val <= 100 --> 크게 상관없는 제약 조건
from collections import deque

class TreeNode :
    def __init__(self, l=None, r=None, v=None) :
        self.left = l
        self.right = r
        self.value = v

root = TreeNode(v=3)
root.left = TreeNode(v=9)
root.right = TreeNode(v=20)
root.right.left = TreeNode(v=15)
root.right.right = TreeNode(v=7)

## level order 풀이
def maxDepth(root) :
    max_depth = 0
    if root is None : 
        return max_depth
    q = deque()
    q.append((root, 1))

    while q : 
        cur_node, cur_depth = q.popleft()
        max_depth = cur_depth
        if cur_node.left :
            q.append((cur_node.left, cur_depth+1))
        if cur_node.right :
            q.append((cur_node.right, cur_depth+1))
    return max_depth

# ## post order 풀이
# def maxDepth(root) :
    
#     if root is None :
#         return 0
    
#     l = maxDepth(root.left)
#     r = maxDepth(root.right)

#     return max(l, r) + 1  

# print(maxDepth(root))


