#Lowest Common Ancestor DAG - Nangleja
class Node:
    def __init__(self, val):
        self.val =  val
        self.left = None
        self.right = None
        self.travelled = False;

def findPath( root, path, k):

    if root is None:
        return False

    path.append(root.val)

    if root.val == k :
        return True

    if ((root.left != None and findPath(root.left, path, k)) or
            (root.right!= None and findPath(root.right, path, k))):
        return True


    path.pop()
    return False

def LCA(root, x, y):
    if(root is not None):
        if(root.left is None and root.right is None and (x is not y)):
            return -1
    return LCARecursive(root, x, y, [False], [false])

def LCARecursive(root, x, y, path1, path2):
    if(root is none):
        return -1

    if(root.travelled is True):
        return -1

    left = LCARecursive(root.left, x, y, path1, path2)
    right = LCARecursive(root.right, x, y, path1, path2)

    if(root.val is x):
        path[0]=True
        return root.val

    if(path1[0] if True and path2[0] is True):
        if(left is not -1 and right is not -1):
            return root.val
        elif(left is not -1):
            return left
        else
            return right
    if(left is not -1):
        return left
    if(right is not -1):
        return right

    return -1
