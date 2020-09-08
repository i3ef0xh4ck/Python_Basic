Python基础知识

<!-- @import "[TOC]" {cmd="toc" depthFrom=1 depthTo=6 orderedList=false} -->

<!-- code_chunk_output -->

- [入门](#入门入门)
- [二进制数据服务](#二进制数据服务二进制数据服务)
- [数字和数学模块](#数字和数学模块数字和数学模块)
- [文件和目录访问](#文件和目录访问)
- [文件格式](#文件格式)
- [通用操作系统服务](#通用操作系统服务)
- [互联网数据处理](#互联网数据处理)
- [互联网协议和支持](#互联网协议和支持)
- [GUI](#gui)
- [调试和分析](#调试和分析)
- [Python运行时的服务](#python运行时的服务)
- [文本处理](#文本处理)
- [数据库](#数据库)
- [数据类型](#数据类型)
- [函数式编程模块](#函数式编程模块)
- [数据持久化](#数据持久化)
- [数据压缩与存档](#数据压缩与存档)
- [加密服务](#加密服务)
- [多线程与多进程](#多线程与多进程)
- [contextvars 上下文变量](#contextvars-上下文变量)
- [网络和进程间通信](#网络和进程间通信)
- [结构化标记处理工具](#结构化标记处理工具)
- [多媒体服务](#多媒体服务)
- [国际化](#国际化)
- [程序框架](#程序框架)
- [开发工具](#开发工具)
- [软件打包和分发](#软件打包和分发)
- [自定义Python解释器](#自定义python解释器)
- [导入模块](#导入模块)
- [Python语言服务](#python语言服务)

<!-- /code_chunk_output -->

## [入门](/入门)

---

[Hello World](/入门/Python_Hello_World.md)

[基本数据类型](/入门/Python基本数据类型.md)

[函数](/入门/Python函数.md)

[流程控制](/入门/Python流程控制.md)

[输入输出](/入门/Python输入输出.md)

[错误和异常](/入门/Python错误和异常.md)

[面向对象编程](/入门/Python面向对象编程.md)

[标准库简介](/入门/Python标准库简介.md)

[虚拟环境和包](/入门/Python虚拟环境和包.md)

[内置函数](/入门/Python内置函数.md)

[内置常量](/入门/Python内置常量.md)

[内置类型](/入门/Python内置类型.md)

[内置异常](/入门/Python内置异常.md)

## [二进制数据服务](/二进制数据服务)

---

[struct --- 将字节串解读为打包的二进制数据](/二进制数据服务/struct---将字节串解读为打包的二进制数据.md)

[codecs --- 编解码器注册和相关基类](/二进制数据服务/codecs---编解码器注册和相关基类.md)

## [数字和数学模块](/数字和数学模块)

---

[numbers --- 数字的抽象基类](.md)

[math --- 数学函数](.md)

[cmath --- 关于复数的数学函数](.md)

[decimal --- 十进制定点和浮点运算](.md)

[fractions --- 分数](.md)

[random --- 生成伪随机数](.md)

[statistics --- 数学统计函数](.md)

## 文件和目录访问

---

[pathlib --- 面向对象的文件系统路径](.md)

[os.path --- 常用路径操作](.md)

[fileinput --- 迭代来自多个输入流的行](.md)

[stat --- 解析 stat() 结果](.md)

[filecmp --- 文件及目录的比较](.md)

[tempfile --- 生成临时文件和目录](.md)

[glob --- Unix 风格路径名模式扩展](.md)

[fnmatch --- Unix 文件名模式匹配](.md)

[linecache --- 随机读写文本行](.md)

[shutil --- 高阶文件操作](.md)

## 文件格式

---

[csv --- CSV 文件读写](.md)

[configparser --- 配置文件解析器](.md)

[netrc --- netrc 文件处理](.md)

[xdrlib --- 编码与解码 XDR 数据](.md)

[plistlib --- 生成与解析 Mac OS X .plist 文件](.md)

## 通用操作系统服务

---

[os --- 多种操作系统接口](.md)

[io --- 处理流的核心工具](.md)

[time --- 时间的访问和转换](.md)

[argparse --- 命令行选项、参数和子命令解析器](.md)

[getopt --- C 风格的命令行选项解析器](.md)

[logging --- Python 的日志记录工具](.md)

[logging.config --- 日志记录配置](.md)

[logging.handlers --- 日志处理](.md)

[getpass --- 便携式密码输入工具](.md)

[curses --- 终端字符单元显示的处理](.md)

[curses --- 终端字符单元显示的处理](.md)

[curses.ascii --- Utilities for ASCII characters](.md)

[curses.panel --- curses 的 panel 栈扩展 ](.md)

[platform --- 获取底层平台的标识数据](.md)

[errno --- 标准 errno 系统符号](.md)

[ctypes --- Python 的外部函数库](.md)

## 互联网数据处理

---

[email --- 电子邮件与 MIME 处理包](.md)

[json --- JSON 编码和解码器](.md)

[mailcap --- Mailcap 文件处理](.md)

[mailbox --- Manipulate mailboxes in various formats](.md)

[mimetypes --- Map filenames to MIME types](.md)

[base64 --- Base16, Base32, Base64, Base85 数据编码](.md)

[binhex --- 对binhex4文件进行编码和解码](.md)

[binascii --- 二进制和 ASCII 码互转](.md)

[quopri --- 编码与解码经过 MIME 转码的可打印数据](.md)

[uu --- 对 uuencode 文件进行编码与解码](.md)

## 互联网协议和支持

---

[webbrowser --- 方便的Web浏览器控制器](.md)

[cgi --- Common Gateway Interface support](.md)

[cgitb --- 用于 CGI 脚本的回溯管理器](.md)

[wsgiref --- WSGI Utilities and Reference Implementation — Python 3.8.5 文档](.md)

[urllib --- URL 处理模块 — Python 3.8.5 文档](.md)

[urllib.request --- 用于打开 URL 的可扩展库 — Python 3.8.5 文档](.md)

[urllib.request --- 用于打开 URL 的可扩展库 — Python 3.8.5 文档](.md)

[urllib.parse --- Parse URLs into components — Python 3.8.5 文档](.md)

[urllib.error --- urllib.request 引发的异常类 — Python 3.8.5 文档](.md)

[urllib.robotparser --- robots.txt 语法分析程序 — Python 3.8.5 文档](.md)

[http --- HTTP 模块 — Python 3.8.5 文档](.md)

[http.client --- HTTP 协议客户端 — Python 3.8.5 文档](.md)

[ftplib --- FTP 协议客户端 — Python 3.8.5 文档](.md)

[poplib --- POP3 protocol client — Python 3.8.5 文档](.md)

[imaplib --- IMAP4 protocol client — Python 3.8.5 文档](.md)

[nntplib --- NNTP protocol client — Python 3.8.5 文档](.md)

[smtplib ---SMTP协议客户端 — Python 3.8.5 文档](.md)

[smtpd --- SMTP 服务器 — Python 3.8.5 文档](.md)

[telnetlib --- Telnet client — Python 3.8.5 文档](.md)

[uuid --- UUID objects according to RFC 4122 — Python 3.8.5 文档](.md)

[socketserver --- A framework for network servers — Python 3.8.5 文档](.md)

[http.server --- HTTP 服务器 — Python 3.8.5 文档](.md)

[http.cookies --- HTTP状态管理 — Python 3.8.5 文档](.md)

[http.cookiejar —— HTTP 客户端的 Cookie 处理 — Python 3.8.5 文档](.md)

[xmlrpc --- XMLRPC 服务端与客户端模块 — Python 3.8.5 文档](.md)

[xmlrpc.client --- XML-RPC client access — Python 3.8.5 文档](.md)

[xmlrpc.server --- Basic XML-RPC servers — Python 3.8.5 文档](.md)

[ipaddress --- IPv4/IPv6 操作库 — Python 3.8.5 文档](.md)

## GUI

---

[tkinter --- Tcl/Tk的Python接口](.md)

[tkinter.ttk --- Tk主题小部件](.md)

[tkinter.tix --- Extension widgets for Tk](.md)

[tkinter.scrolledtext --- 滚动文字控件](.md)

[IDLE](.md)

[其他图形用户界面（GUI）包](.md)

## 调试和分析

---

[审计事件表](.md)

[bdb --- Debugger framework](.md)

[faulthandler --- Dump the Python traceback](.md)

[pdb --- Python的调试器](.md)

[Python Profilers 分析器](.md)

[timeit --- 测量小代码片段的执行时间](.md)

[trace --- 跟踪Python语句的执行](.md)

[tracemalloc --- 跟踪内存分配](.md)

## Python运行时的服务

---

[sys --- 系统相关的参数和函数](.md)

[sysconfig --- Provide access to Python's configuration information](.md)

[builtins --- 内建对象](.md)

[__main__ --- 顶层脚本环境](.md)

[warnings --- Warning control](.md)

[dataclasses --- 数据类](.md)

[contextlib --- 为 with语句上下文提供的工具](.md)

[abc --- 抽象基类](.md)

[atexit --- 退出处理器](.md)

[traceback --- 打印或检索堆栈回溯](.md)

[__future__ --- Future 语句定义](.md)

[gc --- 垃圾回收器接口](.md)

[inspect --- 检查对象](.md)

[site —— 指定域的配置钩子](.md)

## 文本处理

---

[string --- 常见的字符串操作](.md)

[re --- 正则表达式操作](.md)

[difflib --- 计算差异的辅助工具](.md)

[textwrap --- 文本自动换行与填充](.md)

[unicodedata --- Unicode 数据库](.md)

[stringprep --- 因特网字符串预备](.md)

[readline --- GNU readline 接口](.md)

[rlcompleter --- GNU readline 的补全函数](.md)

## 数据库

---

[MySQL](.md)

[Mongo](.md)

[Redis](.md)

[Influxdb](.md)

## 数据类型

---

[datetime --- 基本的日期和时间类型](.md)

[calendar --- 日历相关函数](.md)

[collections --- 容器数据类型](.md)

[collections.abc --- 容器的抽象基类](.md)

[heapq --- 堆队列算法](.md)

[bisect --- 数组二分查找算法](.md)

[array --- 高效的数值数组](.md)

[weakref --- 弱引用](.md)

[types --- 动态类型创建和内置类型名称](.md)

[copy --- 浅层 (shallow) 和深层 (deep) 复制操作](.md)

[pprint --- 数据美化输出](.md)

[reprlib --- 另一种 repr() 实现](.md)

[enum --- 对枚举的支持](.md)

## 函数式编程模块

---

[itertools --- 为高效循环而创建迭代器的函数](.md)

[functools --- 高阶函数和可调用对象上的操作](.md)

[operator --- 标准运算符替代函数](.md)

## 数据持久化

---

[pickle --- Python 对象序列化](.md)

[copyreg --- 注册配合 pickle 模块使用的函数](.md)

[shelve --- Python 对象持久化](.md)

[marshal --- 内部 Python 对象序列化](.md)

[dbm --- Unix "数据库" 接口](.md)

[sqlite3 --- SQLite 数据库 DB-API 2.0 接口模块](.md)

## 数据压缩与存档

---

[zlib --- 与 gzip 兼容的压缩](.md)

[gzip --- 对 gzip 格式的支持](.md)

[bz2 --- 对 bzip2 压缩算法的支持](.md)

[lzma --- 用 LZMA 算法压缩](.md)

[zipfile --- 使用ZIP存档](.md)

[tarfile --- 读写tar归档文件](.md)

## 加密服务

---

[hashlib --- 安全哈希与消息摘要](.md)

[hmac --- 基于密钥的消息验证](.md)

[secrets --- 生成安全随机数字用于管理密码](.md)

## 多线程与多进程

---

[threading --- 基于线程的并行](.md)

[multiprocessing --- 基于进程的并行](.md)

[multiprocessing.shared_memory --- 可从进程直接访问的共享内存](.md)

[concurrent.futures --- 启动并行任务](.md)

[subprocess --- 子进程管理](.md)

[sched --- 事件调度器](.md)

[queue --- 一个同步的队列类](.md)

## contextvars 上下文变量

---

[contextvars 上下文变量](.md)

## 网络和进程间通信

---

[asyncio --- 异步 I/O](.md)

[socket --- 底层网络接口](.md)

[ssl --- 套接字对象的TLS/SSL封装](.md)

[select --- 等待 I/O 完成](.md)

[selectors --- 高级 I/O 复用库](.md)

[asyncore --- 异步socket处理器](.md)

[signal --- 设置异步事件处理程序](.md)

[mmap --- 内存映射文件支持](.md)

## 结构化标记处理工具

---

[html --- 超文本标记语言支持](.md)

[html.parser --- 简单的 HTML 和 XHTML 解析器](.md)

[html.entities --- HTML 一般实体的定义](.md)

[XML处理模块](.md)

[xml.etree.ElementTree --- ElementTree XML API](.md)

[xml.dom --- The Document Object Model API](.md)

[xml.dom.minidom --- Minimal DOM implementation](.md)

[xml.dom.pulldom --- Support for building partial DOM trees](.md)

[xml.sax --- Support for SAX2 parsers](.md)

[xml.sax.handler --- Base classes for SAX handlers](.md)

[xml.sax.saxutils --- SAX 工具集](.md)

[xml.sax.xmlreader --- Interface for XML parsers](.md)

[xml.parsers.expat --- Fast XML parsing using Expat](.md)

## 多媒体服务

---

[audioop --- Manipulate raw audio data — Python 3.8.5 文档](.md)

[aifc --- Read and write AIFF and AIFC files — Python 3.8.5 文档](.md)

[sunau --- 读写 Sun AU 文件 — Python 3.8.5 文档](.md)

[wave --- 读写WAV格式文件 — Python 3.8.5 文档](.md)

[chunk --- 读取 IFF 分块数据 — Python 3.8.5 文档](.md)

[colorsys --- 颜色系统间的转换 — Python 3.8.5 文档](.md)

[imghdr --- 推测图像类型 — Python 3.8.5 文档](.md)

[sndhdr --- 推测声音文件的类型 — Python 3.8.5 文档](.md)

[ossaudiodev --- Access to OSS-compatible audio devices — Python 3.8.5 文档](.md)

## 国际化

---

[gettext --- 多语种国际化服务](.md)

[locale --- 国际化服务](.md)

## 程序框架

---

[turtle --- 海龟绘图](.md)

[cmd --- 支持面向行的命令解释器](.md)

[shlex --- Simple lexical analysis](.md)

## 开发工具

---

[typing --- 类型标注支持](.md)

[pydoc --- 文档生成器和在线帮助系统](.md)

[doctest --- 测试交互性的Python示例](.md)

[unittest --- 单元测试框架](.md)

[unittest.mock --- 模拟对象库](.md)

[unittest.mock 上手指南](.md)

[2to3 - 自动将 Python 2 代码转为Python3代码](.md)

[test --- Python回归测试包](.md)

## 软件打包和分发

---

[distutils --- 构建和安装 Python 模块](.md)

[ensurepip --- Bootstrapping the pip installer](.md)

[venv --- 创建虚拟环境](.md)

[zipapp --- Manage executable Python zip archives](.md)

## 自定义Python解释器

---

[code --- 解释器基类](.md)

[codeop --- 编译Python代码](.md)

## 导入模块

---

[zipimport --- 从 Zip 存档中导入模块](.md)

[pkgutil --- 包扩展工具](.md)

[modulefinder --- 查找脚本使用的模块](.md)

[runpy --- Locating and executing Python modules](.md)

[importlib --- import 的实现](.md)

[Using importlib.metadata](.md)

## Python语言服务

---

[parser --- 访问 Python 解析树](.md)

[ast --- 抽象语法树](.md)

[symtable --- Access to the compiler's symbol tables](.md)

[symbol --- 与 Python 解析树一起使用的常量](.md)

[token --- 与Python解析树一起使用的常量](.md)

[keyword --- 检验Python关键字](.md)

[tokenize --- 对 Python 代码使用的标记解析器](.md)

[tabnanny --- 模糊缩进检测](.md)

[pyclbr --- Python module browser support](.md)

[py_compile --- Compile Python source files](.md)

[compileall --- Byte-compile Python libraries](.md)

[dis --- Python 字节码反汇编器](.md)

[pickletools --- pickle 开发者工具集](.md)

---