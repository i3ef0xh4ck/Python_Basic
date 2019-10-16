import os

# print(os.name, os.environ.get('path').split(';'))
# # 目录操作:
# print(os.path.abspath('.'))  # 查看当前目录的绝对路径
# print(os.path.join('C:\Code\Python\Basic\python3', 'testdir'))  # 目录的拼接
# os.mkdir(os.path.join('C:\Code\Python\Basic\python3', 'testdir'))  # 创建新目录
# os.rmdir(os.path.join('C:\Code\Python\Basic\python3', 'testdir'))  # 删除目录
# os.rename('test.txt', 'test2.txt')  # 文件重命名
# os.remove('test2.txt')  # 删除文件
# os.removedirs('path')  # 删除文件夹
print([x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1] == '.py'])  #当前文件夹所有py文件
