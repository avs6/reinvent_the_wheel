class Node :
    data = None;
    next = None;
    def __init__(self, data, next_node=None):
        self.data = data;
        self.next = next_node;

def insert (head_node, value):
    node = head_node;
    if (node != None):
        while (node.next != None):
            node=node.next;
        node.next = Node (value);
        return head_node;
    return Node( value);

def read_all_nodes (head_node):
    node = head_node;
    while (node != None):
        print (node.data);
        node = node.next;
    return node;
head_node = insert (None, 5);
head_node = insert (head_node, 6);
head_node = insert (head_node, 7);
read_all_nodes(head_node);