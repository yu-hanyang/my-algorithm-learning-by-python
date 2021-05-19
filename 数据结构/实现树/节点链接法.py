class BinaryTree:#构建一个二叉树类
    def __init__(self,rootObj):
        self.key=rootObj
        self.leftChild=None
        self.rightChild=None

    def insertLeft(self,newNode):
        if self.leftChild==None:
            self.leftChild=BinaryTree(newNode)
        else:
            t=BinaryTree(newNode)
            t.leftChild=self.leftChild
            self.leftChild=t

    def insertRight(self,newNode):
        if self.rightChild==None:
            self.rightChild=BinaryTree(newNode)
        else:
            t=BinaryTree(newNode)
            t.rightChild=self.rightChild
            self.rightChild=t

    def getRightChild(self):
        return self.rightChild

    def getLeftChild(self):
        return self.leftChild

    def setRootVal(self,Obj):
        self.key=Obj

    def getRootVal(self):
        return self.key

    def preorder(self):
        print(self.key)
        if self.rightChild:
            self.rightChild.preorder()
        if self.leftChild:
            self.leftChild.preorder()
            
#尝试调用二叉树类
r=BinaryTree('a')
print(r)
r.insertLeft('b')
r.insertRight('c')
r.getRightChild().setRootVal('helllo')
r.getLeftChild().insertRight('d')
print(r.getLeftChild().getRightChild().getRootVal())