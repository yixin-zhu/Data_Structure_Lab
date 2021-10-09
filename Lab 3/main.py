postfix = ["9", "3", "7", "*", "+", "4", "5", "*", "6", "+", "2", "*", "+"]

priority = {"**": 13, "~": 12, "*": 11, "/": 11, "mod": 11, "%": 11, "//": 11,
            "+": 10, "-": 10, "<<": 9, ">>": 9, "&": 8,  "^": 7, "|": 7, "<=": 6, "<": 6,
            ">": 6, ">=": 6, "<>": 5, "==": 5, "!=": 5, "not": 1, "!": 1, "and": 1, "&&": 1, "or": 1,
            "||": 1, "{": 0, "(": 0}

pair = {"}": "{", ")": "("}


class Stack:
    __s = []

    def __init__(self):
        self.__s = []

    def push(self, x):
        self.__s.append(x)

    def top(self):
        return self.__s[-1]

    def pop(self):
        return self.__s.pop()

    def empty(self):
        return len(self.__s) == 0

    def size(self):
        return len(self.__s)


def readExpression():
    s = input(
        "Please enter a valid expression! Use blank to seperate numbers and operators.\n")
    myExpression = s.split()
    return myExpression


def isFloat(num):
    for everyChar in num:
        if(everyChar == "."):
            return True
    return False


def convert(infix):
    opeStack = Stack()
    result = []
    for t in infix:
        if ((t[0] >= "0" and t[0] <= "9") or (t[0] == "-" and len(t) > 1)):
            result.append(t)
        elif(t == "True" or t == "False"):
            result.append(int(t))
        elif(opeStack.empty() or t == "(" or t == "{"):
            opeStack.push(t)
        elif(t == ")" or t == "}"):         # 右括号部分
            while(opeStack.top() != pair[t]):
                temp = opeStack.pop()
                result.append(temp)
            opeStack.pop()          # 消除左括号
        else:
            while(not opeStack.empty() and priority[opeStack.top()] >= priority[t]):
                temp = opeStack.pop()
                result.append(temp)
            opeStack.push(t)
    while(not opeStack.empty()):
        result.append(opeStack.pop())
    return result


def calculate(postfix):
    calStack = Stack()
    for t in postfix:
        if ((t[0] >= "0" and t[0] <= "9") or (t[0] == "-" and len(t) > 1)):
            if(isFloat(t)):
                calStack.push(float(t))
            else:
                calStack.push(int(t))
        else:
            y = calStack.pop()
            x = calStack.pop()
            if(t == "+"):
                calStack.push(x + y)
            elif(t == "-"):
                calStack.push(x - y)
            elif(t == "*"):
                calStack.push(x * y)
            elif(t == "/"):
                if(y == 0):
                    return "Error! Division by zero!"
                calStack.push(x / y)
            elif(t == "mod"):
                if(y == 0):
                    return "Error! Division by zero!"
                calStack.push(x % y)
            elif(t == "%"):
                if(y == 0):
                    return "Error! Division by zero!"
                calStack.push(x % y)
            elif(t == "~"):
                calStack.push(x)
                calStack.push(~ y)
            elif(t == "not"):
                calStack.push(x)
                calStack.push(not y)
            elif(t == "!"):
                calStack.push(x)
                calStack.push(not y)
            elif(t == "**"):
                calStack.push(x ** y)
            elif(t == "//"):
                if(y == 0):
                    return "Error! Division by zero!"
                calStack.push(x // y)
            elif(t == "<"):
                calStack.push(x < y)
            elif(t == "<="):
                calStack.push(x <= y)
            elif(t == ">"):
                calStack.push(x > y)
            elif(t == ">="):
                calStack.push(x >= y)
            elif(t == "=="):
                calStack.push(x == y)
            elif(t == "!="):
                calStack.push(x != y)
            elif(t == "<>"):
                calStack.push(x != y)
            elif(t == "<<"):
                calStack.push(x << y)
            elif(t == ">>"):
                calStack.push(x >> y)
            elif(t == "&"):
                calStack.push(x & y)
            elif(t == "^"):
                calStack.push(x ^ y)
            elif(t == "|"):
                calStack.push(x | y)
            elif(t == "and"):
                calStack.push(x and y)
            elif(t == "&&"):
                calStack.push(x and y)
            elif(t == "or"):
                calStack.push(x or y)
            elif(t == "||"):
                calStack.push(x or y)
    return calStack.top()


infix = readExpression()
postfix = convert(infix)
print("The postfix is ")
for x in postfix:
    print(x, end="")
    print(" ", end="")
print("\n")
print("The result is ", end="")
print(calculate(postfix))
