from datetime import datetime

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import plotly
import plotly.express as px

path = "/Users/chenxilin/Documents/bosc-logs/report.json"
pd.read_json(path)
data = pd.read_json(path)['data']

for i in range(len(data)):
    print(i)

    a = data[i]
    if a is np.nan:
        continue
    b = list(zip(a.keys(), a.values()))
    columns = ['timestamp', 'score', 'value']
    df = pd.DataFrame([[int(i[0]), i[1][0], i[1][2]]
                       for i in b], columns=columns)
    df = df.sort_values(by='timestamp')
    df['timestamp'] = df['timestamp'].map(
        lambda x: datetime.fromtimestamp(x / 1000))

    fig1 = px.line(x=df['timestamp'], y=df['value'])

    fig1.write_html('./result/%s value.html' % i)
    fig2 = px.scatter(x=df['timestamp'], y=df['score'])
    fig2.write_html('./result/%s score.html' % i)
