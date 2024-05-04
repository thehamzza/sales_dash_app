from pages import home, table_view, graph_view
from dash import html, dcc

# Assume each module returns a layout function or a layout property

#Navigation bar
navbar = html.Div([

    dcc.Location(id='url', refresh=False), # This component holds the URL information

    dcc.Link('Home', href='/', className='nav-links'),
    dcc.Link('Table View', href='/table', className='nav-links'),
    dcc.Link('Graph View', href='/graph', className='nav-links'),
], className='header')

def get_layout(pathname):
    if pathname == '/table':
        return table_view.layout
    elif pathname == '/graph':
        return graph_view.layout
    return home.layout

