from minheap import *


def isLeaf(self):
    return self.character != ""


def createTree(queue):
    while len(queue) > 1:
        n1 = heap_deq(queue)
        n2 = heap_deq(queue)
        if n1 == n2 and not n1.isLeaf():
            temp = n1
            n1 = n2
            n2 = temp
        heap_enq(queue, (n1[0] + n2[0], "", n1, n2))
    return heap_deq(queue)
