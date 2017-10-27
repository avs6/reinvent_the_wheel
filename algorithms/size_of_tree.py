class Node:
    value=None
    left=None
    right=None
    def __init__(self, value, left, right):
        self.value=value
        self.left=left
        self.right=right

#      10
#    5    15
#  1   7
one=Node(1,None,None)
seven=Node(7,None,None)
five = Node(5, one, seven)
fifteen = Node(15, None, None)
ten = Node(10, five, fifteen)

def size_of_tree(root):
    if(root!=None):
        size = size_of_tree(root.left) + size_of_tree(root.right) + 1;
        return size
    elif(root==None):
        return 0

print(size_of_tree(ten))
