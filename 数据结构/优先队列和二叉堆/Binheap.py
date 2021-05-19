class Binheap:
    def __init__(self):
        self.heapList=[]
        self.currentSize=0

    def percUp(self,i):
        while i//2>0:
            if self.heapList[i]<self.heapList[i//2]:
                tmp = self.heapList[i//2]
                self.heapList[i//2] = self.heapList[i]
                self.heapList[i] = tmp
            else:break
            i=i//2

    def percDown(self,i):
        while (i*2) <= self.currentSize:
            mc = self.minChild(i)
            if self.heapList[i] > self.heapList[mc]:
                tmp = self.heapList[mc]
                self.heapList[mc] = self.heapList[i]
                self.heapList[i] = tmp
            i = mc

    def minChild(self,i):
        if i*2+1>self.currentSize:#唯一子节点
            return i*2
        else:
            #返回较小的
            if self.heapList[i*2] < self.heapList[i*2+1]:
                return i*2
            else:
                return i*2+1

    def delMin(self):
        retval = self.heapList[1]
        self.heapList[1] =self.heapList[self.currentSize]
        self.currentSize-=1
        self.heapList.pop()
        self.percDown(1)
        return  retval

    def insert(self,k):
        self.heapList.append(k)
        self.currentSize+=1
        self.percUp(self.currentSize)

    def builHeap(self,alist):
        i = len(alist)//2
        self.currentSize = len(alist)
        self.heapList = [0] + alist
        print(len(self.heapList),i )
        while i > 0:
            print(self.heapList,i)
            self.percDown(i)
            i-=1
        print(self.heapList,i)