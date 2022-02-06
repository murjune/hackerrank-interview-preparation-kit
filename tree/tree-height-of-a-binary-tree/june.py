def height(root):
    
    if root == None:
        return -1
    
    left = height(root.left)
    right = height(root.right)
    cnt = max(left, right) + 1
    
    return cnt
