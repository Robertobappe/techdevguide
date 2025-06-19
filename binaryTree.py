class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None

tree = BinaryTree('a')
print(tree.value)
print(tree.left_child)
print(tree.right_child)