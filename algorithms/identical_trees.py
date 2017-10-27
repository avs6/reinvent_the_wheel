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

def preorder(root):
    return preorder_(root, [])
def preorder_(root, pre_order_list):
    if(root!=None):
        pre_order_list.append(root.value)
        preorder_(root.left,pre_order_list)
        preorder_(root.right,pre_order_list)
    return pre_order_list

def inorder(root):
    return inorder_(root, [])
def inorder_(root, in_order_list):
    if(root!=None):
        inorder_(root.left, in_order_list)
        in_order_list.append(root.value)
        inorder_(root.right, in_order_list)
    return in_order_list

def identical_trees(root1, root2):
    pre_root1, in_root1=preorder(root1), inorder(root1)
    pre_root2, in_root2=preorder(root2), inorder(root2)
    print(in_root1)
    if (pre_root1==pre_root2 and in_root1==in_root2):
        return True
    else:
        return False

print(identical_trees(ten,ten))
