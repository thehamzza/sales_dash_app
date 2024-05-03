# callbacks.py
from dash.dependencies import Input, Output
from app import app
import pages.home as home
import pages.table_view as table_view
import pages.graph_view as graph_view

# # Define the callback for dynamic page rendering
# @app.callback(Output('page-content', 'children'),
#               [Input('url', 'pathname')])

def display_page(pathname):
    if pathname == '/table':
        return table_view.layout
    elif pathname == '/graph':
        return graph_view.layout
    else:
        return home.layout  # Default to home layout if no specific path matched
