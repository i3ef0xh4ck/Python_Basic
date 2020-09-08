[https://docs.python.org/zh-cn/3.8/library/exceptions.html](https://docs.python.org/zh-cn/3.8/library/exceptions.html)

在 Python 中，所有异常必须为一个派生自 `[BaseException](https://docs.python.org/zh-cn/3.8/library/exceptions.html)` 的类的实例。 在带有提及一个特定类的 `[except](https://docs.python.org/zh-cn/3.8/reference/compound_stmts.html)` 子句的 `[try](https://docs.python.org/zh-cn/3.8/reference/compound_stmts.html)` 语句中，该子句也会处理任何派生自该类的异常类（但不处理 *它* 所派生出的异常类）。 通过子类化创建的两个不相关异常类永远是不等效的，既使它们具有相同的名称。

下面列出的内置异常可通过解释器或内置函数来生成。除非另有说明，它们都会具有一个提示导致错误详细原因的“关联值”。 这可以是一个字符串或由多个信息项（例如一个错误码和一个解释错误的字符串）组成的元组。 关联值通常会作为参数被传递给异常类的构造器。

用户代码可以引发内置异常。 这可被用于测试异常处理程序或报告错误条件，“就像” 在解释器引发了相同异常的情况时一样；但是请注意，没有任何机制能防止用户代码引发不适当的错误。

内置异常类可以被子类化以定义新的异常；鼓励程序员从 `[Exception](https://docs.python.org/zh-cn/3.8/library/exceptions.html)` 类或它的某个子类而不是从 `[BaseException](https://docs.python.org/zh-cn/3.8/library/exceptions.html)` 来派生新的异常。 关于定义异常的更多信息可以在 Python 教程的 [用户自定义异常](https://docs.python.org/zh-cn/3.8/tutorial/errors.html) 部分查看。

当在 `[except](https://docs.python.org/zh-cn/3.8/reference/compound_stmts.html)` 或 `[finally](https://docs.python.org/zh-cn/3.8/reference/compound_stmts.html)` 子句中引发（或重新引发）异常时，`__context__` 会被自动设为所捕获的最后一个异常；如果新的异常未被处理，则最终显示的回溯信息将包括原始的异常和最后的异常。

当引发一个新的异常（而不是简单地使用 `raise` 来重新引发当前在处理的异常）时，隐式的异常上下文可以通过使用带有 `[raise](https://docs.python.org/zh-cn/3.8/reference/simple_stmts.html)` 的 `[from](https://docs.python.org/zh-cn/3.8/reference/simple_stmts.html)` 来补充一个显式的原因:

```
raise new_exc from original_exc

```

跟在 `[from](https://docs.python.org/zh-cn/3.8/reference/simple_stmts.html)` 之后的表达式必须为一个异常或 `None`。 它将在所引发的异常上被设置为 `__cause__`。 设置 `__cause__` 还会隐式地将 `__suppress_context__` 属性设为 `True`，这样使用 `raise new_exc from None` 可以有效地将旧异常替换为新异常来显示其目的 (例如将 `[KeyError](https://docs.python.org/zh-cn/3.8/library/exceptions.html)` 转换为 `[AttributeError](https://docs.python.org/zh-cn/3.8/library/exceptions.html)`)，同时让旧异常在 `__context__` 中保持可用状态以便在调试时进行内省。

除了异常本身的回溯以外，默认的回溯还会显示这些串连的异常。 `__cause__` 中的显式串连异常如果存在将总是显示。 `__context__` 中的隐式串连异常仅在 `__cause__` 为 `[None](https://docs.python.org/zh-cn/3.8/library/constants.html)` 并且 `__suppress_context__` 为假值时显示。

不论在哪种情况下，异常本身总会在任何串连异常之后显示，以便回溯的最后一行总是显示所引发的最后一个异常。

## 基类

下列异常主要被用作其他异常的基类。

 *exception* `BaseException` 所有内置异常的基类。 它不应该被用户自定义类直接继承 (这种情况请使用 `[Exception](https://docs.python.org/zh-cn/3.8/library/exceptions.html)`)。 如果在此类的实例上调用 `[str()](https://docs.python.org/zh-cn/3.8/library/stdtypes.html)`，则会返回实例的参数表示，或者当没有参数时返回空字符串。   `args` 传给异常构造器的参数元组。 某些内置异常 (例如 `[OSError](https://docs.python.org/zh-cn/3.8/library/exceptions.html)`) 接受特定数量的参数并赋予此元组中的元素特殊的含义，而其他异常通常只接受一个给出错误信息的单独字符串。    `with_traceback`(*tb*) 此方法将 *tb* 设为异常的新回溯信息并返回该异常对象。 它通常以如下的形式在异常处理程序中使用: try: ...
except SomeException: tb = sys.exc_info()[2] raise OtherException(...).with_traceback(tb)
  

 *exception* `Exception` 所有内置的非系统退出类异常都派生自此类。 所有用户自定义异常也应当派生自此类。 

## 具体异常

以下异常属于经常被引发的异常。

 *exception* `FloatingPointError` 目前未被使用。 

 *exception* `KeyError` 当在现有键集合中找不到指定的映射（字典）键时将被引发。 

 *exception* `KeyboardInterrupt` 当用户按下中断键 (通常为 Control-C 或 Delete) 时将被引发。 在执行期间，会定期检测中断信号。 该异常继承自 `[BaseException](https://docs.python.org/zh-cn/3.8/library/exceptions.html)` 以确保不会被处理 `[Exception](https://docs.python.org/zh-cn/3.8/library/exceptions.html)` 的代码意外捕获，这样可以避免退出解释器。 

 *exception* `MemoryError` 当一个操作耗尽内存但情况仍可（通过删除一些对象）进行挽救时将被引发。 关联的值是一个字符串，指明是哪种（内部）操作耗尽了内存。 请注意由于底层的内存管理架构（C 的 `malloc()` 函数），解释器也许并不总是能够从这种情况下完全恢复；但它毕竟可以引发一个异常，这样就能打印出栈回溯信息，以便找出导致问题的失控程序。 

 *exception* `NameError` 当某个局部或全局名称未找到时将被引发。 此异常仅用于非限定名称。 关联的值是一条错误信息，其中包含未找到的名称。 

 *exception* `OSError`([*arg*])  *exception* `OSError`(*errno*, *strerror*[, *filename*[, *winerror*[, *filename2*]]]) 此异常在一个系统函数返回系统相关的错误时将被引发，此类错误包括 I/O 操作失败例如 "文件未找到" 或 "磁盘已满" 等（不包括非法参数类型或其他偶然性错误）。 构造器的第二种形式可设置如下所述的相应属性。 如果未指定这些属性则默认为 `[None](https://docs.python.org/zh-cn/3.8/library/constants.html)`。 为了能向下兼容，如果传入了三个参数，则 `[args](https://docs.python.org/zh-cn/3.8/library/exceptions.html)` 属性将仅包含由前两个构造器参数组成的 2 元组。 构造器实际返回的往往是 `[OSError](https://docs.python.org/zh-cn/3.8/library/exceptions.html)` 的某个子类，如下文 [OS exceptions](https://docs.python.org/zh-cn/3.8/library/exceptions.html) 中所描述的。 具体的子类取决于最终的 `[errno](https://docs.python.org/zh-cn/3.8/library/exceptions.html)` 值。 此行为仅在直接或通过别名来构造 `[OSError](https://docs.python.org/zh-cn/3.8/library/exceptions.html)` 时发生，并且在子类化时不会被继承。   `strerror` 操作系统所提供的相应错误信息。 它在 POSIX 平台中由 C 函数 `perror()` 来格式化，在 Windows 中则是由 `FormatMessage()`。  

 *exception* `OverflowError` 当算术运算的结果大到无法表示时将被引发。 这对整数来说不可能发生（宁可引发 `[MemoryError](https://docs.python.org/zh-cn/3.8/library/exceptions.html)` 也不会放弃尝试）。 但是出于历史原因，有时也会在整数超出要求范围的情况下引发 OverflowError。 因为在 C 中缺少对浮点异常处理的标准化，大多数浮点运算都不会做检查。 

 *exception* `ReferenceError` 此异常将在使用 `[weakref.proxy()](https://docs.python.org/zh-cn/3.8/library/weakref.html)` 函数所创建的弱引用来访问该引用的某个已被作为垃圾回收的属性时被引发。 有关弱引用的更多信息请参阅 `[weakref](https://docs.python.org/zh-cn/3.8/library/weakref.html)` 模块。 

 *exception* `RuntimeError` 当检测到一个不归属于任何其他类别的错误时将被引发。 关联的值是一个指明究竟发生了什么问题的字符串。 

 *exception* `StopIteration`  该异常对象只有一个属性 `value`，它在构造该异常时作为参数给出，默认值为 `[None](https://docs.python.org/zh-cn/3.8/library/constants.html)`。 在 3.3 版更改: 添加了 `value` 属性及其被生成器函数用作返回值的功能。 

 *exception* `SystemError` 当解释器发现内部错误，但情况看起来尚未严重到要放弃所有希望时将被引发。 关联的值是一个指明发生了什么问题的字符串（表示为低层级的符号）。 你应当将此问题报告给你所用 Python 解释器的作者或维护人员。 请确认报告 Python 解释器的版本号 (`sys.version`; 它也会在交互式 Python 会话开始时被打印出来)，具体的错误消息（异常所关联的值）以及可能触发该错误的程序源码。 

 *exception* `SystemExit` 此异常由 `[sys.exit()](https://docs.python.org/zh-cn/3.8/library/sys.html)` 函数引发。 它继承自 `[BaseException](https://docs.python.org/zh-cn/3.8/library/exceptions.html)` 而不是 `[Exception](https://docs.python.org/zh-cn/3.8/library/exceptions.html)` 以确保不会被处理 `[Exception](https://docs.python.org/zh-cn/3.8/library/exceptions.html)` 的代码意外捕获。 这允许此异常正确地向上传播并导致解释器退出。 如果它未被处理，则 Python 解释器就将退出；不会打印任何栈回溯信息。 构造器接受的可选参数与传递给 `[sys.exit()](https://docs.python.org/zh-cn/3.8/library/sys.html)` 的相同。 如果该值为一个整数，则它指明系统退出状态码（会传递给 C 的 `exit()` 函数）；如果该值为 `None`，则退出状态码为零；如果该值为其他类型（例如字符串），则会打印对象的值并将退出状态码设为一。 对 `[sys.exit()](https://docs.python.org/zh-cn/3.8/library/sys.html)` 的调用会被转换为一个异常以便能执行清理处理程序 (`[try](https://docs.python.org/zh-cn/3.8/reference/compound_stmts.html)` 语句的 `[finally](https://docs.python.org/zh-cn/3.8/reference/compound_stmts.html)` 子句)，并且使得调试器可以执行一段脚本而不必冒失去控制的风险。 如果绝对确实地需要立即退出（例如在调用 `[os.fork()](https://docs.python.org/zh-cn/3.8/library/os.html)` 之后的子进程中）则可使用 `[os._exit()](https://docs.python.org/zh-cn/3.8/library/os.html)`.   `code` 传给构造器的退出状态码或错误信息（默认为 `None`。）  

 *exception* `UnicodeError` 当发生与 Unicode 相关的编码或解码错误时将被引发。 此异常是 `[ValueError](https://docs.python.org/zh-cn/3.8/library/exceptions.html)` 的一个子类。 `[UnicodeError](https://docs.python.org/zh-cn/3.8/library/exceptions.html)` 具有一些描述编码或解码错误的属性。 例如 `err.object[err.start:err.end]` 会给出导致编解码器失败的特定无效输入。   `encoding` 引发错误的编码名称。    `reason` 描述特定编解码器错误的字符串。    `object` 编解码器试图要编码或解码的对象。  

 *exception* `ValueError` 当操作或函数接收到具有正确类型但值不适合的参数，并且情况不能用更精确的异常例如 `[IndexError](https://docs.python.org/zh-cn/3.8/library/exceptions.html)` 来描述时将被引发。 

 *exception* `ZeroDivisionError` 当除法或取余运算的第二个参数为零时将被引发。 关联的值是一个字符串，指明操作数和运算的类型。 

下列异常被保留以与之前的版本相兼容；从 Python 3.3 开始，它们都是 `[OSError](https://docs.python.org/zh-cn/3.8/library/exceptions.html)` 的别名。

 *exception* `EnvironmentError` 

 *exception* `IOError` 

 *exception* `WindowsError` 限在 Windows 中可用。 

### OS 异常

下列异常均为 `[OSError](https://docs.python.org/zh-cn/3.8/library/exceptions.html)` 的子类，它们将根据系统错误代码被引发。

 *exception* `ChildProcessError` 当一个子进程上的操作失败时将被引发。 对应于 `errno` `ECHILD`。 

 *exception* `FileExistsError` 当试图创建一个已存在的文件或目录时将被引发。 对应于 `errno` `EEXIST`。 

 *exception* `FileNotFoundError` 当所请求的文件或目录不存在时将被引发。 对应于 `errno` `ENOENT`。 

 *exception* `PermissionError` 当在没有足够操作权限的情况下试图执行某个操作时将被引发 —— 例如缺少文件系统权限。 对应于 `errno` `EACCES` 和 `EPERM`。 

 *exception* `ProcessLookupError` 当给定的进程不存在时将被引发。 对应于 `errno` `ESRCH`。 

 *exception* `TimeoutError` 当一个系统函数发生系统级超时的情况下将被引发。 对应于 `errno` `ETIMEDOUT`。 

## 警告

下列异常被用作警告类别；请参阅 [警告类别](https://docs.python.org/zh-cn/3.8/library/warnings.html) 文档了解详情。

 *exception* `Warning` 警告类别的基类。 

 *exception* `UserWarning` 用户代码所产生警告的基类。 

 *exception* `DeprecationWarning` 如果所发出的警告是针对其他 Python 开发者的，则以此作为与已弃用特性相关警告的基类。 

 *exception* `PendingDeprecationWarning` 对于已过时并预计在未来弃用，但目前尚未弃用的特性相关警告的基类。 这个类很少被使用，因为针对未来可能的弃用发出警告的做法并不常见，而针对当前已有的弃用则推荐使用 `[DeprecationWarning](https://docs.python.org/zh-cn/3.8/library/exceptions.html)`。 

 *exception* `SyntaxWarning` 与模糊的语法相关的警告的基类。 

 *exception* `RuntimeWarning` 与模糊的运行时行为相关的警告的基类。 

 *exception* `FutureWarning` 如果所发出的警告是针对以 Python 所编写应用的最终用户的，则以此作为与已弃用特性相关警告的基类。 

 *exception* `ImportWarning` 与在模块导入中可能的错误相关的警告的基类。 

 *exception* `UnicodeWarning` 与 Unicode 相关的警告的基类。 

 *exception* `ResourceWarning` 

# 异常层次结构

内置异常的类层级结构如下：

```python
BaseException
 +-- SystemExit
 +-- KeyboardInterrupt
 +-- GeneratorExit
 +-- Exception
      +-- StopIteration
      +-- StopAsyncIteration
      +-- ArithmeticError
      |    +-- FloatingPointError
      |    +-- OverflowError
      |    +-- ZeroDivisionError
      +-- AssertionError
      +-- AttributeError
      +-- BufferError
      +-- EOFError
      +-- ImportError
      |    +-- ModuleNotFoundError
      +-- LookupError
      |    +-- IndexError
      |    +-- KeyError
      +-- MemoryError
      +-- NameError
      |    +-- UnboundLocalError
      +-- OSError
      |    +-- BlockingIOError
      |    +-- ChildProcessError
      |    +-- ConnectionError
      |    |    +-- BrokenPipeError
      |    |    +-- ConnectionAbortedError
      |    |    +-- ConnectionRefusedError
      |    |    +-- ConnectionResetError
      |    +-- FileExistsError
      |    +-- FileNotFoundError
      |    +-- InterruptedError
      |    +-- IsADirectoryError
      |    +-- NotADirectoryError
      |    +-- PermissionError
      |    +-- ProcessLookupError
      |    +-- TimeoutError
      +-- ReferenceError
      +-- RuntimeError
      |    +-- NotImplementedError
      |    +-- RecursionError
      +-- SyntaxError
      |    +-- IndentationError
      |         +-- TabError
      +-- SystemError
      +-- TypeError
      +-- ValueError
      |    +-- UnicodeError
      |         +-- UnicodeDecodeError
      |         +-- UnicodeEncodeError
      |         +-- UnicodeTranslateError
      +-- Warning
           +-- DeprecationWarning
           +-- PendingDeprecationWarning
           +-- RuntimeWarning
           +-- SyntaxWarning
           +-- UserWarning
           +-- FutureWarning
           +-- ImportWarning
           +-- UnicodeWarning
           +-- BytesWarning
           +-- ResourceWarning
```