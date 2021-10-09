from cyaron import *


def generateInt(size):
    test_data = IO("data.in", "data.out")
    a = Vector.random(size, [(0, 1000000)], 1)
    test_data.input_writeln(a)
    test_data.output_gen("intSort.exe")


def generateFloat(size):
    test_data = IO("data.in", "data.out")
    a = Vector.random(size, [(0, 1000000)], 2)
    test_data.input_writeln(a)
    test_data.output_gen("floatSort.exe")
  
def generateStr(size):
    test_data = IO("data.in", "data.out")
    a = String.random_sentence(size)
    test_data.input_writeln(a)
    test_data.output_gen("stringSort.exe")
  

def generate(type, size):
    if type == 1:
        generateInt(size)
    elif type == 2:
        generateFloat(size)
    elif type == 3:
        generateStr(size)


type = input("Please enter data's type. 1:int 2:float 3:str\n")
size = input("Please enter data's size.\n")
type = int(type)
size = int(size)
generate(type, size)
