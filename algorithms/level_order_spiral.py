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

def level_order_spiral(root):
    # node put in queue
    # while first node not None
    # put left and right in queue when direction_flag is True
    # put right and left in queue when direction_flag is False
    node=root
    queue=[node]
    direction_flag=True
    while(queue[0]!=None):
        node_under_prcessing = queue.pop(0)
        print(node_under_prcessing.value)
        if(direction_flag==True):
            queue.append(node_under_prcessing.left)
            queue.append(node_under_prcessing.right)
        else:
            queue.append(node_under_prcessing.right)
            queue.append(node_under_prcessing.left)
        direction_flag= not direction_flag

level_order_spiral(ten)

