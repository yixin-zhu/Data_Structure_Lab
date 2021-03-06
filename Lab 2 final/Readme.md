# 2021秋数据结构   
## Lab2各文件功能与运行说明   
#### 朱奕新 19307090029
***

本次实验中，选择使用C++和Python语言，两种语言都完成了两种题设算法，故共有四段矩阵乘法核心代码。您可以在实验报告“report.pdf”文件中快速阅读核心代码，或在“Matrix.cpp”或"main.py" 文件中阅读完整代码。

实验中两种矩阵乘法算法运行时间的比较与分析，只在同种编程语言前提之下进行。

report.pdf 文件是本次lab的实验报告的内容，包括了各个矩阵乘法算法的核心代码、对不同算法的理论分析和实验结果，请您阅读。

“Python相关”文件夹中的improve.py文件是基于助教老师的提醒进行的算法改进，不再把矩阵整体补全为2的幂次，而只在切割矩阵需要时增大1边长，应当更优。它的地位等同于main.py文件，但由于Lab时间限制，没有测试它的运行时间。不过其同样有计时工具，不难完成测试，相关部分留待进一步探索。
***
## C++部分代码相关介绍和说明

### 编译运行环境

Ubuntu 20.04.3 

g++ version 9.3.0 


### 编程语言
C++ （核心矩阵乘法、测试运行时间、输入输出定向）

Python （随机数据生成）

###说明

1. 本程序生成随机数据，需要用到python的cyaron库,请您安装。在已有python的前提下，您可以使用`pip`命令获取CYaRon：`pip install cyaron` 

2. 保存“C++相关”文件夹，并在命令行下打开此文件夹

3. Matrix.cpp 文件是核心代码。用Matrix类实现了两种不同类型的矩阵乘法，还重载了加减等运算符。

4. main.cpp使用了Matrix类，测试了不同算法的矩阵乘法的运行时间。输入`g++ main.cpp -o a` 并回车来编译它。为节省时间，本文件夹下已有编译好的a文件，因此可以跳过本步。

5. generator.py负责生成指定种类和数量的数据。输入`python generator.py`命令来运行它。您会被要求输入方阵的规模N。它会自动生成随机的矩阵用于相乘。其实Matrix.cpp中的算法实现不仅限于方阵，要测试其他形状的矩阵，只需简单修改代码的测试部分即可。

6. 接着输入 `./a` 命令运行此可执行文件，它会自动读入刚刚生成的data.in文件中的数据，运算后相关信息输出到data.out文件。

7. 在data.out文件，您可以查看不同矩阵算法的运行时间。

***

## Python部分代码相关介绍和说明

### 编译运行环境

Windows 10

Python 3.9.1


### 编程语言

Python （核心矩阵乘法、测试运行时间、随机数据生成、统计图绘制）

###说明

1. 本程序生成随机数据，需要用到python的numpy库,请您安装。在已有python的前提下，您可以使用`pip`命令获取CYaRon：`pip install numpy` 

2. 保存“Python相关”文件夹，并在命令行下打开此文件夹。

3. Main.cpp 文件是核心代码。用ordinaryMulti()和strassenMulti()实现了两种不同类型的矩阵乘法，还包括随机矩阵生成、打印统计图的功能。

5. 输入`python main.py`命令来运行它。您会被要求输入方阵的规模N。其实实现的算法实现不仅限于方阵，要测试其他形状的矩阵，只需简单修改代码的测试部分即可。

6. 接着程序会自动生成相应规模的两个矩阵用于相乘。

7. 在控制台，您可以查看不同矩阵算法的运行时间。

***
全部代码在笔者的电脑上测试通过，如果在您的设备上出现意料之外的错误，请联系电话：18358425535
