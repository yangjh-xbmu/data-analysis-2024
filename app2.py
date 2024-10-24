import dash
from dash import dcc, html, Input, Output, State
import dash_bootstrap_components as dbc
import markdown

# 初始化 Dash 应用
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# 定义布局
app.layout = dbc.Container([
    dbc.Row([
        # 左侧分栏
        dbc.Col([
            dbc.Textarea(
                id='markdown-input', placeholder='输入 Markdown 内容...', style={'height': '200px'}),
            dbc.Button('生成卡片', id='generate-button',
                       color='primary', className='mt-2')
        ], width=6),

        # 右侧分栏
        dbc.Col([
            html.Div(id='markdown-output', className='border p-3',
                     style={'min-height': '200px'})
        ], width=6)
    ])
], fluid=True)

# 回调函数：点击按钮后生成 Markdown 卡片


@app.callback(
    Output('markdown-output', 'children'),
    Input('generate-button', 'n_clicks'),
    State('markdown-input', 'value')
)
def update_output(n_clicks, markdown_text):
    if n_clicks is None:
        return ''
    if markdown_text:
        # 将 Markdown 转换为 HTML
        html_content = markdown.markdown(markdown_text)
        return html.Div(dangerously_allow_html=True, children=html_content)
    return ''


# 运行应用
if __name__ == '__main__':
    app.run_server(debug=True)
