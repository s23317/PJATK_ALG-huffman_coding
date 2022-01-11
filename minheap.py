# https://favtutor.com/blogs/heap-in-python
def min_heap(A, k):
    l = left(k)
    r = right(k)
    if l < len(A) and A[l] < A[k]:
        smallest = l
    else:
        smallest = k
    if r < len(A) and A[r] < A[smallest]:
        smallest = r
    if smallest != k:
        A[k], A[smallest] = A[smallest], A[k]
        min_heap(A, smallest)


def left(k):
    return 2 * k + 1


def right(k):
    return 2 * k + 2


def build_min_heap(A):
    global heapsize
    heapsize = len(A) - 1

    n = int((len(A) // 2) - 1)
    for k in range(n, -1, -1):
        min_heap(A, k)


def heap_deq(A):
    global heapsize
    if heapsize < 1:
        return A.pop()
    smallest, A[0] = A[0], A.pop()
    heapsize -= 1
    min_heap(A, 0)
    return smallest


def heap_enq(A, k):
    A.append(k)
    build_min_heap(A)
