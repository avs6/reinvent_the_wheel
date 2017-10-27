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

# : mirror left child, mirror right child, clone root node, clone_root link the new lefts and rights return the clone_root
# :
def mirror_tree(root):
    if(root!=None):
        left_clone = mirror_tree(root.left)
        right_clone = mirror_tree(root.right)
        root_clone = Node(root.value, left_clone, right_clone)
        return root_clone
    else:
        return None

def preorder(root):
    if(root!=None):
        print(root.value)
        preorder(root.left)
        preorder(root.right)

ten_clone = mirror_tree(ten)
preorder(ten)
preorder(ten_clone)