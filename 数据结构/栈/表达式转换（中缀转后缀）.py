def infixToPostfix(infixexpr):
    prec={}
    prec['*']=3
    prec['/']=3
    prec['+']=2
    prec['-']=2
    prec['(']=1
    opStack=[]
    postList=[]
    tokenList=infixexpr
    for token in tokenList:
        if token in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' or token in '0123456789':
            postList.append(token)
        elif token=='(':
            opStack.append(token)
        elif token==')':
            topToken=opStack.pop()
            while topToken!='(':
                postList.append(topToken)
                topToken=opStack.pop()
        else:
            while (len(opStack)>0) and (prec[opStack[-1]]>=prec[token]):
                postList.append(opStack.pop())
            opStack.append(token)
    while len(opStack)>0:
        postList.append(opStack.pop())
    return ''.join(postList)


print(infixToPostfix('(A+B+C+D)'))
print(infixToPostfix('((A*B)+(C*D))'))