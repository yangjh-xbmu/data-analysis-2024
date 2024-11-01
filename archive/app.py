# 导入必要的库
import dash
from dash import dcc, html
from dash.dependencies import Input, Output

# 创建Dash应用实例
app = dash.Dash(__name__)

# 定义应用的布局
app.layout = html.Div([
    html.H1("最小化Dash应用示例"),  # 标题
    dcc.Slider(  # 滑块组件
        id='my-slider',
        min=0,
        max=10,
        step=1,
        value=5,
    ),
    html.Div(id='slider-output')  # 用于显示滑块值的区域
])

# 定义回调函数，用于更新滑块值的显示


@app.callback(
    Output('slider-output', 'children'),
    [Input('my-slider', 'value')]
)
def update_output(value):
    return f'滑块的值是: {value}'


# 运行应用
if __name__ == '__main__':
    app.run_server(debug=True)
