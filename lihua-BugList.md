# 李华的BugList

## 1

### 描述

已知在Python自带的**time**模块中有一个**time()**, 以下为Python`help()`给出的描述:

```shell
Help on built-in function time in time:

time.time = time(...)
    time() -> floating point number

    Return the current time in seconds since the Epoch.
    Fractions of a second may be present if the system clock provides them.
(END)
```

尝试调用这个函数

```python
import time
print(time())
```

### 报错信息

```shell
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'module' object is not callable
```

### 期望输出示例

```shell
1569436649.6920297
```

### 原因

阅读报错信息可知错误示例中的time()做的事是调用**time**模块(module)，而我们想做的的是调用**time**模块中的**time**方法(function)

### 解决方案

```shell
import time
print(time.time())
```
或
```shell
import time as time
print(time())
```

## 2

### 描述

传递给`max()`一个列表, 会返回列表中的最大值, 但问题是这个不应被改动的列表的**顺序**改变了.

```python
def max(list):
    list.sort()
    return list[-1]


l = [3, 1, 4, 7, 9]
print(str(max(l)) + ' is ' + 'The max element in ' + str(l))
```

### 错误输出示例

```shell
9 is The max element in [1, 3, 4, 7, 9]
```

### 期望输出示例

```shell
9 is The max element in [3, 1, 4, 7, 9]
```

### 原因

TODO

### 解决方案

TODO

## 3

### 描述

这是一个很值得注意的问题. 同样有一个很明显的错误, 为什么**代码片段一能成功运行**而**代码片段二会报错**?

代码片段一

```python
i = 666
if i > 250:
    print('It works!')
else:
    print('It will never run into here')
    # then a obvious bug
    everpveqmrpm
```

代码片段二

```python
i = 666
if i > 250:
    print('It works!')
else:
    print('It will never run into here')
# then a obvious bug
everpveqmrpm
```
