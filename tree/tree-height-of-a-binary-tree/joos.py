def height(root):
    if not root:
        return -1
    return max(1 + height(root.left), 1 + height(root.right))
