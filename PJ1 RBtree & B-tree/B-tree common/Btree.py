class Dic:
    def __init__(self, nkey, npart, nfrequency):
        self.key = nkey
        self.part = npart
        self.frequency = nfrequency


class Bnode:
    def __init__(self):
        self.parent = None
        self.dics = []   # 用来放Dic类的引用
        self.child = []  # 用来放Bnode类的引用
        self.child.append(None)

    def lookUp(self, k):
        r = -1
        for i in range(0, len(self.dics)):
            if(k >= self.dics[i].key):
                r = i
            else:
                break
        return r


class Btree:
    def __init__(self, newOrder):
        self.__order = newOrder  # order是B树的阶数
        self.root = Bnode()
        self.__last = None

    def order(self):
        return self.__order

    def empty(self):
        return (not self.root)

    def inOrderWalkCur(self, now, ans):
        if(now is not None):
            for i in range(0, len(now.dics)):
                self.inOrderWalkCur(now.child[i], ans)
                temp = []
                temp.append(now.dics[i].key)
                temp.append(now.dics[i].part)
                temp.append(now.dics[i].frequency)
                ans.append(temp)
            self.inOrderWalkCur(now.child[len(now.dics)], ans)

    def inOrderWalk(self):
        now = self.root
        ans = []
        self.inOrderWalkCur(now, ans)
        print(ans)

    def levelOrderWalk(self):
        q = []
        answer = []
        q.append(self.root)
        while(len(q) > 0):
            t = q.pop(0)
            temp = []
            for i in range(0, len(t.dics)):
                temp.append(t.dics[i].key)
            answer.append(temp)
            for i in range(0, len(t.child)):
                if(t.child[i] is not None):
                    q.append(t.child[i])
        print(answer)

    def find(self, k):
        v = self.root
        self.__last = None
        while(v is not None):
            r = v.lookUp(k)
            if(r >= 0 and k == v.dics[r].key):
                return v
            self.__last = v
            v = v.child[r+1]
        return None

    def insertFixup(self, x):
        if(len(x.child) <= self.__order):
            return
        r = self.__order // 2
        u = Bnode()
        for i in range(0, self.__order - r - 1):
            u.child.insert(i, x.child[r+1])
            x.child.pop(r + 1)
            u.dics.insert(i, x.dics[r+1])
            x.dics.pop(r + 1)
        u.child[self.__order - r - 1] = x.child.pop(r + 1)
        for j in range(0, self.__order-r):
            if(u.child[j] is not None):
                u.child[j].parent = u
        p = x.parent
        if(p is None):
            p = Bnode()
            self.root = p
            p.child[0] = x
            x.parent = p
        t = 1 + p.lookUp(x.dics[0].key)
        p.dics.insert(t, x.dics[r])
        x.dics.pop(r)
        p.child.insert(t+1, u)
        u.parent = p
        if(len(p.child) > self.__order):
            self.insertFixup(p)

    def insert(self, k, p, f):
        d = Dic(k, p, f)
        now = self.find(k)
        if(now is not None):
            print('Key', k,  'conflict')
            return False
        r = self.__last.lookUp(k)
        self.__last.dics.insert(r + 1, d)
        self.__last.child.insert(r + 2, None)
        self.insertFixup(self.__last)
        return True

    def deleteFixup(self, x):
        if((self.__order+1)//2 <= len(x.child)):
            return
        p = x.parent
        if(p is None):
            if(len(x.dics) == 0 and (x.child[0] is not None)):
                self.root = x.child[0]
                self.root.parent = None
                x.child[0] = None
            return
        r = 0
        while(p.child[r] != x):
            r = r + 1              # x 是父亲的第r个孩子
        if(r > 0):  # case 1
            lb = p.child[r-1]
            if((self.__order+1)//2 < len(lb.child)):  # 左兄弟有余力借出一个
                x.dics.insert(0, p.dics[r-1])
                p.dics[r-1] = lb.dics.pop(len(lb.dics)-1)
                x.child.insert(0, lb.child.pop(len(lb.child)-1))
                if(x.child[0] is not None):
                    x.child[0].parent = x
        if(r < len(p.child)-1):  # case 2
            rb = p.child[r+1]
            if((self.__order+1)//2 < len(rb.child)):  # 右兄弟有余力借出一个
                x.dics.insert(len(x.dics), p.dics[r])
                p.dics[r] = rb.dics.pop(0)
                if(rb.child[0] is not None):
                    rb.child[0].parent = x
                x.child.append(rb.child.pop(0))
        if(r > 0):  # case 3
            lb = p.child[r-1]  # 左兄弟存在但他也没有余力，只好和他合并了
            lb.dics.append(p.dics.pop(r-1))
            p.child.pop(r)  # x和父亲断开连接
            lb.child.append(x.child.pop(0))
            if(lb.child[len(lb.child)-1] is not None):
                lb.child[len(lb.child)-1].parent = lb
            while(len(x.dics) > 0):
                lb.dics.append(x.dics.pop(0))
                lb.child.append(x.child.pop(0))
                if(lb.child[len(lb.child)-1] is not None):
                    lb.child[len(lb.child)-1].parent = lb
        else:  # case 4 由于左右兄弟至少有一个存在，所以一定会落入这里
            rb = p.child[r+1]  # 右兄弟存在但他也没有余力，只好和他合并了
            rb.dics.insert(0, p.dics.pop(r))
            p.child.pop(r)  # x和父亲断开连接
            rb.child.insert(0, x.child.pop(len(x.child)-1))
            if(rb.child[0] is not None):
                rb.child[0].parent = rb
            while(len(x.dics) > 0):
                rb.dics.insert(0, x.dics.pop(len(x.dics)-1))
                rb.child.insert(0, x.child.pop(len(x.child)-1))
                if(rb.child[0] is not None):
                    rb.child[0].parent = rb
        self.deleteFixup(p)  # 递归修复
        return

    def delete(self, k):
        v = self.find(k)
        if(v is None):
            print('Key', k, 'missing')
            return False
        r = v.lookUp(k)
        if(v.child[0] is not None):
            u = v.child[r+1]
            while(u.child[0] is not None):
                u = u.child[0]
            v.dics[r] = u.dics[0]
            v = u
            r = 0
        v.dics.pop(r)
        v.child.pop(r+1)
        self.deleteFixup(v)
        return True

    def readIn(self, fileName):
        input = []
        f = open(fileName)
        lines = f.readlines()
        f.close()
        for line in lines:
            line = line.strip('\n')
            lineDiv = line.split(" ")
            input.append(lineDiv)
        del input[0]  # 去除第一行即表头
        return input

    def insertByFIle(self, fileName):
        input = self.readIn(fileName)
        for item in input:
            self.insert(item[0], item[1], item[2])
        print("Insert by file OK")

    def initialByFile(self, fileName):
        self.root = Bnode()
        self.__last = None
        input = self.readIn(fileName)
        for item in input:
            self.insert(item[0], item[1], item[2])
        print("Initialization by file OK")

    def deleteByFile(self, fileName):
        input = self.readIn(fileName)
        for item in input:
            self.delete(item[0])
        print("Delete by file OK")

    def update(self, k, p, f):
        x = self.find(k)
        if(x is None):
            self.insert(k, p, f)
        else:
            x.part = p
            x.frequency = f

    def search(self, k):
        x = self.find(k)
        if(x is None):
            print("Key", k,  "missing")
        else:
            print(x.part, x.frequency)
