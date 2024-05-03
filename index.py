from dash import html, dcc
from dash.dependencies import Input, Output
from app import app
import callbacks  # Import to register callbacks
import layouts

layout = html.Div([
    layouts.navbar,
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])

@app.callback(Output('page-content', 'children'), 
              [Input('url', 'pathname')])
def display_page(pathname):
    return layouts.get_layout(pathname)


if __name__ == '__main__':
    app.run_server(debug=True)
