
<!-- @import "[TOC]" {cmd="toc" depthFrom=1 depthTo=6 orderedList=false} -->

<!-- code_chunk_output -->

- [操作系统接口](#操作系统接口)
- [文件通配符](#文件通配符)
- [命令行参数](#命令行参数)
- [错误输出重定向和程序终止](#错误输出重定向和程序终止)
- [字符串模式匹配](#字符串模式匹配)
- [数学](#数学)
- [互联网访问](#互联网访问)
- [日期和时间](#日期和时间)
- [数据压缩](#数据压缩)
- [性能测量](#性能测量)
- [质量控制](#质量控制)
- [自带电池](#自带电池)
- [格式化输出](#格式化输出)
- [模板](#模板)
- [使用二进制数据记录格式](#使用二进制数据记录格式)
- [多线程](#多线程)
- [日志记录](#日志记录)
- [弱引用](#弱引用)
- [用于操作列表的工具](#用于操作列表的工具)
- [十进制浮点运算](#十进制浮点运算)

<!-- /code_chunk_output -->


## 操作系统接口

`os`模块提供了许多与操作系统交互的函数:

```python
>>> import os
>>> os.getcwd()      # Return the current working directory
'C:\\Python38'
>>> os.chdir('/server/accesslogs')   # Change current working directory
>>> os.system('mkdir today')   # Run the command mkdir in the system shell
0

```

一定要使用 `import os` 而不是 `from os import *` 。这将避免内建的 `open()`函数被 `os.open()` 隐式替换掉，它们的使用方式大不相同。

内置的 `dir()` 和 `help()` 函数可用作交互式辅助工具，用于处理大型模块，如 `os`:

```python
>>> import os
>>> dir(os)
<returns a list of all module functions>
>>> help(os)
<returns an extensive manual page created from the module's docstrings>

```

对于日常文件和目录管理任务， `shutil` 模块提供了更易于使用的更高级别的接口:

```python
>>> import shutil
>>> shutil.copyfile('data.db', 'archive.db')
'archive.db'
>>> shutil.move('/build/executables', 'installdir')
'installdir'

```

## 文件通配符

`glob` 模块提供了一个在目录中使用通配符搜索创建文件列表的函数:
```
>>> import glob
>>> glob.glob('*.py')
['primes.py', 'random.py', 'quote.py']
```

## 命令行参数

通用实用程序脚本通常需要处理命令行参数。这些参数作为列表存储在 `sys`模块的 *argv* 属性中。例如，以下输出来自在命令行运行 `python demo.py one two three`

```python
>>> import sys
>>> print(sys.argv)
['demo.py', 'one', 'two', 'three']

```

`argparse` 模块提供了一种更复杂的机制来处理命令行参数。 以下脚本可提取一个或多个文件名，并可选择要显示的行数:

```python
import argparse

parser = argparse.ArgumentParser(prog = 'top',
    description = 'Show top lines from each file')
parser.add_argument('filenames', nargs='+')
parser.add_argument('-l', '--lines', type=int, default=10)
args = parser.parse_args()
print(args)

```

当在通过 `python top.py --lines=5 alpha.txt beta.txt` 在命令行运行时，该脚本会将 `args.lines` 设为 `5` 并将 `args.filenames` 设为 ['alpha.txt', 'beta.txt']`。

## 错误输出重定向和程序终止

`sys` 模块还具有 *stdin* ， *stdout* 和 *stderr* 的属性。后者对于发出警告和错误消息非常有用，即使在 *stdout* 被重定向后也可以看到它们:

```python
>>> sys.stderr.write('Warning, log file not found starting a new one\n')
Warning, log file not found starting a new one

```

终止脚本的最直接方法是使用 `sys.exit() 。

## 字符串模式匹配

`re` 模块为高级字符串处理提供正则表达式工具。对于复杂的匹配和操作，正则表达式提供简洁，优化的解决方案:

```python
>>> import re
>>> re.findall(r'\bf[a-z]*', 'which foot or hand fell fastest')
['foot', 'fell', 'fastest']
>>> re.sub(r'(\b[a-z]+) \1', r'\1', 'cat in the the hat')
'cat in the hat'

```

当只需要简单的功能时，首选字符串方法因为它们更容易阅读和调试:

```python
>>> 'tea for too'.replace('too', 'two')
'tea for two'

```

## 数学

`math` 模块提供对浮点数学的底层C库函数的访问:

```python
>>> import math
>>> math.cos(math.pi / 4)
0.70710678118654757
>>> math.log(1024, 2)
10.0

```

`random` 模块提供了进行随机选择的工具:

```python
>>> import random
>>> random.choice(['apple', 'pear', 'banana'])
'apple'
>>> random.sample(range(100), 10)   # sampling without replacement
[30, 83, 16, 4, 8, 81, 41, 50, 18, 33]
>>> random.random()    # random float
0.17970987693706186
>>> random.randrange(6)    # random integer chosen from range(6)
4

```

`statistics` 模块计算数值数据的基本统计属性（均值，中位数，方差等）:

```python
>>> import statistics
>>> data = [2.75, 1.75, 1.25, 0.25, 0.5, 1.25, 3.5]
>>> statistics.mean(data)
1.6071428571428572
>>> statistics.median(data)
1.25
>>> statistics.variance(data)
1.3720238095238095

```

SciPy项目 <[https://scipy.org](https://scipy.org/)> 有许多其他模块用于数值计算。

## 互联网访问

有许多模块可用于访问互联网和处理互联网协议。其中两个最简单的 `urllib.request` 用于从URL检索数据，以及 `smtplib` 用于发送邮件:

```python
>>> from urllib.request import urlopen
>>> with urlopen('http://tycho.usno.navy.mil/cgi-bin/timer.pl') as response:
...     for line in response:
...         line = line.decode('utf-8')  # Decoding the binary data to text.
...         if 'EST' in line or 'EDT' in line:  # look for Eastern Time
...             print(line)

<BR>Nov. 25, 09:43:32 PM EST

>>> import smtplib
>>> server = smtplib.SMTP('localhost')
>>> server.sendmail('soothsayer@example.org', 'jcaesar@example.org',
... """To: jcaesar@example.org
... From: soothsayer@example.org
...
... Beware the Ides of March.
... """)
>>> server.quit()

```

（请注意，第二个示例需要在localhost上运行的邮件服务器。）

## 日期和时间

`datetime` 模块提供了以简单和复杂的方式操作日期和时间的类。虽然支持日期和时间算法，但实现的重点是有效的成员提取以进行输出格式化和操作。该模块还支持可感知时区的对象。

```python
>>> # dates are easily constructed and formatted
>>> from datetime import date
>>> now = date.today()
>>> now
datetime.date(2003, 12, 2)
>>> now.strftime("%m-%d-%y. %d %b %Y is a %A on the %d day of %B.")
'12-02-03. 02 Dec 2003 is a Tuesday on the 02 day of December.'

>>> # dates support calendar arithmetic
>>> birthday = date(1964, 7, 31)
>>> age = now - birthday
>>> age.days
14368

```

## 数据压缩

```python
>>> import zlib
>>> s = b'witch which has which witches wrist watch'
>>> len(s)
41
>>> t = zlib.compress(s)
>>> len(t)
37
>>> zlib.decompress(t)
b'witch which has which witches wrist watch'
>>> zlib.crc32(s)
226805979

```

## 性能测量

一些Python用户对了解同一问题的不同方法的相对性能产生了浓厚的兴趣。 Python提供了一种可以立即回答这些问题的测量工具。

例如，元组封包和拆包功能相比传统的交换参数可能更具吸引力。`timeit` 模块可以快速演示在运行效率方面一定的优势:

```python
>>> from timeit import Timer
>>> Timer('t=a; a=b; b=t', 'a=1; b=2').timeit()
0.57535828626024577
>>> Timer('a,b = b,a', 'a=1; b=2').timeit()
0.54962537085770791

```

与 `timeit` 的精细粒度级别相反， `profile` 和 `pstats` 模块提供了用于在较大的代码块中识别时间关键部分的工具。

## 质量控制

开发高质量软件的一种方法是在开发过程中为每个函数编写测试，并在开发过程中经常运行这些测试。

`doctest`模块提供了一个工具，用于扫描模块并验证程序文档字符串中嵌入的测试。测试构造就像将典型调用及其结果剪切并粘贴到文档字符串一样简单。这通过向用户提供示例来改进文档，并且它允许doctest模块确保代码保持对文档的真实:

```python
def average(values):
    """Computes the arithmetic mean of a list of numbers.

    >>> print(average([20, 30, 70]))
    40.0
    """
    return sum(values) / len(values)

import doctest
doctest.testmod()   # automatically validate the embedded tests

```

`unittest` 模块不像 `doctest` 模块那样易于使用，但它允许在一个单独的文件中维护更全面的测试集:

```python
import unittest

class TestStatisticalFunctions(unittest.TestCase):

    def test_average(self):
        self.assertEqual(average([20, 30, 70]), 40.0)
        self.assertEqual(round(average([1, 5, 7]), 1), 4.3)
        with self.assertRaises(ZeroDivisionError):
            average([])
        with self.assertRaises(TypeError):
            average(20, 30, 70)

unittest.main()  # Calling from the command line invokes all tests

```

## 自带电池

Python有“自带电池”的理念。通过其包的复杂和强大功能可以最好地看到这一点。例如:

- [xmlrpc.client](https://docs.python.org/zh-cn/3.8/library/xmlrpc.client.html) 和 [xmlrpc.server](https://docs.python.org/zh-cn/3.8/library/xmlrpc.server.html) 模块使得实现远程过程调用变成了小菜一碟。 尽管存在于模块名称中，但用户不需要直接了解或处理 XML。
- [email](https://docs.python.org/zh-cn/3.8/library/email.html) 包是一个用于管理电子邮件的库，包括MIME和其他符合 **[RFC 2822](https://tools.ietf.org/html/rfc2822.html)** 规范的邮件文档。与 [smtplib](https://docs.python.org/zh-cn/3.8/library/smtplib.html) 和 [poplib](https://docs.python.org/zh-cn/3.8/library/poplib.html) 不同（它们实际上做的是发送和接收消息），电子邮件包提供完整的工具集，用于构建或解码复杂的消息结构（包括附件）以及实现互联网编码和标头协议。
- [json](https://docs.python.org/zh-cn/3.8/library/json.html) 包为解析这种流行的数据交换格式提供了强大的支持。 [csv](https://docs.python.org/zh-cn/3.8/library/csv.html) 模块支持以逗号分隔值格式直接读取和写入文件，这种格式通常为数据库和电子表格所支持。 XML 处理由 [xml.etree.ElementTree](https://docs.python.org/zh-cn/3.8/library/xml.etree.elementtree.html) ， [xml.dom](https://docs.python.org/zh-cn/3.8/library/xml.dom.html) 和 [xml.sax](https://docs.python.org/zh-cn/3.8/library/xml.sax.html) 包支持。这些模块和软件包共同大大简化了 Python 应用程序和其他工具之间的数据交换。
- [sqlite3](https://docs.python.org/zh-cn/3.8/library/sqlite3.html) 模块是 SQLite 数据库库的包装器，提供了一个可以使用稍微非标准的 SQL 语法更新和访问的持久数据库。

## 格式化输出

[reprlib](https://docs.python.org/zh-cn/3.8/library/reprlib.html) 模块提供了一个定制化版本的 [repr()](https://docs.python.org/zh-cn/3.8/library/functions.html) 函数，用于缩略显示大型或深层嵌套的容器对象:

```python
>>> import reprlib
>>> reprlib.repr(set('supercalifragilisticexpialidocious'))
"{'a', 'c', 'd', 'e', 'f', 'g', ...}"

```

[pprint](https://docs.python.org/zh-cn/3.8/library/pprint.html) 模块提供了更加复杂的打印控制，其输出的内置对象和用户自定义对象能够被解释器直接读取。当输出结果过长而需要折行时，“美化输出机制”会添加换行符和缩进，以更清楚地展示数据结构:

```python
>>> import pprint
>>> t = [[[['black', 'cyan'], 'white', ['green', 'red']], [['magenta',
...     'yellow'], 'blue']]]
...
>>> pprint.pprint(t, width=30)
[[[['black', 'cyan'],
   'white',
   ['green', 'red']],
  [['magenta', 'yellow'],
   'blue']]]

```

[textwrap](https://docs.python.org/zh-cn/3.8/library/textwrap.html) 模块能够格式化文本段落，以适应给定的屏幕宽度:

```python
>>> import textwrap
>>> doc = """The wrap() method is just like fill() except that it returns
... a list of strings instead of one big string with newlines to separate
... the wrapped lines."""
...
>>> print(textwrap.fill(doc, width=40))
The wrap() method is just like fill()
except that it returns a list of strings
instead of one big string with newlines
to separate the wrapped lines.

```

[locale](https://docs.python.org/zh-cn/3.8/library/locale.html) 模块处理与特定地域文化相关的数据格式。locale 模块的 format 函数包含一个 grouping 属性，可直接将数字格式化为带有组分隔符的样式:

```python
>>> import locale
>>> locale.setlocale(locale.LC_ALL, 'English_United States.1252')
'English_United States.1252'
>>> conv = locale.localeconv()          # get a mapping of conventions
>>> x = 1234567.8
>>> locale.format("%d", x, grouping=True)
'1,234,567'
>>> locale.format_string("%s%.*f", (conv['currency_symbol'],
...                      conv['frac_digits'], x), grouping=True)
'$1,234,567.80'

```

## 模板

[string](https://docs.python.org/zh-cn/3.8/library/string.html) 模块包含一个通用的 [Template](https://docs.python.org/zh-cn/3.8/library/string.html) 类，具有适用于最终用户的简化语法。它允许用户在不更改应用逻辑的情况下定制自己的应用。

上述格式化操作是通过占位符实现的，占位符由 `$` 加上合法的 Python 标识符（只能包含字母、数字和下划线）构成。一旦使用花括号将占位符括起来，就可以在后面直接跟上更多的字母和数字而无需空格分割。`$$` 将被转义成单个字符 `$`:

```python
>>> from string import Template
>>> t = Template('${village}folk send $$10 to $cause.')
>>> t.substitute(village='Nottingham', cause='the ditch fund')
'Nottinghamfolk send $10 to the ditch fund.'

```

如果在字典或关键字参数中未提供某个占位符的值，那么 [substitute()](https://docs.python.org/zh-cn/3.8/library/string.html) 方法将抛出 [KeyError](https://docs.python.org/zh-cn/3.8/library/exceptions.html)。对于邮件合并类型的应用，用户提供的数据有可能是不完整的，此时使用 [safe_substitute()](https://docs.python.org/zh-cn/3.8/library/string.html) 方法更加合适 —— 如果数据缺失，它会直接将占位符原样保留。

```python
>>> t = Template('Return the $item to $owner.')
>>> d = dict(item='unladen swallow')
>>> t.substitute(d)
Traceback (most recent call last):
  ...
KeyError: 'owner'
>>> t.safe_substitute(d)
'Return the unladen swallow to $owner.'

```

Template 的子类可以自定义定界符。例如，以下是某个照片浏览器的批量重命名功能，采用了百分号作为日期、照片序号和照片格式的占位符:

```python
>>> import time, os.path
>>> photofiles = ['img_1074.jpg', 'img_1076.jpg', 'img_1077.jpg']
>>> class BatchRename(Template):
...     delimiter = '%'
>>> fmt = input('Enter rename style (%d-date %n-seqnum %f-format):  ')
Enter rename style (%d-date %n-seqnum %f-format):  Ashley_%n%f

>>> t = BatchRename(fmt)
>>> date = time.strftime('%d%b%y')
>>> for i, filename in enumerate(photofiles):
...     base, ext = os.path.splitext(filename)
...     newname = t.substitute(d=date, n=i, f=ext)
...     print('{0} --> {1}'.format(filename, newname))

img_1074.jpg --> Ashley_0.jpg
img_1076.jpg --> Ashley_1.jpg
img_1077.jpg --> Ashley_2.jpg

```

模板的另一个应用是将程序逻辑与多样的格式化输出细节分离开来。这使得对 XML 文件、纯文本报表和 HTML 网络报表使用自定义模板成为可能。

## 使用二进制数据记录格式

[struct](https://docs.python.org/zh-cn/3.8/library/struct.html) 模块提供了 [pack()](https://docs.python.org/zh-cn/3.8/library/struct.html) 和 [unpack()](https://docs.python.org/zh-cn/3.8/library/struct.html) 函数，用于处理不定长度的二进制记录格式。下面的例子展示了在不使用 [zipfile](https://docs.python.org/zh-cn/3.8/library/zipfile.html) 模块的情况下，如何循环遍历一个 ZIP 文件的所有头信息。Pack 代码 `"H"` 和 `"I"` 分别代表两字节和四字节无符号整数。`"<"` 代表它们是标准尺寸的小尾型字节序:

```python
import struct

with open('myfile.zip', 'rb') as f:
    data = f.read()

start = 0
for i in range(3):                      # show the first 3 file headers
    start += 14
    fields = struct.unpack('<IIIHH', data[start:start+16])
    crc32, comp_size, uncomp_size, filenamesize, extra_size = fields

    start += 16
    filename = data[start:start+filenamesize]
    start += filenamesize
    extra = data[start:start+extra_size]
    print(filename, hex(crc32), comp_size, uncomp_size)

    start += extra_size + comp_size     # skip to the next header

```

## 多线程

线程是一种对于非顺序依赖的多个任务进行解耦的技术。多线程可以提高应用的响应效率，当接收用户输入的同时，保持其他任务在后台运行。一个有关的应用场景是，将 I/O 和计算运行在两个并行的线程中。

以下代码展示了高阶的 [threading](https://docs.python.org/zh-cn/3.8/library/threading.html) 模块如何在后台运行任务，且不影响主程序的继续运行:

```python
import threading, zipfile

class AsyncZip(threading.Thread):
    def __init__(self, infile, outfile):
        threading.Thread.__init__(self)
        self.infile = infile
        self.outfile = outfile

    def run(self):
        f = zipfile.ZipFile(self.outfile, 'w', zipfile.ZIP_DEFLATED)
        f.write(self.infile)
        f.close()
        print('Finished background zip of:', self.infile)

background = AsyncZip('mydata.txt', 'myarchive.zip')
background.start()
print('The main program continues to run in foreground.')

background.join()    # Wait for the background task to finish
print('Main program waited until background was done.')

```

多线程应用面临的主要挑战是，相互协调的多个线程之间需要共享数据或其他资源。为此，threading 模块提供了多个同步操作原语，包括线程锁、事件、条件变量和信号量。

尽管这些工具非常强大，但微小的设计错误却可以导致一些难以复现的问题。因此，实现多任务协作的首选方法是将对资源的所有请求集中到一个线程中，然后使用 [queue](https://docs.python.org/zh-cn/3.8/library/queue.html) 模块向该线程供应来自其他线程的请求。应用程序使用 [Queue](https://docs.python.org/zh-cn/3.8/library/queue.html) 对象进行线程间通信和协调，更易于设计，更易读，更可靠。

## 日志记录

[logging](https://docs.python.org/zh-cn/3.8/library/logging.html) 模块提供功能齐全且灵活的日志记录系统。在最简单的情况下，日志消息被发送到文件或 `sys.stderr`

```python
import logging
logging.debug('Debugging information')
logging.info('Informational message')
logging.warning('Warning:config file %s not found', 'server.conf')
logging.error('Error occurred')
logging.critical('Critical error -- shutting down')

```

这会产生以下输出:

```python
WARNING:root:Warning:config file server.conf not found
ERROR:root:Error occurred
CRITICAL:root:Critical error -- shutting down

```

默认情况下，informational 和 debugging 消息被压制，输出会发送到标准错误流。其他输出选项包括将消息转发到电子邮件，数据报，套接字或 HTTP 服务器。新的过滤器可以根据消息优先级选择不同的路由方式：`DEBUG`，`INFO`，`WARNING`，`ERROR`，和 `CRITICAL`。

日志系统可以直接从 Python 配置，也可以从用户配置文件加载，以便自定义日志记录而无需更改应用程序。

## 弱引用

Python 会自动进行内存管理（对大多数对象进行引用计数并使用 [garbage collection](https://docs.python.org/zh-cn/3.8/glossary.html) 来清除循环引用）。 当某个对象的最后一个引用被移除后不久就会释放其所占用的内存。

此方式对大多数应用来说都适用，但偶尔也必须在对象持续被其他对象所使用时跟踪它们。 不幸的是，跟踪它们将创建一个会令其永久化的引用。 [weakref](https://docs.python.org/zh-cn/3.8/library/weakref.html) 模块提供的工具可以不必创建引用就能跟踪对象。 当对象不再需要时，它将自动从一个弱引用表中被移除，并为弱引用对象触发一个回调。 典型应用包括对创建开销较大的对象进行缓存:

```python
>>> import weakref, gc
>>> class A:
...     def __init__(self, value):
...         self.value = value
...     def __repr__(self):
...         return str(self.value)
...
>>> a = A(10)                   # create a reference
>>> d = weakref.WeakValueDictionary()
>>> d['primary'] = a            # does not create a reference
>>> d['primary']                # fetch the object if it is still alive
10
>>> del a                       # remove the one reference
>>> gc.collect()                # run garbage collection right away
0
>>> d['primary']                # entry was automatically removed
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    d['primary']                # entry was automatically removed
  File "C:/python38/lib/weakref.py", line 46, in __getitem__
    o = self.data[key]()
KeyError: 'primary'

```

## 用于操作列表的工具

许多对于数据结构的需求可以通过内置列表类型来满足。 但是，有时也会需要具有不同效费比的替代实现。

[array](https://docs.python.org/zh-cn/3.8/library/array.html) 模块提供了一种 [array()](https://docs.python.org/zh-cn/3.8/library/array.html) 对象，它类似于列表，但只能存储类型一致的数据且存储密集更高。 下面的例子演示了一个以两个字节为存储单元的无符号二进制数值的数组 (类型码为 `"H"`)，而对于普通列表来说，每个条目存储为标准 Python 的 int 对象通常要占用16 个字节:

```python
>>> from array import array
>>> a = array('H', [4000, 10, 700, 22222])
>>> sum(a)
26932
>>> a[1:3]
array('H', [10, 700])

```

[collections](https://docs.python.org/zh-cn/3.8/library/collections.html) 模块提供了一种 [deque()](https://docs.python.org/zh-cn/3.8/library/collections.html) 对象，它类似于列表，但从左端添加和弹出的速度较快，而在中间查找的速度较慢。 此种对象适用于实现队列和广度优先树搜索:

```python
>>> from collections import deque
>>> d = deque(["task1", "task2", "task3"])
>>> d.append("task4")
>>> print("Handling", d.popleft())
Handling task1

```

```python
unsearched = deque([starting_node])
def breadth_first_search(unsearched):
    node = unsearched.popleft()
    for m in gen_moves(node):
        if is_goal(m):
            return m
        unsearched.append(m)

```

在替代的列表实现以外，标准库也提供了其他工具，例如 [bisect](https://docs.python.org/zh-cn/3.8/library/bisect.html) 模块具有用于操作排序列表的函数:

```python
>>> import bisect
>>> scores = [(100, 'perl'), (200, 'tcl'), (400, 'lua'), (500, 'python')]
>>> bisect.insort(scores, (300, 'ruby'))
>>> scores
[(100, 'perl'), (200, 'tcl'), (300, 'ruby'), (400, 'lua'), (500, 'python')]

```

[heapq](https://docs.python.org/zh-cn/3.8/library/heapq.html) 模块提供了基于常规列表来实现堆的函数。 最小值的条目总是保持在位置零。 这对于需要重复访问最小元素而不希望运行完整列表排序的应用来说非常有用:

```python
>>> from heapq import heapify, heappop, heappush
>>> data = [1, 3, 5, 7, 9, 2, 4, 6, 8, 0]
>>> heapify(data)                      # rearrange the list into heap order
>>> heappush(data, -5)                 # add a new entry
>>> [heappop(data) for i in range(3)]  # fetch the three smallest entries
[-5, 0, 1]

```

## 十进制浮点运算

[decimal](https://docs.python.org/zh-cn/3.8/library/decimal.html) 模块提供了一种 [Decimal](https://docs.python.org/zh-cn/3.8/library/decimal.html) 数据类型用于十进制浮点运算。 相比内置的 [float](https://docs.python.org/zh-cn/3.8/library/functions.html) 二进制浮点实现，该类特别适用于

- 财务应用和其他需要精确十进制表示的用途，
- 控制精度，
- 控制四舍五入以满足法律或监管要求，
- 跟踪有效小数位，或
- 用户期望结果与手工完成的计算相匹配的应用程序。

例如，使用十进制浮点和二进制浮点数计算70美分手机和5％税的总费用，会产生的不同结果。如果结果四舍五入到最接近的分数差异会更大:

```python
>>> from decimal import *
>>> round(Decimal('0.70') * Decimal('1.05'), 2)
Decimal('0.74')
>>> round(.70 * 1.05, 2)
0.73

```

[Decimal](https://docs.python.org/zh-cn/3.8/library/decimal.html) 表示的结果会保留尾部的零，并根据具有两个有效位的被乘数自动推出四个有效位。 Decimal 可以模拟手工运算来避免当二进制浮点数无法精确表示十进制数时会导致的问题。

精确表示特性使得 [Decimal](https://docs.python.org/zh-cn/3.8/library/decimal.html) 类能够执行对于二进制浮点数来说不适用的模运算和相等性检测:

```python
>>> Decimal('1.00') % Decimal('.10')
Decimal('0.00')
>>> 1.00 % 0.10
0.09999999999999995

>>> sum([Decimal('0.1')]*10) == Decimal('1.0')
True
>>> sum([0.1]*10) == 1.0
False

```

[decimal](https://docs.python.org/zh-cn/3.8/library/decimal.html) 模块提供了运算所需要的足够精度:

```python
>>> getcontext().prec = 36
>>> Decimal(1) / Decimal(7)
Decimal('0.142857142857142857142857142857142857')

```