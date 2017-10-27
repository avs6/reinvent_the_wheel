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

def bst_to_dcll(root):
    # lets take 1 2 3 :
    # recurse left
    # recurse right
    # right.left.right is left
    # left.left is right.left
    # left.left.right is root and root.left is left.right
    # right.left is root and root.right is right
    if(root!=None):
        left_dcll = bst_to_dcll(root.left);
        right_dcll = bst_to_dcll(root.right);
        # storing left and rights end nodes
        if(left_dcll==None):
            left_dcll=root
        if(right_dcll==None):
            right_dcll=root

        left_dcll_end_node = left_dcll.left if (left_dcll.left) else root
        right_dcll_end_node = right_dcll.left if( right_dcll.left) else root

        #making circular link
        left_dcll.left=right_dcll.left
        right_dcll_end_node.right=left_dcll

        # linking root to left and right
        left_dcll_end_node.right=root
        root.left=left_dcll_end_node
        right_dcll.left=root
        root.right=right_dcll

        return left_dcll;
    else:
        return None;

def print_circular_ll(root):
    node=root;
    print(node.value)
    if(node!=None):
        while(node.right!=root):
            print(node.right.value)
            node=node.right

root_dcll = bst_to_dcll(one)
print_circular_ll(root_dcll)


