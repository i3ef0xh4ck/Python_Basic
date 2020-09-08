"""
批量测试日志异常检测算法性能
"""


import os
import subprocess
from datetime import datetime

import matplotlib.pyplot as plt
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots


def test_one_log(log_file):
    """测试一个日志文件"""
    jar_path_with_diff = "/Users/chenxilin/BackUp/carpenter-ksigma-diff-12-12.jar"
    jar_path_no_diff = "/Users/chenxilin/BackUp/carpenter-ksigma-12-12.jar"

    log_name = os.path.splitext(os.path.basename(log_file))[0]
    result_dir = 'result/' + log_name
    if not os.path.exists(result_dir):
        os.mkdir(result_dir)
    # 日志文件路径（每行是一条日志）
    arg1 = log_file
    # 模型输出路径
    arg2 = result_dir + '/model-' + log_name + '.json'
    # 格式化日志文件路径
    arg3 = result_dir + '/formatlog-' + log_name + '.json'
    # 输出检测结果路径
    arg4_with_diff = result_dir + '/with-diff-score-' + log_name + '.json'
    arg4_no_diff = result_dir + '/no-diff-score-' + log_name + '.json'

    cmd1 = "$SPARK_HOME/bin/spark-submit --master local[8] --class com.bizseer.anomaly.carpenter.CLI --conf spark.driver.memory=6g  %s train --log-input file --log-input-path %s --model-output file --model-output-path %s --debug --iterative" % (
        jar_path_no_diff, arg1, arg2)
    cmd2 = "python /Users/chenxilin/BackUp/jsonwrap.py --data_id log.mobile.bank.test.01 --log_input %s --log_output %s" % (
        arg1, arg3)
    cmd3_with_diff = "$SPARK_HOME/bin/spark-submit --master local[4] --class com.bizseer.anomaly.logpecker.CLI --conf spark.driver.memory=6g %s peck --batch-duration 3  --debug --json-key-field data_id --json-raw-field raw --model-input file --model-input-path  %s --log-input file --log-input-path %s --influxdb_address __ --log-output-path %s" % (
        jar_path_with_diff, arg2, arg3, arg4_with_diff)
    cmd3_no_diff = "$SPARK_HOME/bin/spark-submit --master local[4] --class com.bizseer.anomaly.logpecker.CLI --conf spark.driver.memory=6g %s peck --batch-duration 3  --debug --json-key-field data_id --json-raw-field raw --model-input file --model-input-path  %s --log-input file --log-input-path %s --influxdb_address __ --log-output-path %s" % (
        jar_path_no_diff, arg2, arg3, arg4_no_diff)
    subprocess.run(cmd1, shell=True)
    print(1)
    subprocess.run(cmd2, shell=True)
    print(2)
    subprocess.run(cmd3_with_diff, shell=True)
    print('3-with-diff')
    subprocess.run(cmd3_no_diff, shell=True)
    print('3-no-diff')
    # plot_score(arg4_with_diff, result_dir, diff=True)
    # plot_score(arg4_no_diff, result_dir, diff=False)
    try:
        data_with_diff = pd.read_json(arg4_with_diff)['data']
        data_no_diff = pd.read_json(arg4_no_diff)['data']
    except Exception as e:
        print(e)
        return
    for i in range(len(data_with_diff)):
        print(i)
        a = data_no_diff[i]
        a_ = data_with_diff[i]
        if not isinstance(a, dict):
            continue
        if not isinstance(a_, dict):
            continue
        columns = ['timestamp', 'value', 'score']
        b = list(zip(a.keys(), a.values()))
        b_ = list(zip(a_.keys(), a_.values()))
        df = pd.DataFrame([[int(i[0]), i[1][0], i[1][2]] for i in b], columns=columns)
        df = df.sort_values(by='timestamp')
        df['timestamp'] = df['timestamp'].map(lambda x: datetime.fromtimestamp(x / 1000))
        df_filter = df[df['score'] > 33]
        df_ = pd.DataFrame([[int(i[0]), i[1][0], i[1][2]] for i in b_], columns=columns)
        df_ = df_.sort_values(by='timestamp')
        df_['timestamp'] = df_['timestamp'].map(lambda x: datetime.fromtimestamp(x / 1000))
        df_['diff'] = df_['value'].diff().abs()
        df_filter_ = df_[df_['score'] > 33]

        fig = make_subplots(rows=3, cols=1, shared_xaxes=True)
        trace_no_diff_value = go.Line(x=df['timestamp'], y=df['value'], fillcolor='blue',
                                      name='原始数据(no diff)')
        trace_no_diff_abnormal = go.Scatter(
            x=df_filter['timestamp'], y=df_filter['value'], fillcolor='red', mode='markers',
            name='异常点')
        fig.append_trace(trace_no_diff_value, 1, 1)
        fig.append_trace(trace_no_diff_abnormal, 1, 1)

        trace_with_diff_value = go.Line(x=df_['timestamp'], y=df_['value'], fillcolor='blue',
                                        name='原始数据(with diff)')
        trace_with_diff_abnormal = go.Scatter(x=df_filter_['timestamp'], y=df_filter_[
            'value'], fillcolor='red', mode='markers', name='异常点')
        fig.append_trace(trace_with_diff_value, 2, 1)
        fig.append_trace(trace_with_diff_abnormal, 2, 1)

        trace_diff_value = go.Line(x=df_['timestamp'], y=df_['value'].diff().abs(),
                                   fillcolor='yellow', name='diff数据')
        trace_diff_abnormal = go.Scatter(x=df_filter_['timestamp'], y=df_filter_[
            'diff'], fillcolor='red', mode='markers', name='异常点')
        fig.append_trace(trace_diff_value, 3, 1)
        fig.append_trace(trace_diff_abnormal, 3, 1)
        fig.write_html(result_dir + '/' + '%s-result.html' % str(i))


def plot_score(json_file, save_path, diff=True):
    """检测分数绘图"""
    html = 'with-diff' if diff else 'no-diff'
    data = pd.read_json(json_file)['data']
    for i in range(len(data)):
        print(i)
        a = data[i]
        if not isinstance(a, dict):
            continue
        b = list(zip(a.keys(), a.values()))
        columns = ['timestamp', 'score', 'value']
        df = pd.DataFrame([[int(i[0]), i[1][0], i[1][2]] for i in b], columns=columns)
        df = df.sort_values(by='timestamp')
        df['timestamp'] = df['timestamp'].map(lambda x: datetime.fromtimestamp(x / 1000))
        df_filter = df[df['score'] > 33]

        trace1 = go.Line(x=df['timestamp'], y=df['value'], fillcolor='blue')
        trace2 = go.Line(x=df['timestamp'], y=df['value'].diff().abs(), fillcolor='yellow')
        trace3 = go.Scatter(x=df_filter['timestamp'], y=df_filter['value'], fillcolor='red',
                            mode='markers')

        fig = make_subplots(rows=2, cols=1, shared_xaxes=True)
        if diff:
            fig.append_trace(trace1, 1, 1)
            fig.append_trace(trace3, 1, 1)
            fig.append_trace(trace2, 2, 1)
            fig.append_trace(trace3, 2, 1)

        fig.write_html(save_path + '/' + html + '-%s-result.html' % str(i))


def get_log_files():
    """获取多个日志文件的路径"""
    log_files = [
        # 注释的都是没有结果的日志
        # '/Users/chenxilin/Code/Python/Python_Notes/log/application.log',
        '/Users/chenxilin/BackUp/spd-sorted-acd.txt',
        '/Users/chenxilin/Code/Python/Python_Notes/log/gc_mSrv1.log.17253.log',
        '/Users/chenxilin/Code/Python/Python_Notes/log/hsysaas-hkj.chanapp.chanjet.com.cn_access190901.log'
        # '/Users/chenxilin/Code/Python/Python_Notes/log/icbc-ceph-mon.prod.log',
        # '/Users/chenxilin/Code/Python/Python_Notes/log/spd-syslog-10k.txt',
        # '/Users/chenxilin/Code/Python/Python_Notes/log/bosc-logs/1.log',
        # '/Users/chenxilin/Code/Python/Python_Notes/log/bosc-logs/2.log',
        # '/Users/chenxilin/Code/Python/Python_Notes/log/bosc-logs/3.log',
        # '/Users/chenxilin/Code/Python/Python_Notes/log/bosc-logs/4.log',
        # '/Users/chenxilin/Code/Python/Python_Notes/log/bosc-logs/alert_oraabs_1.log',
        # '/Users/chenxilin/Code/Python/Python_Notes/log/bosc-logs/alert_oraaim_1.log',
        # '/Users/chenxilin/Code/Python/Python_Notes/log/bosc-logs/alert_oraamldb_1.log',
        # '/Users/chenxilin/Code/Python/Python_Notes/log/bosc-logs/alert_oraasphz_1.log',
        # '/Users/chenxilin/Code/Python/Python_Notes/log/bosc-logs/alert_oraftp_1.log',
        # '/Users/chenxilin/Code/Python/Python_Notes/log/bosc-logs/alert_orafund_1.log',
        # '/Users/chenxilin/Code/Python/Python_Notes/log/bosc-logs/alert_oramonx_1.log',
        # '/Users/chenxilin/Code/Python/Python_Notes/log/bosc-logs/alert_orancdb_1.log',
        # '/Users/chenxilin/Code/Python/Python_Notes/log/bosc-logs/alertoracledb01(cluster).log',
        # '/Users/chenxilin/Code/Python/Python_Notes/log/bosc-logs/listener.log',
        # '/Users/chenxilin/Code/Python/Python_Notes/log/cmbc-prd_logs/errors/weblogic.xBank2_N41_8003.8335_181125.log',
        # '/Users/chenxilin/Code/Python/Python_Notes/log/cmbc-prd_logs/weblogic.xBank2_N41_8003.8335_181124.log',
        # '/Users/chenxilin/Code/Python/Python_Notes/log/everbright-log/middle_ware_asfund.log',
        '/Users/chenxilin/Code/Python/Python_Notes/log/everbright-log/middle_ware_trade.log',
        # '/Users/chenxilin/Code/Python/Python_Notes/log/everbright-log/oracle.log',
        # '/Users/chenxilin/Code/Python/Python_Notes/log/everbright-param/240log/240log20190702.log',
        # '/Users/chenxilin/Code/Python/Python_Notes/log/everbright-param/241log/20190710.log',
        # '/Users/chenxilin/Code/Python/Python_Notes/log/friend_bank_4G_log_0702_0703_5am_9am/ceb-log_logic-0702.txt',
        # '/Users/chenxilin/Code/Python/Python_Notes/log/friend_bank_4G_log_0702_0703_5am_9am/ceb-log_logic-0703.txt',
        # '/Users/chenxilin/Code/Python/Python_Notes/log/guangfa-gateway/tradeInfo.log.2018-10-22.log',
        # '/Users/chenxilin/Code/Python/Python_Notes/log/is/cloud_dlog/as_fund-0-as_fund--1.alog',
        '/Users/chenxilin/Code/Python/Python_Notes/log/is/ehome_log/nginx_access.log',
        '/Users/chenxilin/Code/Python/Python_Notes/log/is/mot_log/117_20190110/117_outsender-7500.out',
        '/Users/chenxilin/Code/Python/Python_Notes/log/is/mot_log/118_20190110/118_outsender-7506.out',
        # '/Users/chenxilin/Code/Python/Python_Notes/log/is/mainsvr.log',
        # '/Users/chenxilin/Code/Python/Python_Notes/log/is/trade.log',
        '/Users/chenxilin/Code/Python/Python_Notes/log/new/10.78.134.14_messages',
        '/Users/chenxilin/Code/Python/Python_Notes/log/new/10.70.206.232_messages',
        '/Users/chenxilin/Code/Python/Python_Notes/log/szlog/influxdb/influxd.log',
        '/Users/chenxilin/Code/Python/Python_Notes/log/tmp/FY4A-X86-HW-4C-65.messages-20181217'
    ]
    return log_files[0:1]


def main():
    """批量测试多个日志文件"""
    log_files_not_exists = []  # 记录下不存在的日志文件
    log_files = get_log_files()
    for log_file in log_files:
        if not os.path.exists(log_file):
            print('日志文件不存在: %s' % log_file)
            log_files_not_exists.append(log_file)
        else:
            test_one_log(log_file)
    pd.DataFrame(log_files_not_exists).to_csv('不存在的日志.txt')


if __name__ == '__main__':
    main()
