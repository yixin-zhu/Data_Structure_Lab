def parent(i, d):
    return (i-1) // d


def nthChild(i, n, d):
    return d*i + n


class dAryHeap:
    __d = 2
    __heap = []
    __size = 0

    def __init__(self, newD, newHeap):
        self.__d = newD
        self.__heap = newHeap
        self.__size = len(self.__heap)
        self.buildMaxHeap()

    def findLargest(self, i):
        largest = i
        for j in range(1, self.__d + 1):
            child = nthChild(i, j, self.__d)
            if(child < self.__size):
                if(self.__heap[child] > self.__heap[largest]):
                    largest = child
            else:
                break
        return largest

    def isEmpty(self):
        return self.__size == 0

    def maxHeapify(self, i):
        largest = self.findLargest(i)
        if(i != largest):
            self.__heap[i], self.__heap[largest] = self.__heap[largest], self.__heap[i]
            self.maxHeapify(largest)

    def buildMaxHeap(self):
        for i in range(parent(self.__size-1, self.__d), -1, -1):
            self.maxHeapify(i)

    def heapSort(self):
        self.buildMaxHeap()
        for i in range(len(self.__heap)-1, 0, -1):
            self.__heap[0], self.__heap[i] = self.__heap[i], self.__heap[0]
            self.__size = self.__size - 1
            self.maxHeapify(0)
        self.__size = len(self.__heap)

    def maximum(self):
        return self.__heap[0]

    def extractMax(self):
        if(self.__size < 1):
            print("Error! Heap underflow!")
            return
        maxn = self.__heap[0]
        self.__size = self.__size - 1
        t = self.__heap.pop()
        if(self.__size > 0):
            self.__heap[0] = t
        self.maxHeapify(0)
        return maxn

    def increaseKey(self, i, key):
        if(self.__heap[i] < key):
            self.__heap[i] = key
            while(i > 0):
                pa = parent(i, self.__d)
                if(self.__heap[pa] < self.__heap[i]):
                    self.__heap[i], self.__heap[pa] = self.__heap[pa], self.__heap[i]
                    i = pa
                else:
                    break

    def insert(self, key):
        self.__heap.append(-99999999)
        self.__size = self.__size + 1
        self.increaseKey(self.__size - 1, key)

    def printHeap(self):
        print("Current heap is")
        print(self.__heap)
