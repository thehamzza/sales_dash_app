import dash
from dash import html, dcc, dash_table, callback, Input, Output, State
from dash.exceptions import PreventUpdate
import pandas as pd
from data import data_loader as dl


data = dl.load_data()

# App layout
layout = html.Div([
    html.H1("Data Table with Filters"),
    html.Div([
        dcc.Dropdown(
            id='country-dropdown',
            options=[{'label': country, 'value': country} for country in data['Country/Region'].unique()],
            value=None,
            placeholder='Select a country'
        ),
        dcc.Dropdown(
            id='state-dropdown',
            options=[],
            value=None,
            placeholder='Select a state'
        ),
        dcc.Dropdown(
            id='city-dropdown',
            options=[],
            value=None,
            placeholder='Select a city',
            disabled=True
        ),
    
        dash_table.DataTable(
            id='data-table',
            columns=[{"name": i, "id": i} for i in data.columns],
            data=data.to_dict('records'),
            filter_action='native',
            sort_action='native',
            page_size=10,
            editable=False
        ),
        html.Div([
            dcc.Input(id='input-country', type='text', placeholder='Country'),
            dcc.Input(id='input-state', type='text', placeholder='State'),
            dcc.Input(id='input-city', type='text', placeholder='City'),
            dcc.Input(id='input-sales', type='number', placeholder='Sales'),
            dcc.Input(id='input-profit', type='number', placeholder='Profit'),
            html.Button('Add', id='add-button', n_clicks=0)
        ]),
    ]),
    html.Div(id='table-container')
])





# Callback to update state dropdown options based on selected country
@callback(
    Output('state-dropdown', 'options'),
    [Input('country-dropdown', 'value')]
)
def update_state_dropdown(selected_country):
    if selected_country is None:
        return []
    else:
        states = data[data['Country/Region'] == selected_country]['State'].unique()
        return [{'label': state, 'value': state} for state in states]
    

@callback(
    Output('city-dropdown', 'disabled'),
    [Input('state-dropdown', 'value')]
)
def update_city_dropdown_disabled(selected_state):
    return selected_state is None

# Callback to update city dropdown options based on selected state
@callback(
    Output('city-dropdown', 'options'),
    [Input('state-dropdown', 'value')]
)
def update_city_dropdown(selected_state):
    if selected_state is None:
        return []
    else:
        cities = data[data['State'] == selected_state]['City'].unique()
        return [{'label': city, 'value': city} for city in cities]

# Callback to update table based on selected filters
@callback(
    Output('data-table', 'data'),
    [Input('country-dropdown', 'value'),
     Input('state-dropdown', 'value'),
     Input('city-dropdown', 'value')]
)
def update_table(selected_country, selected_state, selected_city):
    filtered_data = data

    if selected_country is not None:
        filtered_data = filtered_data[filtered_data['Country/Region'] == selected_country]

    if selected_state is not None:
        filtered_data = filtered_data[filtered_data['State'] == selected_state]

    if selected_city is not None:
        filtered_data = filtered_data[filtered_data['City'] == selected_city]

    return filtered_data.to_dict('records')





# # Callback to add data to the table
# @callback(
#     Output('data-table', 'data'),
#     [Input('add-button', 'n_clicks')],
#     [State('data-table', 'data'),
#      State('input-country', 'value'),
#      State('input-state', 'value'),
#      State('input-city', 'value'),
#      State('input-sales', 'value'),
#      State('input-profit', 'value')]
# )
# def add_data_to_table(n_clicks, rows, input_country, input_state, input_city, input_sales, input_profit):
#     if n_clicks > 0:
#         if not all([input_country, input_state, input_city, input_sales, input_profit]):
#             raise PreventUpdate
#         # Here we check for duplicates. You need to define how you want to handle duplicates.
#         # For example, you might use a combination of columns as a composite primary key.
#         existing_ids = {(row['Country/Region'], row['State'], row['City']) for row in rows}
#         if (input_country, input_state, input_city) in existing_ids:
#             raise PreventUpdate  # This prevents adding the new row if it's a duplicate
#         new_row = {
#             'Country/Region': input_country,
#             'State': input_state,
#             'City': input_city,
#             'Sales': input_sales,
#             'Profit': input_profit
#         }
#         rows.append(new_row)
#         return rows
#     return dash.no_update

