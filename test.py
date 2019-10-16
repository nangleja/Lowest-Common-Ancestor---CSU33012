import unittest
import node
import sys


class test_node(unittest.TestCase):

# Basic Binary Tree For Test No.1
#                     1
#                    / \
#                   /   \
#                  2     \
#                 / \      3
#                4   5    / \
#                   / \  6   \
#                 /    \      7
#                8     9
#

    def test_basicTree(self):
        root = node.Node(1)
        root.left = node.Node(2)
        root.right = node.Node(3)
        root.left.left = node.Node(4)
        root.left.right = node.Node(5)
        root.right.left = node.Node(6)
        root.right.right = node.Node(7)
        self.assertEqual(2, node.LCA(root, 4, 5))

# Test No.2 - Null Tree
    def test_nullTree(self):
        root = None
        self.assertEqual(-1, node.LCA(root, 4, 5), 'Empty tree returns -1')

#Test No.3 - Invalid Node
    def test_InvalidNode(self):
        root = node.Node(1)
        root.left = node.Node(2)
        root.right = node.Node(3)
        root.left.left = node.Node(4)
        root.left.right = node.Node(5)
        root.right.left = node.Node(6)
        root.right.right = node.Node(7)
        root.left.left.left = node.Node(8)
        self.assertEqual(-1, node.LCA(root, 4, 9), "Unfound node returns -1")

#Test No.4 Common Ancestor is the Node

    def test_commonAncestorIsNode(self):
        root = node.Node(1)
        root.left = node.Node(2)
        root.right = node.Node(3)
        root.left.left = node.Node(4)
        root.left.right = node.Node(5)
        root.right.left = node.Node(6)
        root.right.right = node.Node(7)
        root.left.left.left = node.Node(8)
        self.assertEqual(2, node.LCA(root, 2, 4), "Common Ancestor of 2 & 4 is 2 itself")
        self.assertEqual(2, node.LCA(root, 2, 2), "Common Ancestor of 2 & 2 is 2 itself")
        self.assertEqual(2, node.LCA(root, 4, 2), "Common Ancestor of 4 & 2 is 2 itself")



if __name__ == '__main__':
    unittest.main()
