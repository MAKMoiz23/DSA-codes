class TreeNode:
    def __init__(self,data, left=None ,right=None):
        self.data=data
        self.left=left
        self.right=right

class BST:
    def __init__(self, root=None):
        self.root=root

    def Insert(self, x, value):
        if self.root is None:
            self.root = TreeNode(value)
            return

        if value == x.data:
            return

        if value > x.data:
            #go right
            if x.right:
                self.Insert(x.right,value)
            else:
                x.right = TreeNode(value)

        elif value < x.data:
            #go left
            if x.left:
                self.Insert(x.left, value)
            else:
                x.left = TreeNode(value)

    def PreOrder(self, x):
        ele=[]

        ele.append(x.data)

        if x.left:
            ele += self.PreOrder(x.left)

        if x.right:
            ele += self.PreOrder(x.right)

        return ele


    def InOrder(self, x):
        ele = []

        if x.left:
            ele += self.InOrder(x.left)

        ele.append(x.data)

        if x.right:
            ele += self.InOrder(x.right)

        return ele

    def PostOrder(self, x):
        ele = []

        if x.left:
            ele += self.PostOrder(x.left)

        if x.right:
            ele += self.PostOrder(x.right)

        ele.append(x.data)

        return ele

    def Height(self, x):
        if x is None:
            return 0

        else:
            lDepth = self.Height(x.left)
            rDepth = self.Height(x.right)

            if (lDepth > rDepth):
                return lDepth + 1
            else:
                return rDepth + 1


    def FindMin(self, x):
        if x is None:
            return
        while x:
            if x.left is None:
                return x.data
            x=x.left

    def MinNode(self, x):
        if x is None:
            return
        while x:
            if x.left is None:
                return x
            x=x.left

    def FindMax(self, x):
        if x is None:
            return
        while x:
            if x.right is None:
                return x
            x = x.right

    def Successor(self, x):
        if x.right is None:
            return

        x = x.right
        while x:
            if x.left is None:
                return x.data
            x=x.left

    def Predecessor(self, x):
        if x.left is None:
            return

        x = x.left
        while x:
            if x.right is None:
                return x.data
            x = x.right

    def Delete(self, root, x):
        if root is None:
            return root

        if x < root.data:
            root.left = self.Delete(root.left, x)
        elif (x > root.data):
            root.right = self.Delete(root.right, x)

        else:
            if root.left is None:
                temp = root.right
                root = None
                return temp

            elif root.right is None:
                temp = root.left
                root = None
                return temp

            temp = self.MinNode(root.right)
            root.data = temp.data
            root.right = self.Delete(root.right, temp.data)

        return root

if __name__=='__main__':
    b=BST()
    b.Insert(b.root, 78)
    b.Insert(b.root, 65)
    b.Insert(b.root, 90)
    b.Insert(b.root, 72)
    b.Insert(b.root, 79)
    b.Insert(b.root, 68)
    b.Insert(b.root, 75)
    b.Insert(b.root, 69)
    b.Insert(b.root, 73)
    b.Insert(b.root, 77)
    # print(b.PreOrder(b.root))
    print(b.InOrder(b.root))
    print(b.PostOrder(b.root))
    # print(b.Height(b.root))
    # print(b.FindMin(b.root))
    # print(b.FindMax(b.root))
    # print(b.Successor(b.root))
    # print(b.Predecessor(b.root))
    # b.Delete(b.root, 8)
    # print(b.PreOrder(b.root))