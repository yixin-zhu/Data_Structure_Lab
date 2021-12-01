RED = True
BLACK = False


class RBnode:
    def __init__(self, newKey=None, newPart=None, newFrequency=None):
        self.key = newKey
        self.part = newPart
        self.frequency = newFrequency
        self.color = BLACK
        self.left = None
        self.right = None
        self.p = None


class RBtree:
    __nil = RBnode()

    def __init__(self):
        self.root = self.__nil

    def __inorderNodeWalk(self, x):
        temp = ''
        if(x.left != self.__nil):
            temp = temp + self.__inorderNodeWalk(x.left)
        temp = temp + " ( " + str(x.key) + " " + str(x.part) + \
            " " + str(x.frequency) + " ) "
        if(x.right != self.__nil):
            temp = temp + self.__inorderNodeWalk(x.right)
        return temp

    def inorderWalk(self):
        answer = ""
        if(self.root != self.__nil):
            answer = answer + self.__inorderNodeWalk(self.root)
        return answer

    def minimum(self, x):
        t = x
        while(t.left != self.__nil):
            t = t.left
        return t

    def maximum(self, x):
        t = x
        while(t.right != self.__nil):
            t = t.right
        return t

    def uncle(self, x):
        if(x.p == x.p.p.left):
            return x.p.p.right
        elif(x.p == x.p.p.right):
            return x.p.p.left

    def find(self, k):
        x = self.root
        while(x != self.__nil and k != x.key):
            if(k < x.key):
                x = x.left
            elif(k > x.key):
                x = x.right
        return x

    def leftRotate(self, x):
        y = x.right
        x. right = y.left
        if(y.left != self.__nil):
            y.left.p = x
        y.p = x.p
        if(x.p == self.__nil):
            self.root = y
        elif(x == x.p.left):
            x.p.left = y
        else:
            x.p.right = y
        y.left = x
        x.p = y

    def rightRotate(self, y):
        x = y.left
        y. left = x.right
        if(x.right != self.__nil):
            x.right.p = y
        x.p = y.p
        if(y.p == self.__nil):
            self.root = x
        elif(y == y.p.left):
            y.p.left = x
        else:
            y.p.right = x
        x.right = y
        y.p = x

    def insertFixup(self, z):
        while(z.p.color == RED):
            y = self.uncle(z)
            if(y.color == RED):
                z.p.color = BLACK
                y.color = BLACK
                z.p.p.color = RED
                z = z.p.p
            else:
                if(z.p == z.p.p.left):
                    if(z == z.p.right):
                        z = z.p
                        self.leftRotate(z)
                    z.p.color = BLACK
                    z.p.p.color = RED
                    self.rightRotate(z.p.p)
                else:
                    if(z == z.p.left):
                        z = z.p
                        self.rightRotate(z)
                    z.p.color = BLACK
                    z.p.p.color = RED
                    self.leftRotate(z.p.p)
        self.root.color = BLACK

    def dump(self):
        return(self.inorderWalk())

    def insertNode(self, z):
        y = self.__nil
        x = self.root
        while(x != self.__nil):
            y = x
            if (z.key < x.key):
                x = x.left
            elif(z.key > x.key):
                x = x.right
            else:
                return (" Key " + str(z.key) + " conflict ")
        z.p = y
        if(y == self.__nil):
            self.root = z
        elif(z.key < y.key):
            y.left = z
        else:
            y.right = z
        z.left = self.__nil
        z.right = self.__nil
        z.color = RED
        self.insertFixup(z)
        return None

    def insert(self, k, p, f):
        z = RBnode(k, p, f)
        return self.insertNode(z)

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
        answer = ''
        input = self.readIn(fileName)
        for item in input:
            t = self.insert(item[0], item[1], item[2])
            if(t is not None):
                answer = answer + (t)
        answer = answer + (" Insert by file OK ")
        return answer

    def initialByFile(self, fileName):
        answer = ''
        input = self.readIn(fileName)
        for item in input:
            t = self.insert(item[0], item[1], item[2])
            if(t is not None):
                answer = answer + (t)
        answer = answer + (" Initial by file OK ")
        return answer

    def update(self, k, p, f):
        x = self.find(k)
        if(x == self.__nil):
            self.insert(k, p, f)
        else:
            x.part = p
            x.frequency = f
            return " update successfully "

    def search(self, k):
        x = self.find(k)
        if(x == self.__nil):
            return(" Key " + k + " missing ")
        else:
            return(" Search result : " + k + " " + x.part + " " + str(x.frequency))

    def transplant(self, u, v):
        if(u.p == self.__nil):
            self.root = v
        elif(u == u.p.left):
            u.p.left = v
        else:
            u.p.right = v
        v.p = u.p

    def deleteFixup(self, x):
        while(x != self.root and x.color == BLACK):
            if(x == x.p.left):
                w = x.p.right
                if(w.color == RED):
                    w.color = BLACK
                    x.p.color = RED
                    self.leftRotate(x.p)
                    w = x.p.right
                if(w.left.color == BLACK and w.right.color == BLACK):
                    w.color = RED
                    x = x.p
                else:
                    if(w.right.color == BLACK):
                        w.left.color = BLACK
                        w.color = RED
                        self.rightRotate(w)
                        w = x.p.right
                    w.color = x.p.color
                    x.p.color = BLACK
                    w.right.color = BLACK
                    self.leftRotate(x.p)
                    x = self.root
            else:
                w = x.p.left
                if(w.color == RED):
                    w.color = BLACK
                    x.p.color = RED
                    self.rightRotate(x.p)
                    w = x.p.left
                if(w.right.color == BLACK and w.left.color == BLACK):
                    w.color = RED
                    x = x.p
                else:
                    if(w.left.color == BLACK):
                        w.right.color = BLACK
                        w.color = RED
                        self.leftRotate(w)
                        w = x.p.left
                    w.color = x.p.color
                    x.p.color = BLACK
                    w.left.color = BLACK
                    self.rightRotate(x.p)
                    x = self.root
        x.color = BLACK

    def delete(self, i):
        z = self.find(i)
        if(z == self.__nil):
            return(' Key '+i+' missing ')
        else:
            y = z
            yOriginalColor = y.color
            if(z.left == self.__nil):
                x = z.right
                self.transplant(z, z.right)
            elif(z.right == self.__nil):
                x = z.left
                self.transplant(z, z.left)
            else:
                y = self.minimum(z.right)
                yOriginalColor = y.color
                x = y.right
                if(y.p == z):
                    x.p = y
                else:
                    self.transplant(y, y.right)
                    y.right = z.right
                    y.right.p = y
                self.transplant(z, y)
                y.left = z.left
                y.left.p = y
                y.color = z.color
        if(yOriginalColor == BLACK):
            self.deleteFixup(x)
        return None

    def deleteByFile(self, fileName):
        answer = ''
        input = self.readIn(fileName)
        for item in input:
            t = self.delete(item[0])
            if(t is not None):
                answer = answer + (t)
        answer = answer + (" Delete by file OK ")
        return answer
