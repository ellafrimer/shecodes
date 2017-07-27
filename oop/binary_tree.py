"""
a binary search tree is a rooted tree that can have up to two kids for etch node
"""


class TreeNode:
    def __init__(self, value, right=None, left=None):
        self.value = value
        self.right = right
        self.left = left

    def __str__(self):
        output = str(self.value) + "\n"

        if self.left is not None:
            output += "l:" + str(self.left)
        if self.right is not None:
            output += "r:" + str(self.right)

        return output

    def insert(self, value):
        if self.value > value:
            if self.left is None:
                self.left = TreeNode(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = TreeNode(value)
            else:
                self.right.insert(value)

    def search(self, value):
        if self.value == value:
            return True
        elif value > self.value:
            if self.right is None:
                return False
            return self.right.search(value)
        else:
            if self.left is None:
                return False
            return self.left.search(value)


root = TreeNode(8)
root.insert(7)
root.insert(9)
root.insert(6)
print(root)
print(root.search(6))
