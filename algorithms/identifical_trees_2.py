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

def identical_tree(root1, root2):
    if(root1!=None and root2!=None):
        root_flag= True if (root1==root2) else False
        left_flag= identical_tree(root1.left, root2.left)
        right_flag= identical_tree(root1.right, root2.right)
        if(root_flag and left_flag and right_flag):
            return True;
        else:
            return False;
    elif(root1==None and root2==None):
        return True;
    else:
        return False;

print(identical_tree(ten, five));
print(identical_tree(ten, ten));
print(identical_tree(None, ten));

