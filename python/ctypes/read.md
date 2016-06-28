# 用python ctypes调用动态链接库

[引用](http://blog.chinaunix.net/uid-20393955-id-345449.html)
ctypes使得python能够直接调用c语言开发的动态链接库，非常强大。
为了使用CTypes，你必须依次完成以下步骤：
> -  编写动态连接库程序
> - 载入动态连接库
> - 将Python的对象转换为ctypes所能识别的参数
> - 使用ctypes的参数调用动态连接库中的函数

来个简单的实例吧：
======

### 1. 编写动态链接库

```C
// filename: foo.c
#include <stdio.h>
char* myprint(char *str)
{
    puts(str);
    return str;
}

float add(float a, float b)
{
    return a + b;
}
```


以上foo.c代码，linux下编译为动态链接库文件，命令是：
Shell 代码

```
gcc -fPIC -shared foo.c -o foo.so
```


### 2. ctypes调用

Python 代码

```python
 #!/usr/bin/env python
# FILENAME: foo.py

from ctypes import *

foo = CDLL('./foo.so')

myprint = foo.myprint
myprint.argtypes = [POINTER(c_char)]   # 参数类型，为char指针  
myprint.restype = c_char_p   # 返回类型，同样为char指针  
res = myprint('hello')
print res

add = foo.add
add.argtypes = [c_float, c_float] # 参数类型，两个float（c_float内ctypes类型）
add.restype = c_float
print add(1.3, 4.2)
```


文档请参考http://docs.python.org/library/ctypes.html

### 3. 查找链接库

Python 代码
```
   >>> from ctypes.util import find_library  
    >>> find_library("m")  
   'libm.so.6'  
    >>> find_library("c")  
    'libc.so.6'  
    >>> find_library("bz2")  
    'libbz2.so.1.0'  
    >>>  
```
```
>>> from ctypes.util import find_library
>>> find_library("m")
'libm.so.6'
>>> find_library("c")
'libc.so.6'
>>> find_library("bz2")
'libbz2.so.1.0'
>>>

```

调用libc里的printf：

Python 代码
``` python
   #filename: printf_example.py  
 
   import ctypes  
   from ctypes.util import find_library  
   printf = ctypes.CDLL(find_library("c")).printf  
   printf("hello, world\n")   
   
 ```
