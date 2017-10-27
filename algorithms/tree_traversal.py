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

def preorder(root):
    if(root!=None):
        print(root.value)
        preorder(root.left)
        preorder(root.right)

def inorder(root):
    if(root!=None):
        inorder(root.left)
        print(root.value)
        inorder(root.right)

def postorder(root):
    if(root!=None):
        inorder(root.left)
        inorder(root.right)
        print(root.value)



preorder(ten)
print("******")
inorder(ten)
print("******")
postorder(ten)
