from dAryHeap import *
from cyaron import *

d = input("Please enter d for the dAryHeap!\n")
a = Vector.random(20, [(1, 100)], 1)
input = sum(a, [])
myHeap = dAryHeap(int(d), input)
myHeap.printHeap()
for i in range(1, 11):
    myHeap.increaseKey(i, i + 90)
    myHeap.printHeap()
for i in range(1, 11):
    myHeap.insert(i * 10)
    myHeap.printHeap()
myHeap.heapSort()
myHeap.printHeap()
myHeap.buildMaxHeap()
while(not myHeap.isEmpty()):
    myHeap.extractMax()
    myHeap.printHeap()
