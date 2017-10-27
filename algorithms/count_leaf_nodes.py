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

def count_leaves(root):
    # count leaves in left and then right
    # add them up and return it
    # if a node has no left or right then, return 1
    if(root!=None):
        if(root.left==None and root.right==None):
            return 1
        else:
            left_leaves = count_leaves(root.left)
            right_leaves = count_leaves(root.right)
            return left_leaves+right_leaves+1
    else:
        return 0

print(count_leaves(five))
print(count_leaves(ten))