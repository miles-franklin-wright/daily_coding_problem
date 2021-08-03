# STATUS = unsolved as of now. Currently,  have no idea how to do this. Unfamiliar with serialization. 

# Given the root to a binary tree, implement serialize(root), which serializes the tree into a string, and deserialize(s), which deserializes the string back into the tree

# for example, given the node class:
# class Node: 
    # def __init__(self, val, left=None, right=None):
        # self.val=val
        # self.left=left
        # self.right=right
# should pass:
# node = Node('root', 
# Node('left',
# Node('left.left'))
# Node('right'))
# assert
# deserialize(serialize(node)).left.left.val =='left.left'

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# I have no idea how to do this. I will have to research more later tonight