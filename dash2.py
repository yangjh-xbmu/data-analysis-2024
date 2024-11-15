import dash
from dash import dcc, html, Input, Output
import dash_bootstrap_components as dbc
import pandas as pd
import itertools
import plotly.express as px

# 初始化 Dash 应用
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# 定义应用布局
app.layout = dbc.Container([
    dbc.Row([
        dbc.Col(html.H1("随机数组合与平均值分析"), className="mb-4")
    ]),
    dbc.Row([
        dbc.Col([
            html.Label("请输入 10 个随机数（用逗号分隔）:"),
            dcc.Input(id='input-numbers', type='text',
                      placeholder='例如: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10'),
            html.Button('生成组合', id='generate-button', n_clicks=0),
        ], width=6),
    ]),
    dbc.Row([
        dbc.Col([
            dcc.Graph(id='scatter-plot')
        ], width=12),
    ]),
    dbc.Row([
        dbc.Col([
            html.Div(id='output-dataframe')
        ], width=12),
    ]),
])

# 定义回调函数


@app.callback(
    [Output('scatter-plot', 'figure'),
     Output('output-dataframe', 'children')],
    [Input('generate-button', 'n_clicks')],
    [Input('input-numbers', 'value')]
)
def update_output(n_clicks, input_numbers):
    if n_clicks == 0 or not input_numbers:
        return {}, "请输入 10 个随机数并点击生成组合按钮。"

    # 解析用户输入的数字
    try:
        numbers = list(map(float, input_numbers.split(',')))
        if len(numbers) != 10:
            return {}, "请输入 10 个随机数。"
    except ValueError:
        return {}, "输入格式不正确，请用逗号分隔数字。"

    # 生成所有可能的组合
    combinations = list(itertools.combinations(numbers, 2))

    # 计算每个组合的平均值
    data = []
    for comb in combinations:
        avg = sum(comb) / 2
        data.append({'抽样元素1': comb[0], '抽样元素2': comb[1], '样本平均值': avg})

    # 创建 DataFrame
    df = pd.DataFrame(data)

    # 按平均值排序
    df = df.sort_values(by='样本平均值', ascending=False).reset_index(drop=True)

    # 添加“平均值出现次数”列
    df['平均值出现次数'] = df.groupby('样本平均值').cumcount() + 1

    # 重新按平均值排序（由低到高）
    df = df.sort_values(by='样本平均值').reset_index(drop=True)

    # 绘制散点图
    fig = px.scatter(df, x='样本平均值', y='平均值出现次数', title='平均值与出现次数散点图')

    # 显示 DataFrame
    df_table = dbc.Table.from_dataframe(
        df, striped=True, bordered=True, hover=True)

    return fig, df_table


# 运行应用
if __name__ == '__main__':
    app.run_server(debug=True)
