from RBtree import *
from cyaron import *

myTree = RBtree()
myTree.initialByFile("init.txt")
myTree.deleteByFile("delete.txt")
myTree.insertByFIle("insert.txt")
myTree.dump()

'''
myTree.delete(key)
myTree.insert(key, part, frequency)
myTree.search(key)
myTree.update(key, part, frequency)
'''
