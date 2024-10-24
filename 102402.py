import dash
from dash import dcc, html, Input, Output
import dash_bootstrap_components as dbc
import mytools

# 创建 Dash 应用实例
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# 定义应用程序的布局
app.layout = dbc.Container([
    dbc.Row([
        dbc.Col([
            html.Div([
                dcc.Textarea(
                    id='input-text',
                    placeholder='Enter some text...',
                    style={'width': '100%', 'height': '200px'}
                ),
                html.Button('Explain', id='explain-button', n_clicks=0, className='mt-2'),
            ], style={'padding': '20px', 'background': 'linear-gradient(to right, #f0f8ff, #e0ffff)'}),
        ], width=6),
        dbc.Col([
            html.Div(id='output-area', style={'padding': '20px', 'background': 'linear-gradient(to left, #f0f8ff, #e0ffff)', 'height': '100%', 'border-left': '1px solid #ccc'}),
        ], width=6),
    ], style={'height': '100vh'}),
], fluid=True)

# 定义回调函数
@app.callback(
    Output('output-area', 'children'),
    Input('explain-button', 'n_clicks'),
    Input('input-text', 'value')
)
def update_output(n_clicks, input_text):
    if n_clicks > 0 and input_text:
        # 调用 mytools 模块中的 cognitive_load_explain 函数
        explanation = mytools.cognitive_load_explain(input_text)
        return html.Div([
            html.H4("Explanation:"),
            html.P(explanation)
        ])
    return html.Div()

# 运行应用程序
if __name__ == '__main__':
    app.run_server(debug=True)
