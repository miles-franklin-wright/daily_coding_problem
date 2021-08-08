# Timelimit = under an hour
# Remaining (after each stop) =  40min
# 
# Good morning! Here's your coding interview problem for today.

# This problem was asked by Google.

# A unival tree (which stands for "universal value") is a tree where all nodes under it have the same value.

# Given the root to a binary tree, count the number of unival subtrees.

# For example, the following tree has 5 unival subtrees:

#    0
#   / \
#  1   0
#     / \
#    1   0
#   / \
#  1   1


# to do = 1. learn about unival trees 2. learn how they work in Python 3. learn how to interact with them in python

# NOTES 
# Looks like there's a lot of stuff out here on this already. May have the answer given to me
# 
# Universal value tree = children same as parents. Empty tree is a unival tree. 1 = 1, 2 is not though. Non empty unival trees would cover all those that do have values below (?)
# In the above, leftmost 1, the bottom 1s, the rightmost 0, and the whole 1 1 1 structure, are all unival trees => meaning that they can include subtrees without any child values
# tree has bunch of nodes, each node consists of the following class structure. Left and right are children of the Node. 
# class Node {
#   int value
#   Node left
#   Node right
# }
# dude will give his solution in a second, so I will try to figure out now
# how to cycle through 
# how to check the nodes
# parameters for checking nodes
# if Node right && Node left == int value => return true
# node = new Node (instantiate class)
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 