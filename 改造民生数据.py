import os

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# var-adm-ras-platform-FSMountStatus
# 最后一个是类型class  FSMountStatus
# 其他的合到一起是进程 instance var-adm-ras-platform
# 所有的是指标名  var-adm-ras-platform-FSMountStatus


def get_new_name(filename):
    if '-' not in filename:
        return "class##instance##%s" % filename
    else:
        names = filename.split('-')
        return names[-1][:-4] + '##' + '-'.join(names[:-1]) + '##' + filename


def rename_all_files(dir):
    files = []
    for parent, dir_names, file_names in os.walk(dir):
        for filename in file_names:
            if filename[-3:] == 'csv':
                old_filename = parent + '/' + filename
                new_filename = parent + '/' + get_new_name(filename)
                os.rename(old_filename, new_filename)
                files.append(new_filename)
    return files


dir2 = "/Users/chenxilin/BizSeer/异常检测数据/日志聚合/node.pe.202002240737"
m = 0
for parent, dir_names, file_names in os.walk(dir2):
    for filename in file_names:
        if filename[-3:] == 'csv':
            old_filename = parent + '/' + filename
            try:
                df = pd.read_csv(old_filename, header=None)
                df.columns = ['time', 'value']
                m = max(m, df['time'].max())
            except:
                print(0)


dir = "/Users/chenxilin/BizSeer/异常检测数据/日志聚合/minsheng2/"
# 每行长这样 1.57596584E9,0.0   中间点是1575972300  一秒加1
files = rename_all_files(dir)
try:
    for i, file in enumerate(files):
        df = pd.read_csv(file, header=None)
        df.columns = ['time', 'value']
        n = len(df)
        m = int(n / 2)
        x = 0 if n % 2 == 0 else 1
        df['time'] = [1575972300 + 60 * i for i in range(m - n, n - m - x)]
        df['value'] = make_value(list(df['value']), True if i % 300 == 0 else False)
        df.to_csv(file, index=False, header=False)
        print(i)
except:
    print('error')


def make_value(array, use_rand):
    if use_rand:
        n = len(array)
        m = int(n / 2)
        array[m] += 5 + 40 * np.random.rand(1)[0]
        array[m + 1] += 10 + 40 * np.random.rand(1)[0]
        array[m + 2] += 21 + 40 * np.random.rand(1)[0]
        array[m + 3] += 45 + 40 * np.random.rand(1)[0]
        array[m + 4] += 56 + 40 * np.random.rand(1)[0]
        array[m + 5] += 46 + 40 * np.random.rand(1)[0]
        array[m + 6] += 30 + 40 * np.random.rand(1)[0]
        array[m + 7] += 19 + 40 * np.random.rand(1)[0]
        array[m + 8] += 9 + 40 * np.random.rand(1)[0]
        array[m + 9] += 4 + 40 * np.random.rand(1)[0]
    return array
