import numpy as np
from numpy.core.shape_base import hstack, vstack
import time


def copy(x, y):
    for i in range(y.shape[0]):
        for j in range(y.shape[1]):
            x[i][j] = y[i][j]


def ordinaryMulti(x, y):
    ans = np.zeros((x.shape[0], y.shape[1]))
    if x.shape[1] != y.shape[0]:
        print("OrdinaryMulti error!\n")
        return ans
    for i in range(x.shape[0]):
        for j in range(y.shape[1]):
            for k in range(x.shape[1]):
                ans[i][j] += (x[i][k] * y[k][j])
    return ans


def strassenMulti(x, y):
    p = max(x.shape[0], x.shape[1])
    q = max(y.shape[0], y.shape[1])
    t = max(p, q)
    if t == 1:
        ans = np.zeros((1, 1))
        ans[0][0] = x[0][0] * y[0][0]
        return ans
    w = t
    if(w % 2 == 1):
        w = w+1
    ans = np.zeros((w, w))
    if x.shape[1] != y.shape[0]:
        print("OrdinaryMulti error!\n")

    else:
        mid = w // 2
        xx = np.zeros((w, w))
        copy(xx, x)
        yy = np.zeros((w, w))
        copy(yy, y)
        a = xx[0:mid, 0:mid]
        b = xx[0:mid, mid:w]
        c = xx[mid:w, 0:mid]
        d = xx[mid:w, mid:w]
        e = yy[0:mid, 0:mid]
        f = yy[0:mid, mid:w]
        g = yy[mid:w, 0:mid]
        h = yy[mid:w, mid:w]
        P1 = strassenMulti(a, (f - h))
        P2 = strassenMulti((a + b), h)
        P3 = strassenMulti((c + d), e)
        P4 = strassenMulti(d, (g - e))
        P5 = strassenMulti((a + d), (e + h))
        P6 = strassenMulti((b - d), (g + h))
        P7 = strassenMulti((a - c), (e + f))
        r = P5 + P4 - P2 + P6
        s = P1 + P2
        t = P3 + P4
        u = P5 + P1 - P3 - P7
        ans = vstack((hstack((r, s)), hstack((t, u))))
        ans = ans[0:x.shape[0], 0:y.shape[1]]
    return ans


def testOrdinaryMulti(x, y):
    begin = time.time_ns()
    print(ordinaryMulti(x, y))
    end = time.time_ns()
    diff = end - begin
    print("The time use of Ordinary Multi is ", end="")
    print(diff)


def testStrassenMulti(x, y):
    begin = time.time_ns()
    print(strassenMulti(x, y))
    end = time.time_ns()
    diff = end - begin
    print("The time use of Ordinary Multi is ", end="")
    print(diff)


s = input("Please enter the size of the matrix!")
s = int(s)
i = s
x = np.random.randint(0, 10, (i, i))
y = np.random.randint(0, 10, (i, i))
testOrdinaryMulti(x, y)
testStrassenMulti(x, y)
