import binarytree
from binarytree import bst
# my_tree = binarytree.bst(height=3, is_perfect=True)
print(my_tree)


class Node(object):

    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def insert(self, root, node):
        if root == None:
            root == node
        if node < root.value:
            if root.left != None:
                root.left = node
            else:
                insert (root.left, node)
        elif node > root.value:
            if root.right != None:
                root.right = node

    def find(self, num):
        #return true if num in tree, else false

        if num == self.value:
            return True

        elif num < self.value and self.left:
            return self.left.find(num)
        elif num > self.value and self.right:
            return self.right.find(num)

        else:
            return False



class Tree():

    def __init__(self, root, current):
        self.root = root




tree = Tree(9)

print (tree)
