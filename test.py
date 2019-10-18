import unittest
import node
import sys

class test_node(unittest.TestCase):


    def test_NullTree(self):
        root = None
        self.assertEqual(-1, node.LCA(root, 4, 5), 'Empty tree returns -1')
        self.assertEqual(-1, node.LCA(None, 0, 0), 'Empty tree returns -1')


    def test_TreeOfOneElement(self):
        # create one element tree
        # test one element tree
        root = node.Node(1)

        self.assertEqual(node.LCA(root, 1, 2), -1, "Should return -1")
        self.assertEqual(node.LCA(root, 1, 1), 1, "Should return 1")
        self.assertEqual(node.LCA(root, 6, 7), -1, "Should return -1")

    def test_basicTree1(self):
        root = node.Node(1)
        n2 = node.Node(2)
        n3 = node.Node(3)
        n4 = node.Node(4)
        n5 = node.Node(5)
        n6 = node.Node(6)
        n7 = node.Node(7)
        root.addChild(n2)
        root.addChild(n3)
        n2.addChild(n4)
        n2.addChild(n5)
        n3.addChild(n6)
        n3.addChild(n7)

        self.assertEqual(2, node.LCA(root, 4, 5))
        self.assertEqual(1, node.LCA(root, 4, 6))


    def test_basicTree2(self):

        #See basicgraph2.jpg in github repository for visualisation!

        root = node.Node(1)
        n2 = node.Node(2)
        n3 = node.Node(3)
        n4 = node.Node(4)
        n5 = node.Node(5)
        n6 = node.Node(6)
        n7 = node.Node(7)
        n8 = node.Node(8)
        n9 = node.Node(9)
        n10 = node.Node(10)
        n11 = node.Node(11)
        n12 = node.Node(12)
        n13 = node.Node(13)
        root.addChild(n2)
        root.addChild(n3)
        n2.addChild(n4)
        n3.addChild(n5)
        n4.addChild(n6)
        n5.addChild(n7)
        n5.addChild(n8)
        n7.addChild(n10)
        n10.addChild(n9)
        n10.addChild(n13)
        n10.addChild(n11)
        n11.addChild(n12)


        self.assertEqual(5, node.LCA(root, 12, 8))
        self.assertEqual(10, node.LCA(root, 9, 12))
        self.assertEqual(1, node.LCA(root, 6, 13))

    def test_simpleDag(self):
        root = node.Node(1)
        n2 = node.Node(2)
        n3 = node.Node(3)
        n4 = node.Node(4)
        n5 = node.Node(5)
        n6 = node.Node(6)
        n7 = node.Node(7)
        n8 = node.Node(8)
        n9 = node.Node(9)
        n10 = node.Node(10)
        n11 = node.Node(11)
        n12 = node.Node(12)
        n13 = node.Node(13)
        n14 = node.Node(14)
        root.addChild(n2)
        root.addChild(n3)
        n2.addChild(n5)
        n2.addChild(n4)
        n3.addChild(n4)
        n3.addChild(n7)
        n4.addChild(n11)
        n4.addChild(n6)
        n5.addChild(n8)
        n6.addChild(n10)
        n6.addChild(n13)
        n7.addChild(n9)
        n8.addChild(n10)
        n9.addChild(n12)
        n10.addChild(n14)
        n11.addChild(n10)
        n13.addChild(n12)
        n13.addChild(n14)

        self.assertEqual(13, node.LCA(root, 12, 14))
        self.assertEqual(6, node.LCA(root, 10, 12))

if __name__ == '__main__':
    unittest.main()
