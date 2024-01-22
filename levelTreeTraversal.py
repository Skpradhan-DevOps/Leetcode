from collections import deque
class Solution:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
def level_order_traversal(root):
    # Write your code here.
    q=deque()
    res=[]
    if root is None:
        return
            
    q.append(root)
    while q:
        temp=[]
        for i in range(len(q)):
            node=q.popleft()
            temp.append(node.value)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
                
        res.append(temp)
    print(res)
    print(res[::-1])
    print([ele for ele in reversed(res)])


root=Solution(2)
root.left=Solution(5)
root.right=Solution(4)
root.left.left=Solution(0)
root.left.right=Solution(1)
root.right.left=Solution(3)
root.right.right=Solution(6)
level_order_traversal(root)
