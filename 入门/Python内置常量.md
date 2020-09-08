有少数的常量存在于内置命名空间中。 它们是：

- **`False**[bool](<https://docs.python.org/zh-cn/3.8/library/functions.html#bool>)` 类型的假值。 给 `False` 赋值是非法的并会引发 `[SyntaxError](<https://docs.python.org/zh-cn/3.8/library/exceptions.html#SyntaxError>)`。
- **`True**[bool](<https://docs.python.org/zh-cn/3.8/library/functions.html#bool>)` 类型的真值。 给 `True` 赋值是非法的并会引发 `[SyntaxError](<https://docs.python.org/zh-cn/3.8/library/exceptions.html#SyntaxError>)`。
- **`None**NoneType` 类型的唯一值。 `None` 经常用于表示缺少值，当因为默认参数未传递给函数时。 给 `None` 赋值是非法的并会引发 `[SyntaxError](<https://docs.python.org/zh-cn/3.8/library/exceptions.html#SyntaxError>)`。
- **`NotImplemented`**二进制特殊方法应返回的特殊值（例如，`[__eq__()](<https://docs.python.org/zh-cn/3.8/reference/datamodel.html#object.__eq__>)`、`[__lt__()](<https://docs.python.org/zh-cn/3.8/reference/datamodel.html#object.__lt__>)`、`__add __()`、`[__rsub__()](<https://docs.python.org/zh-cn/3.8/reference/datamodel.html#object.__rsub__>)` 等）表示操作没有针对其他类型实现；为了相同的目的，可以通过就地二进制特殊方法（例如，`__imul __()`、`__ rightnd__()` 等）返回。 它的逻辑值为真。**注解** 当二进制（或就地）方法返回`NotImplemented`时，解释器将尝试对另一种类型（或其他一些回滚操作，取决于运算符）的反射操作。 如果所有尝试都返回`NotImplemented`，则解释器将引发适当的异常。 错误返回的`NotImplemented`将导致误导性错误消息或返回到Python代码中的`NotImplemented`值。参见 [实现算数运算](https://docs.python.org/zh-cn/3.8/library/numbers.html#implementing-the-arithmetic-operations) 为例。**注解** `NotImplementedError` 和 `NotImplemented` 不可互换，即使它们有相似的名称和用途。 有关何时使用它的详细信息，请参阅 `[NotImplementedError](<https://docs.python.org/zh-cn/3.8/library/exceptions.html#NotImplementedError>)`。
- **`Ellipsis`**与省略号文字字面 “`...`” 相同。 特殊值主要与用户定义的容器数据类型的扩展切片语法结合使用。
- **`__debug__`**如果 Python 没有以 `[O](<https://docs.python.org/zh-cn/3.8/using/cmdline.html#cmdoption-o>)` 选项启动，则此常量为真值。 另请参见 `[assert](<https://docs.python.org/zh-cn/3.8/reference/simple_stmts.html#assert>)` 语句。

变量名 `[None](<https://docs.python.org/zh-cn/3.8/library/constants.html#None>)`，`[False](<https://docs.python.org/zh-cn/3.8/library/constants.html#False>)`，`[True](<https://docs.python.org/zh-cn/3.8/library/constants.html#True>)` 和 `__ debug__` 无法重新赋值（赋值给它们，即使是属性名，将引发 `[SyntaxError](<https://docs.python.org/zh-cn/3.8/library/exceptions.html#SyntaxError>)` ），所以它们可以被认为是“真正的”常数。

# 由 site 模块添加的常量

`[site](<https://docs.python.org/zh-cn/3.8/library/site.html#module-site>)` 模块（在启动期间自动导入，除非给出 `[S](<https://docs.python.org/zh-cn/3.8/using/cmdline.html#id3>)` 命令行选项）将几个常量添加到内置命名空间。 它们对交互式解释器 shell 很有用，并且不应在程序中使用。

- **`quit`**(*code=None*)**`exit`**(*code=None*)当打印此对象时，会打印出一条消息，例如“Use quit() or Ctrl-D (i.e. EOF) to exit”，当调用此对象时，将使用指定的退出代码来引发 `[SystemExit](<https://docs.python.org/zh-cn/3.8/library/exceptions.html#SystemExit>)`。
- **`copyright`**
- **`credits`**打印或调用的对象分别打印版权或作者的文本。
- **`license`**当打印此对象时，会打印出一条消息“Type license() to see the full license text”，当调用此对象时，将以分页形式显示完整的许可证文本（每次显示一屏）。