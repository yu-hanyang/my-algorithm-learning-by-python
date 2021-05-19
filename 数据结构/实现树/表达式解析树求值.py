import operator
def evaluate(parsTree):
    opers = {'+':operator.add,'-':operator.sub,'*':operator.mul,'/':operator.truediv}
    leftC = parsTree.getLeftChild()
    rightC = parsTree.getRightChild()
    if leftC and rightC:
        fn = opers[parsTree.getRootVal()]
        return fn(evaluate(leftC),evaluate(rightC))
    else:return parsTree.getRootVal()