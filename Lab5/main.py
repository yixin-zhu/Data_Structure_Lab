from HashTableDouble import *
from HashTableLinear import *
import csv
import math


def isPrime(x):
    for i in range(2, math.ceil(math.sqrt(x))):
        if(x % i == 0):
            return False
    return True


def nextPrime(n):
    k = n
    while(not isPrime(k)):
        k = k + 1
    return k


def readInCsv():
    input = []
    with open('data.csv', 'r') as d:
        people = csv.reader(d)
        for person in people:
            input.append(person)
        del input[0]  # 去除第一行即表头
        return(input)


students = readInCsv()
length = nextPrime(15*len(students))  # 双重散列法中，表长要取素数
myTable = HashTableDouble(length)
myTable.insertList(students)
myTable.testSearchList(students)
'''
下面是search()函数和delete()函数功能的测试，将代码移出注释即可观看测试结果
myTable.search('李艳')
myTable.search('董淑英')
myTable.search('张华华')
myTable.delete('董淑英')
myTable.delete('刘红')
myTable.delete('王晨')
myTable.search('李艳')
myTable.search('董淑英')
myTable.search('张华华')
'''
'''
下面是用线性探查法实现的散列表的测试，将代码移出注释即可观看测试结果
Table2 = HashTableLinear(len(students))
Table2.insertList(students)
Table2.testSearchList(students)
Table2.search('李艳')
Table2.search('董淑英')
Table2.search('张华华')
Table2.delete('董淑英')
Table2.delete('刘红')
Table2.delete('王晨')
Table2.search('李艳')
Table2.search('董淑英')
'''
