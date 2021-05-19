def quickSort(alist):
    quickSortHelper(alist, 0, len(alist) - 1)


def quickSortHelper(alist, first, last):
    if first < last:
        splitpoint = partition(alist, first, last)
        quickSortHelper(alist, first, splitpoint - 1)
        quickSortHelper(alist, splitpoint + 1, last)

def partition(alist, first,last):
    piovtvalue = alist[first]#选定中值

    #左右标初值
    leftmark = first+1
    rightmark = last


    done = False

    while not done:
        while leftmark <= rightmark and alist[leftmark] <= piovtvalue:
            leftmark+=1

        while rightmark >= leftmark and alist[rightmark] >= piovtvalue:
            rightmark-=1

        if rightmark < leftmark:
            done = True
        else:
            temp = alist[leftmark]
            alist[leftmark] = alist[rightmark]
            alist[rightmark] = temp

    temp = alist[first]
    alist[first] = alist[rightmark]
    alist[rightmark] = temp

    return rightmark

alist = [54,26,93,17,77,31,44,55,20]
quickSort(alist)
print(alist)

