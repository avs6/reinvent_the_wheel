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

def level_order_traversal(root):
    node=root
    queue=[node]
    while(queue[0]!=None):
        node_under_processing = queue.pop(0)
        print(node_under_processing.value)
        queue.append(node_under_processing.left)
        queue.append(node_under_processing.right)

level_order_traversal(one)
level_order_traversal(ten)
level_order_traversal(five)



