# -- 트리 문제 유형 -- 
# 트리 구현 문제 
# 트리 순회 문제

## ------ 문제 ------
# 문제에서 이진트리 하나와 해당 트리에 속한 두 개의 노드가 주어진다. 이 때, 두 노드의 공통 조상 중
# 가장 낮은 node 즉, the lowest common ancestor (LCA)를 찾아라. (값이 낮다는 게 아님)

## ------ 제약조건 -------
# 2 <= node 개수 <= 10^5 --> 전체 트리의 수가 n개 일때, 전체를 순회하는데 O(n) 따라서 시간 초과 X
# -10^9 <= Node.val <= 10^9 --> 4byte(int)는 -2^31 ~ 2^31-1까지 표현할 수 있다. 따라서 문제 X
# 모든 Node.val은 unique하다
# p != q
# p, q는 모두 주어진 트리에 속해 있다

# class Node :
#     def __init__(self, value=0, left=None, right=None) :
#         self.value = value
#         self.left = left
#         self.right = right

# class BinaryTree :
#     def __init__(self) :
#         self.root = None

# bt = BinaryTree()


def LCA(root, p, q) :
    if root == None : 
        return None
    
    left = LCA(root.left, p, q) # 정보를 갖춘 뒤(left, right) 아래에서 결정 (조건문)
    right = LCA(root.right, p, q) 

    if root == p or root == q :
        return root
    
    elif left and right : 
        return root 
    
    return left or right #(left, right가 모두 None이면 None을 반환)
    # 한쪽이 None, 다른 한쪽이 None이 아니라면 None이 아닌 값을 반환

print(LCA([3,5,1,6,2,0,8, None,None, 7,4], 6,4 ))