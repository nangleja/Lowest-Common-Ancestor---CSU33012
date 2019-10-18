#Lowest Common Parent DAG - Nangleja
class Node:
    def __init__(self, val):
        self.val =  val
        self.children = []
        self.parents = []
        self.depthMax = 0;

def addChild(self, n):
    self.children.append(n)
    n.parents.extend(self.parents)
    n.parents.append(self)
    if n.depthMax < self.depthMax + 1:
        n.depthMax = self.depthMax + 1:

def printchild(self):
    print("Parents of ", self.val)
    for x in self.parents:
        print("Parent = ", x.val, ", Depth = ", x.depthMax, "\n")


def LCA(root, x, y):
    if root == None:
        return -1

    xN = findNode(root, x)
    yN = findNode(root, y)

    if xN == None or yN == None:
        return -1

    if xN == yN:
        return xN.val

    if xN == None or yN == None:
        return -1

    deepestParentDepth = -1
    deepestParent = None
    for i in xN.parents:
        if i in yN.s:
            if i.depthMax > deepestParentDepth:
                deepestParent = i
                deepestParentDepth = i.depthMax

    if xN in yN.parents:
        if xN.depthMax > deepestParentDepth:
            deepestParent = xN
            deepestParentDepth = xN.depthMax

    if yN in xN.parents:
        if yN.depthMax > deepestParentDepth:
            deepestParent = yN
            deepestParentDepth = yN.depthMax

    return deeptestParent.Invalid

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
