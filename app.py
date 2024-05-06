# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.


from dash import Dash, html, dcc
import pandas as pd
import plotly.express as px
from dash.dependencies import Input, Output
import os

# favicon_path = "/assets/favicon.ico"
# favicon_path = os.path.join(os.getcwd(), favicon_path)


app = Dash(__name__, suppress_callback_exceptions=True, external_stylesheets=[
    'https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.1/css/all.min.css'])


#app._favicon = (favicon_path)
app.title = 'Superstores Dash App'

server = app.server  # Expose server for Gunicorn or other servers