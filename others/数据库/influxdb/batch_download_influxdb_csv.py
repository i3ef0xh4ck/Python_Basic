import pandas as pd
from influxdb import DataFrameClient

client = DataFrameClient(host='172.31.3.1', port=8086, database='aiops_logwarn')  # 连接数据库
tables = list(map(lambda x: x['name'], client.get_list_measurements()))  # 获取所有表名
count = 0
for table in tables:
    sql = "select * from \"%s\"" % table
    result = client.query(sql)[table]
    columns = result.columns
    df = result[columns[list(map(lambda x: False if '-' in x else True, columns))]]
    for column in df.columns:
        df2 = df[column].reset_index()
        df2['index'] = df2['index'].map(lambda x: x.timestamp() * 1000)
        df2.dropna().to_csv("/Users/chenxilin/Code/Python/Python_Notes/数据库/influxdb/csv/%s.csv" %
                            count, header=False, index=False)
        print(count)
        count += 1
