
<!-- @import "[TOC]" {cmd="toc" depthFrom=1 depthTo=6 orderedList=false} -->
<!-- code_chunk_output -->

- [简单例子](#简单例子)
- [详细API](#详细api)
  - [InfluxDBClient](#influxdbclient)
    - [InfluxDBClient类的参数说明](#influxdbclient类的参数说明)
    - [InfluxDB类的方法](#influxdb类的方法)
  - [DataFrameClient](#dataframeclient)
    - [DataFrameClient类的参数说明](#dataframeclient类的参数说明)
    - [DataFrame类的方法](#dataframe类的方法)
- [详细例子](#详细例子)
  - [InfluxDBClient例子](#influxdbclient例子)
  - [DataFrameClient例子](#dataframeclient例子)

<!-- /code_chunk_output -->

[TOC]
# 简单例子
```python
from influxdb import InfluxDBClient
client = InfluxDBClient('localhost', 8086, 'aiops_logwarn')  # 连接数据库
client.create_database('example')  # 创建数据库


points = [ # 待写入数据库的点组成的列表
    {
        "measurement": "cpu_load_short",
        "tags": {
            "host": "server01",
            "region": "us-west"
        },
        "time": "2009-11-10T23:00:00Z",
        "fields": {
            "value": 0.64
        }
    }
]
client.write_points(points, database='example')  # 将这些点写入指定database
# 查询刚刚写入的点
result = client.query('select value from cpu_load_short;', database='example')
print(result)
```
```
ResultSet({'('cpu_load_short', None)': [{'time': '2009-11-10T23:00:00Z', 'value': 0.64}]})
```
# 详细API
要连接influxdb数据库，需创建一个influxdb client，目前支持两种客户端：
- InfluxDBClient
- DataFrameClient

## InfluxDBClient
可以使用以下几种连接方式来创建InfluxDBClient对象
```
from influxdb import InfluxDBClient

# using Http
client = InfluxDBClient(database='dbname')
client = InfluxDBClient(host='127.0.0.1', port=8086, database='dbname')
client = InfluxDBClient(host='127.0.0.1', port=8086, username='root', password='root', database='dbname')

# using UDP
client = InfluxDBClient(host='127.0.0.1', database='dbname', use_udp=True, udp_port=4444)
```

**InfluxDBClient类详细说明**

### InfluxDBClient类的参数说明
```python
class influxdb.InfluxDBClient(host=u'localhost', port=8086, username=u'root', password=u'root', database=None, ssl=False, verify_ssl=False, timeout=None, retries=3, use_udp=False, udp_port=4444, proxies=None, pool_size=10, path=u'', cert=None)
```

参数|说明
----|----
host|InfluxDB主机, 默认为 'localhost'
port (int)|端口号，默认8086
username (str)|用户名，默认root
password (str)|密码，默认root
pool_size (int)|urllib3 连接池大小，默认10
database (str) |要连接的数据库名，默认None
ssl (bool) |是否使用https连接InfluxDB，默认False
verify_ssl (bool)|是否对https请求采用ssl认证，默认False
timeout (int)|请求创建连接到客户端的timeout秒数，默认None
retries (int) |连接客户端重试次数，默认3
use_udp (bool)|是否使用udp连接InfluxDB, 默认False
udp_port (int) |UDP port, 默认4444
proxies (dict) | HTTP(S) 代理，默认为空dict
path (str) | 服务器上InfluxDB的连接路径, 默认为''
cert (str) – 客户端证书信息的路径，用于相互TLS身份验证。您可以指定本地证书，以用作包含私钥和证书的单个文件，也可以用作两个文件路径的元组，默认为None


### InfluxDB类的方法
- 修改数据库的现有保存策略
`alter_retention_policy(name, database=None, duration=None, replication=None, default=None, shard_duration=None)`
- 关闭http会话
`close()`
- 为数据库创建一个连续的查询
`create_continuous_query(name, select, database=None, resample_opts=None)`
- 在InfluxDB中创建一个新数据库
`create_database(dbname)`
- 为数据库创建保留策略
`create_retention_policy(name, duration, replication, database=None, default=False, shard_duration=u'0s')`
- 在InfluxDB中创建一个新用户
`create_user(username, password, admin=False)`
- 从数据库中删除Series
`delete_series(database=None, measurement=None, tags=None)`
- 删除现有的数据库连续查询
`drop_continuous_query(name, database=None)`
- 从InfluxDB中删除数据库
`drop_database(dbname)`
- 从InfluxDB中删除一个measurement
`drop_measurement(measurement)`
- 删除数据库的现有保留策略
`drop_retention_policy(name, database=None)`
- 从InfluxDB中删除用户
`drop_user(username)`
- 类方法：从给定的数据源名称生成一个InfluxDBClient实例
`classmethodfrom_dsn(dsn, **kwargs)`
举例：`cli = InfluxDBClient.from_dsn('influxdb://username:password@\localhost:8086/databasename', timeout=5)`
- 获取InfluxDB中连续查询的列表
`get_list_continuous_queries()`
- 获取InfluxDB中的数据库列表
`get_list_database()`
- 获取InfluxDB中的measurements列表
`get_list_measurements()`
- 获取授予给定用户的所有特权的列表
`get_list_privileges(username)`
- 获取数据库的保留策略列表
`get_list_retention_policies(database=None)`
- 获取InfluxDB中所有用户的列表
`get_list_users()`
- 向用户授予管理员权限
`grant_admin_privileges(username)`
- 向用户授予数据库权限
`grant_privilege(privilege, database, username)`
- 检查与InfluxDB的连接
`ping()`
- 查询
`query(query, params=None, bind_params=None, epoch=None, expected_response_code=200, database=None, raise_errors=True, chunked=False, chunk_size=0, method=u'GET')`
- 向InfluxDB API发出HTTP请求
`request(url, method=u'GET', params=None, data=None, expected_response_code=200, headers=None)`
- 撤消用户的管理员权限
`revoke_admin_privileges(username)`
- 撤消用户对数据库的权限
`revoke_privilege(privilege, database, username)`
- 发送UDP数据包
`send_packet(packet, protocol=u'json', time_precision=None)`
- 更改现有用户的密码
`set_user_password(username, password)`
- 更改客户端的数据库
`switch_database(database)`
- 更改客户端的用户名
`switch_user(username, password)`
- 写入数据库
`write(data, params=None, expected_response_code=204, protocol=u'json')`
- 写入多个时间序列名称
`write_points(points, time_precision=None, database=None, retention_policy=None, tags=None, batch_size=None, protocol=u'json', consistency=None)`

## DataFrameClient
### DataFrameClient类的参数说明
```python
classinfluxdb.DataFrameClient(host=u'localhost', port=8086, username=u'root', password=u'root', database=None, ssl=False, verify_ssl=False, timeout=None, retries=3, use_udp=False, udp_port=4444, proxies=None, pool_size=10, path=u'', cert=None)
```
和[InfluxDBClient类的参数说明](#influxdbclient类的参数说明)一致
### DataFrame类的方法
- 将数据查询到DataFrame中
`query(query, params=None, bind_params=None, epoch=None, expected_response_code=200, database=None, raise_errors=True, chunked=False, chunk_size=0, method=u'GET', dropna=True)`
- 写入多个时间序列名称
`write_points(dataframe, measurement, tags=None, tag_columns=None, field_columns=None, time_precision=None, database=None, retention_policy=None, batch_size=None, protocol=u'line', numeric_precision=None)`

# 详细例子
## InfluxDBClient例子
```python
import argparse

from influxdb import InfluxDBClient


def main(host='localhost', port=8086):
    """Instantiate a connection to the InfluxDB."""
    user = '用户名'
    password = '密码'
    dbname = '数据库名'
    dbuser = '数据库用户名'
    dbuser_password = '数据库用户密码'
    query = 'select Float_value from cpu_load_short;'
    query_where = 'select Int_value from cpu_load_short where host=$host;'
    bind_params = {'host': 'server01'}
    json_body = [
        {
            "measurement": "cpu_load_short",
            "tags": {
                "host": "server01",
                "region": "us-west"
            },
            "time": "2009-11-10T23:00:00Z",
            "fields": {
                "Float_value": 0.64,
                "Int_value": 3,
                "String_value": "Text",
                "Bool_value": True
            }
        }
    ]

    client = InfluxDBClient(host, port, user, password, dbname)

    print("创建数据库: " + dbname)
    client.create_database(dbname)

    print("创建retention策略")
    client.create_retention_policy('awesome_policy', '3d', 3, default=True)

    print("切换用户: " + dbuser)
    client.switch_user(dbuser, dbuser_password)

    print("写入points: {0}".format(json_body))
    client.write_points(json_body)

    print("查询数据: " + query)
    result = client.query(query)

    print("结果: {0}".format(result))

    print("查询data: " + query_where)
    result = client.query(query_where, bind_params=bind_params)

    print("结果: {0}".format(result))

    print("切换用户: " + user)
    client.switch_user(user, password)

    print("删除数据库: " + dbname)
    client.drop_database(dbname)


def parse_args():
    """解析args"""
    parser = argparse.ArgumentParser(
        description='example code to play with InfluxDB')
    parser.add_argument('--host', type=str, required=False,
                        default='localhost',
                        help='hostname of InfluxDB http API')
    parser.add_argument('--port', type=int, required=False, default=8086,
                        help='port of InfluxDB http API')
    return parser.parse_args()


if __name__ == '__main__':
    args = parse_args()
    main(host=args.host, port=args.port)
```
## DataFrameClient例子
```python
import argparse
import pandas as pd

from influxdb import DataFrameClient


def main(host='localhost', port=8086):
    user = 'root'
    password = 'root'
    dbname = 'demo'
    protocol = 'line'

    client = DataFrameClient(host, port, user, password, dbname)

    print("创建 pandas DataFrame")
    df = pd.DataFrame(data=list(range(30)),
                      index=pd.date_range(start='2014-11-16',
                                          periods=30, freq='H'), columns=['0'])

    print("创建数据库: " + dbname)
    client.create_database(dbname)

    print("将DataFrame写入数据库")
    client.write_points(df, 'demo', protocol=protocol)

    print("写带标签的DataFrame")
    client.write_points(df, 'demo',
                        {'k1': 'v1', 'k2': 'v2'}, protocol=protocol)

    print("查询")
    client.query("select * from demo")

    print("删除数据库: " + dbname)
    client.drop_database(dbname)


def parse_args():
    parser = argparse.ArgumentParser(
        description='example code to play with InfluxDB')
    parser.add_argument('--host', type=str, required=False,
                        default='localhost',
                        help='hostname of InfluxDB http API')
    parser.add_argument('--port', type=int, required=False, default=8086,
                        help='port of InfluxDB http API')
    return parser.parse_args()


if __name__ == '__main__':
    args = parse_args()
    main(host=args.host, port=args.port)
```
