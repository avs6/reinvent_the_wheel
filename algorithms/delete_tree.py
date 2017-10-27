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
one = Node(1,None,None)
seven = Node(7,None,None)
five = Node(5, one, seven)
fifteen = Node(15, None, None)
ten = Node(10, five, fifteen)

# root : delete the left child, delete the right child and then make root node None
def delete_tree(root):
    if(root!=None):
        delete_tree(root.left)
        delete_tree(root.right)
        root.value=None;

def preorder_traverse(root):
    if(root!=None):
        print(root.value)
        preorder_traverse(root.left)
        preorder_traverse(root.right)

preorder_traverse(ten)
delete_tree(ten)
preorder_traverse(five)
preorder_traverse(ten)