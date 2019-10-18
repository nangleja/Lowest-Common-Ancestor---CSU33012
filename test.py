#Software Engineering Part A - LCA testing
#Nangleja - 17338145
import unittest
import node


class test_node(unittest.TestCase):

# Basic Binary Tree For Test No.1
#                     1
#                   /  \
#                  /    \
#                 2      3
#                / \    / \
#               4   5  6   7
#
# Test No.1 - Basic test case

    def test_basicTree(self):
        root = node.Node(1)
        root.left = node.Node(2)
        root.right = node.Node(3)
        root.left.left = node.Node(4)
        root.left.right = node.Node(5)
        root.right.left = node.Node(6)
        root.right.right = node.Node(7)
        self.assertEqual(1, node.lowestCommonAncestor(root, 4, 3))
        self.assertEqual(1, node.lowestCommonAncestor(root, 2, 7))
        self.assertEqual(3, node.lowestCommonAncestor(root, 6, 7))

# Test No.2 - Null Tree
    def test_nullTree(self):
        root = None
        self.assertEqual(-1, node.lowestCommonAncestor(root, 4, 5), 'Empty tree returns -1')

#Test No.3 - Invalid Node
    def test_InvalidNode(self):
        root = node.Node(1)
        root.left = node.Node(2)
        root.right = node.Node(3)
        root.left.left = node.Node(4)
        root.left.right = node.Node(5)
        root.right.left = node.Node(6)
        root.right.right = node.Node(7)
        self.assertEqual(-1, node.lowestCommonAncestor(root, 4, 9), "Unfound node returns -1")

#Test No.4 Common Ancestor is the Node

    def test_commonAncestorIsNode(self):
        root = node.Node(1)
        root.left = node.Node(2)
        root.right = node.Node(3)
        root.left.left = node.Node(4)
        root.left.right = node.Node(5)
        root.right.left = node.Node(6)
        root.right.right = node.Node(7)
        self.assertEqual(2, node.lowestCommonAncestor(root, 2, 4))
        self.assertEqual(2, node.lowestCommonAncestor(root, 2, 2))
        self.assertEqual(2, node.lowestCommonAncestor(root, 4, 2))

#Test No.5 Extreme inputs

    def test_extremeInputValues(self):
        root = node.Node(-9223372036854775800)
        root.left = node.Node(1.6)
        root.right = node.Node(1.7)
        root.left.left = node.Node(1.9)
        root.left.right = node.Node(300000)
        root.right.left = node.Node(400000)
        root.right.right = node.Node(9223372036854775800)
        self.assertEqual(-9223372036854775800, node.lowestCommonAncestor(root, 1.6, 1.7))
        self.assertEqual(1.7, node.lowestCommonAncestor(root, 400000, 9223372036854775800))

#Test No.6 Root is only node

    def test_rootIsNodeOnly(self):
        root = node.Node(1)
        self.assertEqual(1, node.lowestCommonAncestor(root, 1, 1))



if __name__ == '__main__':
    unittest.main()
