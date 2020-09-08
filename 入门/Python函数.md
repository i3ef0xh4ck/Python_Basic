
<!-- @import "[TOC]" {cmd="toc" depthFrom=1 depthTo=6 orderedList=false} -->

<!-- code_chunk_output -->

- [没有返回值的函数](#没有返回值的函数)
- [有返回值的函数](#有返回值的函数)
- [带参数的函数](#带参数的函数)
- [带参数默认值的函数](#带参数默认值的函数)
- [指定参数传递形式](#指定参数传递形式)
- [带参数列表的函数](#带参数列表的函数)
- [解包参数列表](#解包参数列表)
- [匿名函数](#匿名函数)

<!-- /code_chunk_output -->



### 没有返回值的函数

```python
def print_hello():
		print("Hello")
```

### 有返回值的函数

```python
def get_name():
    name = "xilige"
		return name
```

### 带参数的函数

```python
def add(x, y):
		return x + y
```

### 带参数默认值的函数

```python
def add(x, y=1):
		return x + y

def sum(a, b, c=1, d=2, e=3):
		return a + b + c + d + e
```

**注意**：
- 参数默认值只能放在后边，如上，不可以定义为 def sum(a, c=1, b, d=2, e=3)

- 默认值只会执行一次，这条规则在默认值为可变对象（列表、字典以及大多数类实例）时很重要。比如，下面的函数会存储在后续调用中传递给它的参数:

```python
def f(a, l=[]):
		l.append(a)
		return l

print(f(1))
print(f(2))
print(f(3))
```

这将会打印

```python
[1]
[1, 2]
[1, 2, 3]
```

因为默认值只会执行一次，都共享了同一个默认值

如果不想在后续调用之间共享默认值，可以这样写：

```python
def f(a, l=None):
		if l is None:
				l = []
		l.append(a)
		return l
```

### 指定参数传递形式

默认情况下，函数的参数传递形式可以是位置参数或是显式的关键字参数。 为了确保可读性和运行效率，限制允许的参数传递形式是有意义的，这样开发者只需查看函数定义即可确定参数项是仅按位置、按位置也按关键字，还是仅按关键字传递。

函数的定义看起来可以像是这样：

```python
def f(pos1, pos2, /, pos_or_kwd, *, kwd1, kwd2):
      -----------    ----------     ----------
        |             |                  |
        |        Positional or keyword   |
        |                                - Keyword only
         -- Positional only
```

在这里 / 和 * 是可选的。 如果使用这些符号则表明可以通过何种形参将参数值传递给函数：仅限位置、位置或关键字，以及仅限关键字。 关键字形参也被称为命名形参。

### 带参数列表的函数

使用任意数量的参数调用函数，这些参数可以包含在一个元组或字典中

```python
def print_all_elements(*array):
		for a in array:
				print(a)

def print_all_keyvalues(**kwargs):
		for a, b in kwargs:
				print(a, b)

print_all_elements(*[1,2,3,4,5])
print_all_keyvalues(**{"a": 1, "b": 2, "c": 3})
```

### 解包参数列表

内置的range()函数需要单独的start和stop参数，如range(3, 6)

但其实也可以这样调用：

```python
args = [3, 6]
range(*args)
```

同样的，字典可使用**操作符来提供关键字参数：

```python
def print_all(a, b="b", c="c"):
		print(a)
		print(b)
		print(c)

args = {"a": "a", "b": "b", "c": "c"}
print_all(**args)
```

### 匿名函数

```python
def make_incrementor(n):
		return lambda x: x + n
```

**lambda x: x + n** 调用了lambda来创建匿名函数，make_incrementor函数使用lambda来返回一个匿名函数