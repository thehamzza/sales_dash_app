# import dash
# from dash import html, dcc, Input, Output, callback
# from dash import dash_table 
# import pandas as pd
# from datetime import datetime as dt
# from data import data_loader as dl


# df = dl.load_data()
# #keeping this column name for simplicity
# date='Order Date'

# df[date] = pd.to_datetime(df[date])  # Ensure the date column is in datetime format


# # Define the layout
# layout = html.Div([
#     html.H1("Data Analysis Dashboard"),
#     dcc.DatePickerRange(
#         id='date-picker-range',
#         min_date_allowed=df[date].min(),
#         max_date_allowed=df[date].max(),
#         start_date=df[date].min(),
#         end_date=df[date].max()
#     ),
#     dcc.Dropdown(
#         id='granularity-dropdown',
#         options=[
#             {'label': 'Week', 'value': 'W'},
#             {'label': 'Month', 'value': 'M'},
#             {'label': 'Quarter', 'value': 'Q'},
#             {'label': 'Year', 'value': 'Y'}
#         ],
#         value='M',  # Default to Month
#         clearable=False
#     ),
#     html.Div(id='filtered-data-display'),
#     dcc.Graph(id='data-graph')
# ])

# # Callback to filter data and update the table and graph
# @callback(
#     [Output('filtered-data-display', 'children'),
#      Output('data-graph', 'figure')],
#     [Input('date-picker-range', 'start_date'),
#      Input('date-picker-range', 'end_date'),
#      Input('granularity-dropdown', 'value')]
# )
# def update_output(start_date, end_date, granularity):
#     # Filter data based on the date range
#     mask = (df[date] >= start_date) & (df[date] <= end_date)
#     filtered_df = df.loc[mask]

#     # Resample data based on selected granularity
#     if granularity:
#         filtered_df.set_index(date, inplace=True)
#         numeric_cols = filtered_df.select_dtypes(include=['number'])  # Ensure only numeric columns are processed
#         if not numeric_cols.empty:
#             aggregated_df = numeric_cols.resample(granularity).mean().reset_index()
#         else:
#             return "No numeric data available for aggregation", {}

#     # Display the filtered DataFrame (limited to 5 rows)
#     display_df = aggregated_df.head(5).to_dict('records')
#     display_columns = [{'name': col, 'id': col} for col in aggregated_df.columns]

#     # Prepare a simple line graph of the aggregated data
#     # Assuming the first numeric column is what you want to plot
#     first_numeric_col = numeric_cols.columns[0] if not numeric_cols.empty else None
#     fig = {
#         'data': [{'x': aggregated_df[date], 'y': aggregated_df[first_numeric_col], 'type': 'line'}],
#         'layout': {'title': 'Aggregated Data'}
#     }

#     return [dash_table.DataTable(data=display_df, columns=display_columns), fig]



import dash
from dash import html, dcc, Input, Output, callback
from dash import dash_table
import pandas as pd
from datetime import datetime as dt
from data import data_loader as dl

df = dl.load_data()

# Convert dates to datetime and calculate Days to Ship
df['Order Date'] = pd.to_datetime(df['Order Date'])
df['Ship Date'] = pd.to_datetime(df['Ship Date'])
df['Days to Ship'] = (df['Ship Date'] - df['Order Date']).dt.days
df['Profit Ratio'] = df['Profit'] / df['Sales']

# Define the layout
layout = html.Div([
    html.H1("Data Analysis Dashboard"),
    dcc.DatePickerRange(
        id='date-picker-range',
        min_date_allowed=df['Order Date'].min(),
        max_date_allowed=df['Ship Date'].max(),
        start_date=df['Order Date'].min(),
        end_date=df['Ship Date'].max()
    ),
    dcc.Dropdown(
        id='granularity-dropdown',
        options=[
            {'label': 'Week', 'value': 'W'},
            {'label': 'Month', 'value': 'M'},
            {'label': 'Quarter', 'value': 'Q'},
            {'label': 'Year', 'value': 'Y'}
        ],
        value='M',  # Default to Month
        clearable=False
    ),
    html.Div(id='filtered-data-display'),
    dcc.Graph(id='data-graph')
])



@callback(
    Output('data-graph', 'figure'),
    [Input('date-picker-range', 'start_date'),
     Input('date-picker-range', 'end_date'),
     Input('granularity-dropdown', 'value')]
)
def update_graph(start_date, end_date, granularity):
    # Filter data based on the date range
    mask = (df['Order Date'] >= start_date) & (df['Ship Date'] <= end_date)
    filtered_df = df.loc[mask]

    # Set the index to Order Date for resampling
    filtered_df.set_index('Order Date', inplace=True)
    # Resample data based on selected granularity and calculate means for numeric columns
    aggregated_df = filtered_df.resample(granularity).agg({
        'Days to Ship': 'mean',
        'Discount': 'mean',
        'Profit': 'mean',
        'Profit Ratio': 'mean',
        'Quantity': 'mean',
        'Sales': 'mean'
    }).reset_index()

    # Create the timeline graph with multiple metrics
    fig = {
        'data': [
            {'x': aggregated_df['Order Date'], 'y': aggregated_df['Days to Ship'], 'type': 'line', 'name': 'Days to Ship'},
            {'x': aggregated_df['Order Date'], 'y': aggregated_df['Discount'], 'type': 'line', 'name': 'Discount'},
            {'x': aggregated_df['Order Date'], 'y': aggregated_df['Profit'], 'type': 'line', 'name': 'Profit'},
            {'x': aggregated_df['Order Date'], 'y': aggregated_df['Profit Ratio'], 'type': 'line', 'name': 'Profit Ratio'},
            {'x': aggregated_df['Order Date'], 'y': aggregated_df['Quantity'], 'type': 'line', 'name': 'Quantity'},
            {'x': aggregated_df['Order Date'], 'y': aggregated_df['Sales'], 'type': 'line', 'name': 'Sales'}
        ],
        'layout': {
            'title': 'Metrics Over Time',
            'height': 600,  # Increase the height of the graph
            'yaxis': {'title': 'Values', 'fixedrange': False}  # Allows for dynamic range on the y-axis
        }
    }

    return fig
