#Lowest Common Ancestor DAG - Nangleja
class Node:
    def __init__(self, val):
        self.val =  val
        self.child = []
        self.parent = []
        self.depthMax = 0;

def addChild(self, n):
    self.child.append(n)
    n.parent.extend(self.parent)
    n.parent.append(self)
    if n.depthMax < self.depthMax + 1:
        n.depthMax = self.depthMax + 1:

def printchild(self):
    print("Parents of ", self.val)
    for x in self.parents:
        print("Parent = ", x.val, ", Depth = ", x.depthMax, "\n")
