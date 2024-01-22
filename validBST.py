def validBST(root):
    globalFlag=False

    def valid(node, left, right):
        '''if node.left==null and node.right==null:
            globalFlag=True'''
        if not node:
            globalFlag=True

        #recursive
        if not (node.val > left and node.val < right):
            globalFlag=False

        if valid(node.left,left,node.val) and valid(node.right,node.val,right):
            globalFlag=True

        valid(root, float("-inf"), float("inf"))
        return globalFlag

if __name__ == '__main__':
    root = [2,1,3]

    validBST(root)
            










        
