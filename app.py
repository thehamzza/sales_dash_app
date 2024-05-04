# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.


from dash import Dash, html, dcc
import pandas as pd
import plotly.express as px
from dash.dependencies import Input, Output


app = Dash(__name__, suppress_callback_exceptions=True)


# # Define the layout of the app
# app.layout = html.Div([
#     dcc.Location(id='url', refresh=False), # This component holds the URL information

#     # Navigation bar
#     html.Div([
#         dcc.Link('Home', href='/', className='nav-links'),
#         dcc.Link('Table View', href='/table', className='nav-links'),
#         dcc.Link('Graph View', href='/graph', className='nav-links'),
#     ], className='header'),
    
#     html.Div(id='page-content', className='container')

# ])


# # Define the callback for dynamic page rendering
# @app.callback(Output('page-content', 'children'),
#               [Input('url', 'pathname')])

# def render_page_content(pathname):
#     if pathname == '/table':
#         # You would return the layout of the table view page here
#         return html.Div([
#             html.H1('Table View Page'),
#             # Your DataTable and associated components would go here
#         ])
#     elif pathname == '/graph':
#         # You would return the layout of the graph view page here
#         return html.Div([
#             html.H1('Graph View Page'),
#             # Your graph and associated components would go here
#         ])
    
#     else:
#             # The default layout when navigating to the Home page
#             return html.Div([
#                 html.H1('Home Page'),
#                 html.P('Welcome to the Dash Superstore Data Application!')
#                 # Your home page content would go here
#             ])


# Add external CSS and JavaScript if needed
# app.css.append_css({'external_url': 'URL_TO_EXTERNAL_CSS'})
# app.scripts.append_script({'external_url': 'URL_TO_EXTERNAL_JAVASCRIPT'})

# Only run the server if this script is executed directly (not imported)

server = app.server  # Expose server for Gunicorn or other servers