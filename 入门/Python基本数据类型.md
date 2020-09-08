

<!-- @import "[TOC]" {cmd="toc" depthFrom=1 depthTo=6 orderedList=false} -->

<!-- code_chunk_output -->

- [列表](#列表)
  - [列表对象方法清单](#列表对象方法清单)
  - [列表作为栈使用](#列表作为栈使用)
  - [列表作为队列使用](#列表作为队列使用)
  - [列表推导式](#列表推导式)
  - [del 语句](#del-语句)
- [元组](#元组)
  - [元组对象方法清单](#元组对象方法清单)
- [集合](#集合)
  - [集合对象方法清单](#集合对象方法清单)
  - [集合推导式](#集合推导式)
- [字典](#字典)
  - [字典对象方法清单](#字典对象方法清单)

<!-- /code_chunk_output -->

## 列表

### 列表对象方法清单

- `list.append(x)`

    在列表的末尾添加一个元素，相当于a[len(a):]=[x]

- `list.extend(iterable)`

    使用可迭代对象中的所有元素来扩展列表，相当于a[len(a):] = iterable

- `list.insert(i, x)`

    在给定的位置插入一个元素，第一个参数是要插入的元素的索引，所以a.insert(0, x) 插入列表头部， a.insert(len(a), x) 等同于 a.append(x)

- `list.remove(x)`

    移除列表中第一个值为x的元素，如果没有这样的元素，抛出ValueError异常

- `list.pop([i])`

    删除列表中给定位置i的元素并返回它，如果没有给定i，则会删除并返回最后一个元素

    方法签名中 i 两边的方括号表示这个参数是可选的，而不是要你输入方括号。你会在 Python 参考库中经常看到这种表示方法

- `list.clear()`

    移除列表中的所有元素，等价于del a[:]

- `list.index(x, [start[, end]])`

    返回列表中第一个值为x的元素的从零开始的索引，如果没有这样的元素则抛出ValueError异常

    可选参数start和end是切片符号，用于将搜索限制为列表的特定子序列，返回的索引是相对于整个序列开始计算的，而不是start参数

- `list.count(x)`

    返回元素x在列表中出现的次数

- `list.sort(key=None, reverse=False)`

    对列表中的元素进行排序；

    key 指定带有单个参数的函数，用于从 iterable 的每个元素中提取用于比较的键 (例如 key=str.lower)。 默认值为 None (直接比较元素)；

    reverse 为一个布尔值。 如果设为 True，则每个列表元素将按反向顺序比较进行排序。

- `list.reverse()`

    翻转列表中的元素

- `list.copy()`

    返回列表的一个浅拷贝，等价于a[:]

    你可能已经注意到，像 insert ，remove 或者 sort 方法，只修改列表，没有打印出返回值——它们返回默认值 None 。这是Python中所有可变数据结构的设计原则。

    你可能会注意到的另一件事是并非所有数据或可以排序或比较。 例如，[None, 'hello', 10] 就不可排序，因为整数不能与字符串比较，而 None 不能与其他类型比较。 并且还存在一些没有定义顺序关系的类型。 例如，3+4j < 5+7j 就不是一个合法的比较。

### 列表作为栈使用

列表方法使得列表作为堆栈非常容易，最后一个插入，最先取出（后进先出）。要添加一个元素到堆栈的顶端，使用append()。要从堆栈顶部取出一个元素，使用pop()，不用指定索引，如：

```python
>>> stack = [3, 4, 5]
>>> stack.append(6)
>>> stack.append(7)
>>> stack
[3, 4, 5, 6, 7]
>>> stack.pop()
7
>>> stack
[3, 4, 5, 6]
>>> stack.pop()
6
>>> stack.pop()
5
>>> stack
[3, 4]
```

### 列表作为队列使用

列表也可以用作队列，其中先添加的元素被最先取出 (“先进先出”)；然而列表用作这个目的相当低效。因为在列表的末尾添加和弹出元素非常快，但是在列表的开头插入或弹出元素却很慢 (因为所有的其他元素都必须移动一位)。

若要实现一个队列，可使用 [collections.deque](https://docs.python.org/zh-cn/3.8/library/collections.html#collections.deque)，它被设计成可以快速地从两端添加或弹出元素。例如：

```python
>>> from collections import deque
>>> queue = deque(["Eric", "John", "Michael"])
>>> queue.append("Terry")           # Terry arrives
>>> queue.append("Graham")          # Graham arrives
>>> queue.popleft()                 # The first to arrive now leaves
'Eric'
>>> queue.popleft()                 # The second to arrive now leaves
'John'
>>> queue                           # Remaining queue in order of arrival
deque(['Michael', 'Terry', 'Graham'])
```

### 列表推导式

列表推导式提供了一个更简单的创建列表的方法。常见的用法是把某种操作应用于序列或可迭代对象的每个元素上，然后使用其结果来创建列表，或者通过满足某些特定条件元素来创建子序列。

例如，假设我们想创建一个平方列表，像这样

```python
>>> squares = []
>>> for x in range(10):
...     squares.append(x**2)
...
>>> squares
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
```

注意这里创建（或被重写）的名为 `x` 的变量在for循环后仍然存在。我们可以计算平方列表的值而不会产生任何副作用

```python
squares = list(map(**lambda** x: x**2, range(10)))
```

或者，等价于

```python
squares = [x**2 **for** x **in** range(10)]
```

上面这种写法更加简洁易读。

列表推导式的结构是由一对方括号所包含的以下内容：一个表达式，后面跟一个 `for` 子句，然后是零个或多个 `for` 或 `if` 子句。 其结果将是一个新列表，由对表达式依据后面的 `for` 和 `if` 子句的内容进行求值计算而得出。 举例来说，以下列表推导式会将两个列表中不相等的元素组合起来:

```python
>>> [(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]
[(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]
```

而它等价于

```python
>>> combs = []
>>> for x in [1,2,3]:
...  for y in [3,1,4]:
...  if x != y:
...  combs.append((x, y))
...
>>> combs
[(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]
```

### del 语句

有一种方式可以从列表按照给定的索引而不是值来移除一个元素: 那就是 del 语句。 它不同于会返回一个值的 pop() 方法。 del 语句也可以用来从列表中移除切片或者清空整个列表（我们之前用过的方式是将一个空列表赋值给指定的切片）。 例如:

```python
>>> a = [-1, 1, 66.25, 333, 333, 1234.5]
>>> del a[0]
>>> a
[1, 66.25, 333, 333, 1234.5]
>>> del a[2:4]
>>> a
[1, 66.25, 1234.5]
>>> del a[:]
>>> a
[]
```

del 也可以删除整个变量

```python
del a
```

此后再引用 a 时会报错（直到另一个值被赋给它）

## 元组

元组是不可变的序列。

元组在输出时总是被圆括号包围的，以便正确表示嵌套元组。输入时圆括号可有可无，不过经常会是必须的（如果这个元组是一个更大的表达式的一部分）。给元组中的一个单独的元素赋值是不允许的，当然你可以创建包含可变对象的元组，例如列表。

虽然元组可能看起来与列表很像，但它们通常是在不同的场景被使用，并且有着不同的用途。元组是 `immutable`，其序列通常包含不同种类的元素，并且通过解包（这一节下面会解释）或者索引来访问（如果是 `namedtuples` 的话甚至还可以通过属性访问）。列表是 `mutable`，并且列表中的元素一般是同种类型的，并且通过迭代访问。

一个特殊的问题是构造包含0个或1个元素的元组：为了适应这种情况，语法有一些额外的改变。空元组可以直接被一对空圆括号创建，含有一个元素的元组可以通过在这个元素后添加一个逗号来构建（圆括号里只有一个值的话不够明确）。丑陋，但是有效。例如

```python
>>> empty = ()
>>> singleton = 'hello',    # <-- 注意末尾有逗号
>>> len(empty)
0
>>> len(singleton)
1
>>> singleton
('hello',)
```

语句 `t = 12345, 54321, 'hello!'` 是 *元组打包* 的一个例子：值 `12345`, `54321` 和 `'hello!'` 被打包进元组。其逆操作也是允许的:  **`x, y, z = t`

这被称为 *序列解包* 也是很恰当的，因为解包操作的等号右侧可以是任何序列。序列解包要求等号左侧的变量数与右侧序列里所含的元素数相同。注意多重赋值其实也只是元组打包和序列解包的组合。

### 元组对象方法清单

- `tuple.index(x, [start[, end]])`

    返回元组中第一个值为x的元素的从零开始的索引，如果没有这样的元素则抛出ValueError异常

    可选参数start和end是切片符号，用于将搜索限制为列表的特定子序列，返回的索引是相对于整个序列开始计算的，而不是start参数

- `tuple.count(x)`

    返回元素x在元组中出现的次数

## 集合

集合是由不重复元素组成的无序的集。它的基本用法包括成员检测和消除重复元素。集合对象也支持像 联合，交集，差集，对称差分等数学运算。

花括号或 `set()` 函数可以用来创建集合。注意：要创建一个空集合你只能用 `set()` 而不能用 `{}`，因为后者是创建一个空字典

### 集合对象方法清单

- `set.add(x)`

    将x添加到集合，若添加之前x就属于集合，则没有影响

- `set.pop()`

    随机删除并返回集合的某个元素

- `set.clear()`

    清空集合

- `set.copy()`

    返回集合的浅拷贝

- `set1.difference(set2)`

    返回一个属于set1但不属于set2的所有元素的新集合

- `set1.difference_update(set2)`

    将set1替换为`set1.difference(set2)`

- `set.discard(x)`

    删除集合中的x，若集合不包含x，则没有影响

- `set1.intersection(set2)`

    set1和set2的交集

- `set1.intersection_update(set2)`

    将set1替换为`set1.intersection(set2)`

- `set1.isdisjoint(set2)`

    若set1和set2无交集则返回 `True`否则返回 `False`

- `set1.issubset(set2)`

    判断set1是否为set2的子集

- `set1.issuperset(set2)`

    判断set1是否为set2的超集

- `set.remove(x)`

    移除集合的一个元素，若x不属于集合，包KeyError

### 集合推导式

```python
>>> a = {x for x in 'abracadabra' if x not in 'abc'}
>>> a
{'r', 'd'}
```

## 字典

字典在其他语言里可能会被叫做 *联合内存* 或 *联合数组*。与以连续整数为索引的序列不同，字典是以 *关键字* 为索引的，关键字可以是任意不可变类型，通常是字符串或数字。如果一个元组只包含字符串、数字或元组，那么这个元组也可以用作关键字。但如果元组直接或间接地包含了可变对象，那么它就不能用作关键字。列表不能用作关键字，因为列表可以通过索引、切片或 `append()` 和 `extend()` 之类的方法来改变。

理解字典的最好方式，就是将它看做是一个 *键: 值* 对的集合，键必须是唯一的（在一个字典中）。一对花括号可以创建一个空字典：`{}` 。另一种初始化字典的方式是在一对花括号里放置一些以逗号分隔的键值对，而这也是字典输出的方式。

字典主要的操作是使用关键字存储和解析值。也可以用 `del` 来删除一个键值对。如果你使用了一个已经存在的关键字来存储值，那么之前与这个关键字关联的值就会被遗忘。用一个不存在的键来取值则会报错。

对一个字典执行 `list(d)` 将返回包含该字典中所有键的列表，按插入次序排列 (如需其他排序，则要使用 `sorted(d)`)。要检查字典中是否存在一个特定键，可使用 `in` 关键字

以下是使用字典的一些简单示例

```python
>>> tel = {'jack': 4098, 'sape': 4139}
>>> tel['guido'] = 4127
>>> tel
{'jack': 4098, 'sape': 4139, 'guido': 4127}
>>> tel['jack']
4098
>>> del tel['sape']
>>> tel['irv'] = 4127
>>> tel
{'jack': 4098, 'guido': 4127, 'irv': 4127}
>>> list(tel)
['jack', 'guido', 'irv']
>>> sorted(tel)
['guido', 'irv', 'jack']
>>> 'guido' in tel
True
>>> 'jack' not in tel
False
```

`dict()` 构造函数可以直接从键值对序列里创建字典。

```python
>>> dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])
{'sape': 4139, 'guido': 4127, 'jack': 4098}
```

此外，字典推导式可以从任意的键值表达式中创建字典

```python
>>> {x: x**2 for x in (2, 4, 6)}
{2: 4, 4: 16, 6: 36}
```

当关键字是简单字符串时，有时直接通过关键字参数来指定键值对更方便

```python
>>> dict(sape=4139, guido=4127, jack=4098)
{'sape': 4139, 'guido': 4127, 'jack': 4098}
```

### 字典对象方法清单

- `dict.get(x, default=None)`

    返回字典中key为x的值，没有则返回default

- `dict.pop(x[, d])`

    删除指定的键并返回相应的值。
    如果没有找到key，则返回d，否则会引发KeyError

- `dict.clear()`

    清空字典

- `dict.copy()`

    字典浅拷贝

- `dict.fromkeys(iterable, value=None)`

    创建一个新的字典，其中的键来自iterable，值设置为value。

- `dict.items()`

    返回 `dict_items([(key1, value1), (key2, value2), ...])`

- `dict.keys()`

    返回 `dict_keys([key1, key2, ...])`

- `dict.values()`

    返回 `dict_values([value1, value2, ...])`

- `dict.popitem()`

    删除并返回一个(键，值)对作为一个二元组。
    按照后进先出的顺序返回。
    如果dict为空，引发键错误。

- `dict.setdefault(key, default=None)`

    如果key不在dict中，插入key和value, value为default

    如果key在dict中，返回对应的vlaue，否则返回default

- `dict.update([x])`

    若没有参数，没有影响

    若x有.keys()方法，则将x中的所有键值对添加到dict

    若x没有.keys()方法，则x必须是可迭代对象（且x的长度必须为2，否则引发ValueError）然后执行如下操作：

    ```python
    for key, value in x:
            dict[key] = value
    ```