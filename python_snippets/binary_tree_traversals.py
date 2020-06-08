class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


def print_inorder(root):
    if root:
        print_inorder(root.left)
        print(root.val)
        print_inorder(root.right)


def print_preorder(root):
    if root:
        print(root.val)
        print_preorder(root.left)
        print_preorder(root.right)


def print_postorder(root):
    if root:
        print_postorder(root.left)
        print_postorder(root.right)
        print(root.val)


"""Create below tree:
     tree
     ----
     1    <-- root
    / \ 
   2   3  
  / \  
 4   5

"""

root = Node(25)
root.left = Node(15)
root.left.left = Node(10)
root.left.left.left = Node(4)
root.left.left.right = Node(12)
root.left.right = Node(22)
root.left.right.left = Node(18)
root.left.right.right = Node(24)
root.right = Node(50)
root.right.left = Node(35)
root.right.left.left = Node(31)
root.right.left.right = Node(44)
root.right.right = Node(70)
root.right.right.left = Node(66)
root.right.right.right = Node(90)


print("inorder:")
print_inorder(root)
print("preorder:")
print_preorder(root)
print("postorder:")
print_postorder(root)

