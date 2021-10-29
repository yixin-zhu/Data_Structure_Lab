import time
DELETED = [-2]
EMPTY = [-1]


def h1(k, m):
    return k % m


def h2(k, m):
    return 1 + k % (m-1)


def double(k, i, m):
    return (h1(k, m)+i*(h2(k, m))) % m


def ChineseHash(s):
    result = 0
    for i in range(0, len(s)):
        result *= 100000
        result += (ord(s[i]))
    return result


class HashTableDouble:
    __table = []
    __size = 0
    searchTime = 0

    def __init__(self, size):
        self.__size = size
        self.__table = [EMPTY]*(self.__size)

    def printTable(self):
        print("Current table is")
        print(self.__table)

    def insert(self, item):
        k = ChineseHash(item[0])
        for i in range(0, self.__size):
            j = double(k, i, self.__size)
            if(self.__table[j] == EMPTY or self.__table[j] == DELETED):
                self.__table[j] = item
                return j
        print("hash table overflow!")
        return -1

    def insertList(self, input):
        for item in input:
            self.insert(item)

    def search(self, key):
        k = ChineseHash(key)
        for i in range(0, self.__size):
            j = double(k, i, self.__size)
            if(self.__table[j][0] == key):
                print("Successfully find")
                print(self.__table[j])
                self.searchTime = (i+1)
                return j
            if(self.__table[j] == EMPTY):
                break
        print("Can't find ", end='')
        print(key)
        return -1

    def testSearch(self, key):
        begin = time.time_ns()
        self.search(key)
        end = time.time_ns()
        diff = end - begin
        print("The time use of searching is ", end="")
        print(diff)
        print("Search number is ", end="")
        print(self.searchTime)

    def testSearchList(self, keys):
        print("Begin to search list!")
        totalTime = 0
        totalI = 0
        for key in keys:
            begin = time.time_ns()
            self.search(key[0])
            end = time.time_ns()
            diff = end - begin
            totalTime = totalTime + diff
            totalI = totalI + self.searchTime
        print("The time use of searching list is ", end="")
        print(totalTime)
        print("Overall search number is ", end="")
        print(totalI)

    def delete(self, key):
        index = self.search(key)
        if(index == -1):
            print("and nothing to delete")
            return
        self.__table[index] = DELETED
        print("and successfully delete")
