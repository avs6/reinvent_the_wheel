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

def height_of_tree(root):
    if(root!=None):
        left_height = height_of_tree(root.left)
        right_height = height_of_tree(root.right);
        taller_childs_height = left_height if (left_height > right_height) else right_height
        return taller_childs_height+1
    else:
        return 0;

print(height_of_tree(ten));
print(height_of_tree(five));
print(height_of_tree(None));