class Node:
    value=None
    left=None
    right=None
    def __init__(self, value, left, right):
        self.value=value
        self.left=left
        self.right=right

    def __repr__(self):
        return str(self.value)

#      10
#    5    15
#  1   7
one=Node(1,None,None)
seven=Node(7,None,None)
five = Node(5, one, seven)
fifteen = Node(15, None, None)
ten = Node(10, five, fifteen)

def print_stuff(result):
    for item in result:
        print(str(item[0:])[1:-1])

def all_paths_to_leafs_(root, paths, my_path):
    # if left and right are both None then add the my_path to paths
    # all_paths_to_leafs_ left append root and pass it in to left
    # all_paths_to_leafs_ right append root and pass it in to right
    # append left and right
    if (root!=None):
        if (root.left == None and root.right == None):
            my_path.append(root)
            paths.append(list(my_path))
            return paths
        else:
            my_path.append(root)
            left_paths=all_paths_to_leafs_(root.left, list(paths), list(my_path))
            right_paths=all_paths_to_leafs_(root.right, list(paths), list(my_path))
            merged_paths=left_paths + right_paths
            return merged_paths
    else:
        return None

def all_paths_to_leafs(root):
    return all_paths_to_leafs_(root, [], [])

result = all_paths_to_leafs(ten)
print_stuff(result)
