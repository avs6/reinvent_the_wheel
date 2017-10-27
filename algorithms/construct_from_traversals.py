class Node:
    value=None
    left=None
    right=None
    def __init__(self, value, left, right):
        self.value=value
        self.left=left
        self.right=right

def get_min_index(inorder, preorder):
    if(len(inorder)!=0):
        i=0
        min_index=inorder[i]
        while(i<len(inorder)-1):
            min_index = min_index if(preorder.index(min_index) < preorder.index(inorder [i+1])) else inorder[i+1]
            i=i+1
        return min_index
    else:
        return None

def construct_from_in_and_pre(inorder, preorder):
    # get the element in inorder with least index in preorder
    # construct_from_in_and_pre for everything to left in inorder, and preorder
    # construct_from_in_and_pre for everything to right in inorder and preorder
    # create node with left and right
    if(len(inorder)!=0 and len(preorder)!=0):
        root_value = get_min_index(inorder, preorder)
        if (root_value!=None):
            min_index = inorder.index(root_value)
            left_root=construct_from_in_and_pre(inorder[0:min_index], preorder)
            right_root=construct_from_in_and_pre(inorder[min_index+1:len(inorder)], preorder)
            root_node=Node(root_value,left_root,right_root)
            return root_node;
        else:
            return None

def preorder(root):
    if(root!=None):
        print(root.value)
        preorder(root.left)
        preorder(root.right)

root = construct_from_in_and_pre([1,2,3,4,5],[4,2,1,3,5])
preorder(root)