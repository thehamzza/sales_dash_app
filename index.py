from dash import html, dcc
from dash.dependencies import Input, Output
from app import app
import layouts

app.layout = html.Div([
    layouts.navbar,
    html.Div(id='page-content')
])

@app.callback(Output('page-content', 'children'), 
              [Input('url', 'pathname')])
def display_page(pathname):
    return layouts.get_layout(pathname)


if __name__ == '__main__':
    #for local server i.e development
    app.run_server(debug=True)
    
    #for production server    
    app.run_server(debug=False, host='0.0.0.0', port=5000)
    
