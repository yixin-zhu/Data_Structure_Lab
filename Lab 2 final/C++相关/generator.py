from cyaron import *


def generate(size):
    test_data = IO("data.in", "data.out")
    test_data.input_writeln(size)
    for i in range(size):
        a = Vector.random(size, [(1,9)],1)
        test_data.input_writeln(a)
        b = Vector.random(size, [(1,9)],1)
        test_data.input_writeln(b)


size = input("Please enter N for the Matrix.\n")
size = int(size)
generate(size)
