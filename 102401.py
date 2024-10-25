import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc

# 创建Dash应用
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# 定义布局
app.layout = dbc.Container([
    dbc.Row([
        dbc.Col(
            [
                dcc.Textarea(
                    id='input-text',
                    placeholder='输入一些文本...',
                    style={'width': '100%', 'height': '200px'}
                ),
                dbc.Button('处理', id='process-button',
                           color='primary', className='mt-2')
            ],
            width=6
        ),
        dbc.Col(
            [
                html.Div(id='output-text', style={'whiteSpace': 'pre-wrap'})
            ],
            width=6
        )
    ])
], fluid=True)

# 定义文本转换为Markdown的函数


def convert_to_markdown(text):
    lines = text.strip().split('\n')
    markdown_lines = []

    for line in lines:
        if line.strip():
            word, definition = line.split('/', 1)
            word = word.strip()
            markdown_lines.append(f"## {word}\n\n{line.strip()}\n")

    return '\n'.join(markdown_lines)

# 回调函数，处理按钮点击事件


@app.callback(
    Output('output-text', 'children'),
    Input('process-button', 'n_clicks'),
    Input('input-text', 'value')
)
def process_text(n_clicks, input_text):
    if n_clicks is None:
        return "处理结果将显示在这里..."
    else:
        # 调用convert_to_markdown函数处理文本
        processed_text = convert_to_markdown(input_text)
        return processed_text


# 运行应用
if __name__ == '__main__':
    app.run_server(debug=True)
