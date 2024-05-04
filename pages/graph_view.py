# import dash
# from dash import html, dcc, Input, Output, callback
# import pandas as pd
# from datetime import datetime as dt
# from data import data_loader as dl


# df = dl.load_data()
# #keeping this column name for simplicity
# date='Order Date'

# df[date] = pd.to_datetime(df[date])  # Ensure the date column is in datetime format



# print (df.head())
# print("i am here: ??>>>",df.head())



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
#         if 'value' in filtered_df.columns:  # Assuming 'value' is the column you want to sum
#             aggregated_df = filtered_df.resample(granularity).sum().reset_index()
#         else:
#             aggregated_df = filtered_df.resample(granularity).mean().reset_index()  # Assuming mean if 'value' is not present

#     # Display the filtered DataFrame (limited to 5 rows)
#     display_df = aggregated_df.head(5).to_dict('records')
#     display_columns = [{'name': col, 'id': col} for col in aggregated_df.columns]

#     # Prepare a simple line graph of the aggregated data
#     fig = {
#         'data': [{'x': aggregated_df[date], 'y': aggregated_df['value'], 'type': 'line'}],
#         'layout': {'title': 'Aggregated Data'}
#     }

#     return [dcc.Table(data=display_df, columns=display_columns), fig]
