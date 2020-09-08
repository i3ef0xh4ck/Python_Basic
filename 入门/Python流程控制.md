
<!-- @import "[TOC]" {cmd="toc" depthFrom=1 depthTo=6 orderedList=false} -->

<!-- code_chunk_output -->

- [if elif else](#if-elif-else)
- [for 循环](#for-循环)
- [while 循环](#while-循环)
- [break](#break)
- [continue](#continue)
- [pass语句](#pass语句)
- [循环的技巧](#循环的技巧)
- [深入条件控制](#深入条件控制)
- [比较序列和其他类型](#比较序列和其他类型)

<!-- /code_chunk_output -->

### if elif else

```python
x = int(input("Please enter an integer: "))
if x < 0:
		print("Negative")
elif x == 0:
		print("zero")
else:
		print("positive")
```

### for 循环

```python
array = [1, 2, 3, 4, 5]
for a in array:
		print(a)
```

### while 循环

```python
a = 10
while a > 0:
		print(a)
		a -= 1
```

### break

break语句：用于跳出最近的for或while循环

```python
for n in range(10):
		if n > 6:
				print(n)
				break
```

循环语句可能带有else子句，它会在循环耗尽了可迭代对象或循环条件变为False时被执行，但不会在循环被break语句终止时执行，以下搜索素数的循环就是这样的一个例子：

```python
for n in range(2, 10):
		for x in range(2, n):
				if n % x == 0:
						print(n, 'equals', x, '*', n / x)
						break
		else:
				print(n, "is a prime number ")
```

### continue

continue语句借鉴自c语言，表示跳过continue之后的语句，直接进入到循环的下一个迭代

```python
for i in range(2, 10):
		if i % 2 == 0:
				print("Found an even numeber", i)
				continue
		print("Found a number", i)
```

```python
Found an even number 2
Found a number 3
Found an even number 4
Found a number 5
Found an even number 6
Found a number 7
Found an even number 8
Found a number 9
```

### pass语句

pass 语句什么也不做。当语法上需要一个语句，但程序需要什么动作也不做时，可以使用它

pass 的另一个可以使用的场合是在你编写新的代码时作为一个函数或条件子句体的占位符，允许你保持在更抽象的层次上进行思考

```python
def initlog(*args):
		pass  # 暂时不做，记得实现它
```

### 循环的技巧

当在字典中循环时，用 `items()` 方法可将关键字和对应的值同时取出

```python
>>> knights = {'gallahad': 'the pure', 'robin': 'the brave'}
>>> for k, v in knights.items():
...  print(k, v)
...gallahad the pure
robin the brave
```

当在序列中循环时，用 `enumerate()` 函数可以将索引位置和其对应的值同时取出

```python
>>> for i, v in enumerate(['tic', 'tac', 'toe']):
...  print(i, v)
...0 tic
1 tac
2 toe
```

当同时在两个或更多序列中循环时，可以用 `zip()` 函数将其内元素一一匹配。

```python
>>> questions = ['name', 'quest', 'favorite color']
>>> answers = ['lancelot', 'the holy grail', 'blue']
>>> for q, a in zip(questions, answers):
...  print('What is your *{0}*? It is *{1}*.'.format(q, a))
...What is your name? It is lancelot.
What is your quest? It is the holy grail.
What is your favorite color? It is blue.
```

如果要逆向循环一个序列，可以先正向定位序列，然后调用 `reversed()` 函数

```python
>>> for i in reversed(range(1, 10, 2)):
...  print(i)
...9
7
5
3
1
```

如果要按某个指定顺序循环一个序列，可以用 `sorted()` 函数，它可以在不改动原序列的基础上返回一个新的排好序的序列

```python
>>> basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
>>> for f in sorted(set(basket)):
...  print(f)
...apple
banana
orange
pear
```

有时可能会想在循环时修改列表内容，一般来说改为创建一个新列表是比较简单且安全的

```python
>>> import math>>> raw_data = [56.2, float('NaN'), 51.7, 55.3, 52.5, float('NaN'), 47.8]
>>> filtered_data = []
>>> for value in raw_data:
...  if not math.isnan(value):
...  filtered_data.append(value)
...>>> filtered_data
[56.2, 51.7, 55.3, 52.5, 47.8]
```

### 深入条件控制

`while` 和 `if` 条件句中可以使用任意操作，而不仅仅是比较操作。

比较操作符 `in` 和 `not in` 校验一个值是否在（或不在）一个序列里。操作符 `is` 和 `is not` 比较两个对象是不是同一个对象，这只对像列表这样的可变对象比较重要。所有的比较操作符都有相同的优先级，且这个优先级比数值运算符低。

比较操作可以传递。例如 `a < b == c` 会校验是否 `a` 小于 `b` 并且 `b` 等于 `c`。

比较操作可以通过布尔运算符 `and` 和 `or` 来组合，并且比较操作（或其他任何布尔运算）的结果都可以用 `not` 来取反。这些操作符的优先级低于比较操作符；在它们之中，`not` 优先级最高， `or` 优先级最低，因此 `A and not B or C` 等价于 `(A and (not B)) or C`。和之前一样，你也可以在这种式子里使用圆括号。

布尔运算符 `and` 和 `or` 也被称为 *短路* 运算符：它们的参数从左至右解析，一旦可以确定结果解析就会停止。例如，如果 `A` 和 `C` 为真而 `B` 为假，那么 `A and B and C` 不会解析 `C`。当用作普通值而非布尔值时，短路操作符的返回值通常是最后一个变量。

也可以把比较操作或者逻辑表达式的结果赋值给一个变量，例如

```python
>>> string1, string2, string3 = '', 'Trondheim', 'Hammer Dance'
>>> non_null = string1 or string2 or string3
>>> non_null
'Trondheim'
```

### 比较序列和其他类型

序列对象通常可以与相同序列类型的其他对象比较。 这种比较使用 *字典式* 顺序：首先比较开头的两个对应元素，如果两者不相等则比较结果就由此确定；如果两者相等则比较之后的两个元素，以此类推，直到有一个序列被耗尽。 如果要比较的两个元素本身又是相同类型的序列，则会递归地执行字典式顺序比较。 如果两个序列中所有的对应元素都相等，则两个序列也将被视为相等。 如果一个序列是另一个的初始子序列，则较短的序列就被视为较小（较少）。 对于字符串来说，字典式顺序是使用 Unicode 码位序号对单个字符排序。 下面是一些相同类型序列之间比较的例子:

```python
(1, 2, 3) < (1, 2, 4)
[1, 2, 3] < [1, 2, 4]
'ABC' < 'C' < 'Pascal' < 'Python'
(1, 2, 3, 4) < (1, 2, 4)
(1, 2) < (1, 2, -1)
(1, 2, 3) == (1.0, 2.0, 3.0)
(1, 2, ('aa', 'ab')) < (1, 2, ('abc', 'a'), 4)
```

注意对不同类型对象来说，只要待比较对象提供了合适的比较方法，就可以使用 `<` 和 `>` 来比较。例如，混合数值类型是通过他们的数值进行比较的，所以 0 等于 0.0，等等。否则，解释器将抛出一个 `TypeError` 异常，而不是随便给出一个结果。