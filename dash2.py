import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import itertools
from collections import Counter

# 创建 Dash 应用程序
app = dash.Dash(__name__)

# 定义应用程序布局
app.layout = html.Div([
    html.H1("随机数抽样分布"),
    html.Div([
        html.Label("输入 10 个随机数 (用逗号分隔):"),
        dcc.Input(id='input-numbers', type='text',
                  placeholder='例如: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10'),
        html.Button('生成抽样分布', id='submit-button', n_clicks=0),
    ]),
    dcc.Graph(id='sampling-distribution-plot')
])

# 定义回调函数


@app.callback(
    Output('sampling-distribution-plot', 'figure'),
    [Input('submit-button', 'n_clicks')],
    [Input('input-numbers', 'value')]
)
def update_graph(n_clicks, input_numbers):
    if n_clicks > 0 and input_numbers:
        # 将输入的字符串转换为整数列表
        numbers = list(map(int, input_numbers.split(',')))

        # 生成所有可能的组合
        combinations = list(itertools.combinations(numbers, 2))

        # 计算每个组合的平均值
        averages = [(comb[0] + comb[1]) / 2 for comb in combinations]

        # 计算每个平均值的出现次数
        average_counts = Counter(averages)

        # 将平均值和出现次数转换为散点图数据
        x = list(average_counts.keys())
        y = list(average_counts.values())

        # 创建散点图
        figure = go.Figure(data=[go.Scatter(x=x, y=y, mode='markers')])
        figure.update_layout(
            title='抽样分布散点图', xaxis_title='组合的平均值', yaxis_title='平均值出现的次数')

        return figure
    else:
        return {}


# 运行应用程序
if __name__ == '__main__':
    app.run_server(debug=True)
