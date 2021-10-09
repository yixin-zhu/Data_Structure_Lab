# 2021秋数据结构   
## Lab1各文件功能与运行说明   
#### 朱奕新 19307090029
***
### 编译运行环境
Windows 10

mingw32

gcc version 9.2.0 

***
### 语言
C++ （核心排序算法）

Python （随机数据生成、输入输出定向）
***

### 介绍和说明

0. 本程序生成随机数据，需要用到python及其cyaron库,请您安装。在已有python的前提下，您可以使用`pip`命令获取CYaRon：`pip install cyaron`

1. 把所有源代码文件保存到本地同一文件夹中

2. 在命令行下打开此文件夹

3. report.pdf 文件是本次lab的实验报告的内容，包括三种排序方法的核心代码与对各个问题的解答。

4. Sort.cpp 文件是核心代码。用模板类Sort类实现了对不同数据类型的数据的插入排序、归并排序以及两者结合的排序。

5. intSort.cpp使用了Sort类，实现了对int数组的读入和排序。输入`g++ intSort.cpp -o intSort.exe` 并回车来编译它。为节省时间，本文件夹下已有编译好的intSort.exe文件，因此可以跳过本步。floatSort.cpp与stringSort.cpp同理。

6. generator.py负责生成指定种类和数量的数据，传给相应的exe文件。输入`python generator.py`命令来运行它。

7. 分别输入两个数字来指定数据种类和数量。要指定种类，输入1:int或2:float或3:str。要指定数量，请输入一个正整数。

8. 在data.out文件，您可以查看三个排序算法的运行时间和排好序的数组。从上至下分别对应插入排序、归并排序以及两者结合的排序。


