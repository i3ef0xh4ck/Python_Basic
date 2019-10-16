from io import StringIO, BytesIO
# 数据读写不一定是文件,也可以在内存中读写
f = StringIO()
f.write("Hello")
f.write(' ')
f.write('World!')
print(f.getvalue())

f2 = StringIO("Hello!\nHi!\nGoodbye!")

while True:
    s = f2.readline()
    if s == '':
        break
    print(s.strip())
##################################################
f3 = BytesIO()
f3.write('中文'.encode('utf-8'))
print(f3.getvalue())

f4 = BytesIO(b'\xe4\xb8\xad\xe6\x96\x87')
print(f4.read())