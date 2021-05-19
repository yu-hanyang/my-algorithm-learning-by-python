class Stack:
    def __init__(self):
        self.items=[]

    def isEmpty(self):
        return self.items==[]

    def push(self,i):
        self.items+=i,

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def size(self):
        return len(self.items)

def parChecker(symbolString):
    s=Stack
    balanced=True
    index=0
    while index<len(symbolString) and balanced:
        symbol=symbolString[index]
        if symbol=='(':
            s.push(symbolString[index])
        else:
            if s.isEmpty():
                balanced=False
            else:
                s.pop()
        index=index+1
    if balanced and s.isEmpty():
        return True
    else:
        return False


print(parChecker('((()))'))
print(parChecker('(()'))