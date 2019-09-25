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

### 正确运行输出示例

```shell
1569436649.6920297
```

## 2

### 描述

传递给`max()`一个列表, 会返回列表中的最大值, 但问题是这个不应被改动的列表的顺序
改变了.

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

### 正确运行输出示例

```shell
9 is The max element in [3, 1, 4, 7, 9]
```