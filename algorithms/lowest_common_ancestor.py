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

def lowest_common_ancestor_(root, node1, node2):
    if(root!=None):
        if(node1==None or node2==None):
            raise "the seach node can not be None"
        if(node1.value<root.value and node2.value<root.value):
            return lowest_common_ancestor_(root.left, node1, node2)
        elif(node1.value>root.value and node2.value>root.value):
            return lowest_common_ancestor_(root.right, node1, node2)
        elif(node1.value<=root.value and node2.value>=root.value):
            return root
    else:
        return None
def lowest_common_ancestor(root, node1, node2):
    # this is a binary search tree 1 and 5
    # if both nodes are smaller than root, lca of left
    # if both are larger, go recurse right
    # if one is smaller or equal and one is larger or equal, then that's it.
    smaller_node=node1 if (node1.value<node2.value) else node2
    larger_node=node1 if (smaller_node.value==node2.value) else node2
    return lowest_common_ancestor_(root, smaller_node, larger_node)

print(lowest_common_ancestor(ten, five, fifteen).value)
print(lowest_common_ancestor(ten, one, one).value)
print(lowest_common_ancestor(ten, one, seven).value)