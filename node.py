#Lowest Common Parent DAG - Nangleja
class Node:
    def __init__(self, val):
        self.val =  val
        self.children = []
        self.parents = []
        self.maxDepth = 0

    def addChild(self, n):
        self.children.append(n)
        n.parents.extend(self.parents)
        n.parents.append(self)
        if n.maxDepth < self.maxDepth + 1:
            n.maxDepth = self.maxDepth + 1

    def printparents(self):
        print("Aarents of ", self.val)
        for x in self.parents:
            print("Parent = ", x.val, ", Depth = ", x.maxDepth, "\n")



def LCA(root, x, y):
    if root == None:
        return -1

    if root.parents != []:
        return -1



    xN = findNode(root, x)
    yN = findNode(root, y)

    if xN == None or yN == None:
        return -1

    if xN == yN:
        return xN.val

    if xN == None or yN == None:
        return -1

    deepestAncestorDepth = -1
    deepestAncestor = None
    for i in xN.parents:
        if i in yN.parents:
            if i.maxDepth > deepestAncestorDepth:
                deepestAncestor = i
                deepestAncestorDepth = i.maxDepth

    if xN in yN.parents:
        if xN.maxDepth > deepestAncestorDepth:
            deepestAncestor = xN
            deepestAncestorDepth = xN.maxDepth

    if yN in xN.parents:
        if yN.maxDepth > deepestAncestorDepth:
            deepestAncestor = yN
            deepestAncestorDepth = yN.maxDepth

    #Need method to iterate through ancestry


    return deepestAncestor.val

def findNode(node, val):
    if node.val == val:
        return node
    elif len(node.children) != 0:
        for x in node.children:
            n = findNode(x,val)
            if n != None:
                return n
    else:
        return None
