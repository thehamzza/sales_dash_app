from pages import home, table_view, graph_view
from dash import html, dcc

# Navigation bar with icons
navbar = html.Div([
    dcc.Location(id='url', refresh=False),  # This component holds the URL information
    html.Div([
        dcc.Link(html.Div([html.I(className="fas fa-home"), " Home"], className='nav-item'), href='/'),
        dcc.Link(html.Div([html.I(className="fas fa-table"), " Table View"], className='nav-item'), href='/table'),
        dcc.Link(html.Div([html.I(className="fas fa-chart-bar"), " Graph View"], className='nav-item'), href='/graph'),
    ], className='navbar')
], className='header')


def get_layout(pathname):
    if pathname == '/table':
        return table_view.layout
    elif pathname == '/graph':
        return graph_view.layout
    return home.layout

