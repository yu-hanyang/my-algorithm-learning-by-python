def BinaryTree(r):#构造一个只有根节点的二叉树
    return [r,[],[]]

def insertLeft(root,newBranch):#在根节点与左子树中间插一个节点
    t=root.pop(1)
    # if len(t)>1:
    root.insert(1,[newBranch,t,[]])
    # else:root.insert(1,[newBranch,[],[]])
    return root

def insertRight(root,newBranch):#在根节点与右子树中间插一个节点
    t=root.pop(2)
    # if len(t)>1:
    root.insert(2,[newBranch,[],t])
    # else:root.insert(2,[newBranch,[],[]])
    return root

def getRootVal(root):
    return root[0]

def setRootVal(root,newVal):
    root[0]=newVal

def getLeftChild(root):
    return root[1]

def getRightChild(root):
    return root[2]

#尝试构建
r=BinaryTree(3)
insertLeft(r,4)
insertLeft(r,5)
insertRight(r,6)
insertRight(r,7)
l=getLeftChild(r)
print(l)

setRootVal(l,9)
print(r)
insertLeft(l,11)
print(r)
print(getRightChild(getRightChild(r)))

