class Node:
    value=None
    left=None
    right=None
    def __init__(self, value, left, right):
        self.value=value
        self.left=left
        self.right=right

#       15
#     10  5
#    7  3
seven = Node(7, None, None)
three = Node(3, None, None)
five = Node(5, None, None)
ten = Node(10, seven, three)
fifteen = Node(15, ten, five)


def children_sum_property(root):
    # left recurse
    # right recurse
    # if left and right are true and sum of children is equal to roo then return root
    if(root!=None):
        if(root.left==None and root.right==None):
            return True
        left_property = children_sum_property(root.left)
        right_property = children_sum_property(root.right)
        left_node_value = root.left.value if (root.left!=None) else 0
        right_node_value = root.right.value if (root.right!=None) else 0
        if(left_property and right_property):
            if(root.value==left_node_value+right_node_value):
                return True
            else:
                return False
        else:
            return False
    else:
        return False

print(children_sum_property(fifteen))