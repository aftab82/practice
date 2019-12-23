class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def traverse(root, nodes):
    if root:
        traverse(root.left, nodes)
        traverse(root.right, nodes)
        nodes.append(str(root.val))
    else:
        nodes.append('#')

    return nodes


def serialize(root):
    nodes = []
    traverse(root, nodes)
    coded = ','.join(nodes)
    return coded


def deserialize(data):
    nodes = data.split(',')
    for node in nodes:
        root = Node(node)
    return nodes


"""
tree:
           1
          / \
         2   3
            / \          
           4   5
[1, 2, None, None, 3, 4, None, None, 5, None, None]
"""

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.right.left = Node(4)
root.right.right = Node(5)

coded = serialize(root)
print(coded)
print(deserialize(coded))
