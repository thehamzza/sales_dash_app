from dash import html, dcc, dash_table, callback, Input, Output, State
from dash.exceptions import PreventUpdate
import pandas as pd
import data_loader as dl


df = dl.load_data()


app.layout = html.Div([

    html.H1('Table View Page'),
    # Your DataTable and associated components would go here
    html.P('Welcome to the Table View Page!'),
    
        dcc.Dropdown(
            id='country-dropdown',
            options=[{'label': i, 'value': i} for i in sorted(df['Country/Region'].unique())],
            value=None,
            placeholder="Select a Country",
            clearable = True
        ),
        dcc.Dropdown(
            id='state-dropdown',
            options=[{'label': i, 'value': i} for i in df['State'].unique()],
            value=None,
            #disabled=True,  # Initially disabled until a country is selected
            placeholder="Select a State"
        ),
        dcc.Dropdown(
            id='city-dropdown',
            options=[{'label': i, 'value': i} for i in df['City'].unique()],
            value=None,
            #disabled=True,  # Initially disabled until a country is selected
            placeholder="Select a City"
        ),


        dash_table.DataTable(
            id='data-table',
            columns=[{"name": i, "id": i} for i in df.columns],
            data=df.to_dict('records'),
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
        html.Div(id='add-output')
    ])

# # Callbacks for dynamic dropdowns
# @callback(
#     Output('state-dropdown', 'options'),
#     Input('country-dropdown', 'value')
# )
# def set_states_options(selected_country):
#     if not selected_country:
#         return []
#     return [{'label': i, 'value': i} for i in df[df['Country'] == selected_country]['State'].unique()]

# @callback(
#     Output('city-dropdown', 'options'),
#     Input('state-dropdown', 'value'),
#     State('country-dropdown', 'value')
# )
# def set_cities_options(selected_state, selected_country):
#     if not selected_state or not selected_country:
#         return []
#     return [{'label': i, 'value': i} for i in df[(df['Country'] == selected_country) & (df['State'] == selected_state)]['City'].unique()]

# # Callback for adding data to the table
# @callback(
#     Output('data-table', 'data'),
#     Input('add-button', 'n_clicks'),
#     State('data-table', 'data'),
#     State('input-country', 'value'),
#     State('input-state', 'value'),
#     State('input-city', 'value'),
#     State('input-sales', 'value'),
#     State('input-profit', 'value')
# )
# def add_data_to_table(n_clicks, rows, country, state, city, sales, profit):
#     if n_clicks > 0:
#         if not all([country, state, city, sales, profit]):
#             raise PreventUpdate
#         new_row = {'Country': country, 'State': state, 'City': city, 'Sales': sales, 'Profit': profit}
#         if new_row not in rows:
#             rows.append(new_row)
#         return rows
#     raise PreventUpdate


@app.callback(
    Output('state-dropdown', 'options'),
    Input('country-dropdown', 'value')
)
def update_state_options(selected_country):
    if not selected_country:
        return []
    filtered_df = df[df['Country/Region'] == selected_country].dropna(subset=['State'])
    print ("filtered_df: ", filtered_df)
    states = [{'label': state, 'value': state} for state in sorted(filtered_df['State'].unique())]
    print ("states: ", states)
    return states



@callback(
    [Output('city-dropdown', 'options'),
     Output('city-dropdown', 'disabled')],
    [Input('state-dropdown', 'value')],
    [State('country-dropdown', 'value')]
)
def set_cities_options(selected_state, selected_country):
    if not selected_state or not selected_country:
        return [], True
    filtered_df = df[(df['Country/Region'] == selected_country) & (df['State'] == selected_state)]
    cities = [{'label': i, 'value': i} for i in filtered_df['City'].unique()]
    return cities, False


# Add a new callback here to filter the table based on dropdowns
@callback(
    Output('data-table', 'data'),
    [Input('country-dropdown', 'value'),
     Input('state-dropdown', 'value'),
     Input('city-dropdown', 'value')],
)
def filter_table(selected_country, selected_state, selected_city):
    # If no country is selected, display all data
    if not selected_country:
        return df.to_dict('records')
    # Filter by selected country
    filtered_df = df[df['Country/Region'] == selected_country]
    # Further filter by selected state if one is selected
    if selected_state:
        filtered_df = filtered_df[filtered_df['State'] == selected_state]
    # Further filter by selected city if one is selected
    if selected_city:
        filtered_df = filtered_df[filtered_df['City'] == selected_city]
    return filtered_df.to_dict('records')



def add_data_to_table(n_clicks, rows, input_country, input_state, input_city, input_sales, input_profit):
    if n_clicks > 0:
        if not all([input_country, input_state, input_city, input_sales, input_profit]):
            raise PreventUpdate
        # Here we check for duplicates. You need to define how you want to handle duplicates.
        # For example, you might use a combination of columns as a composite primary key.
        existing_ids = {(row['Country'], row['State'], row['City']) for row in rows}
        if (input_country, input_state, input_city) in existing_ids:
            raise PreventUpdate  # This prevents adding the new row if it's a duplicate
        new_row = {
            'Country/Region': input_country,
            'State': input_state,
            'City': input_city,
            'Sales': input_sales,
            'Profit': input_profit
        }
        rows.append(new_row)
        return rows
    return dash.no_update