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

def get_all_leaves(root, leaves):
    # if left and right are nNone then 1
    # recurse left + recurse right and reutrn it
    if(root!=None):
        if(root.left == None and root.right ==  None):
            leaves.append(root)
            return leaves
        else:
            left_leaves = get_all_leaves(root.left, list(leaves))
            right_leaves = get_all_leaves(root.right, list(leaves))
            total_leaves = left_leaves + right_leaves
            return total_leaves
    else:
        return leaves

def print_nodes(items):
    for item in items:
        print(item.value)

def number_of_nodes_between_two_nodes(root, node1, node2):
    # get root to node1 path
    # get root to node2 path
    # go next until the nodes are not equal
    # that node to None in node1 path +  that node to None in node2 path
    if(root!=None):
        root_to_node1=root_to_node_(root, node1)
        root_to_node2=root_to_node_(root, node2)

        print("result1")
        for item in root_to_node1:
            print(item.value)

        print("result2")
        for item in root_to_node2:
            print(item.value)
        lca=None
        for item1, item2 in zip(root_to_node1, root_to_node2):
            if(item1.value == item2.value):
                lca=item1
            else:
                break
        lca_index1 = root_to_node1.index(lca)
        lca_index2 = root_to_node2.index(lca)

        width_between_nodes = len(root_to_node1)-lca_index1 -1 + len(root_to_node2)-lca_index2  -1
        return width_between_nodes
    else:
        return -1

# print(number_of_nodes_between_two_nodes(ten, one, seven))
# for item in get_all_leaves(ten, []):
#     print(item.value)
