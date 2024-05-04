# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.


from dash import Dash, html, dcc
import pandas as pd
import plotly.express as px
from dash.dependencies import Input, Output


app = Dash(__name__, suppress_callback_exceptions=True)


server = app.server  # Expose server for Gunicorn or other servers