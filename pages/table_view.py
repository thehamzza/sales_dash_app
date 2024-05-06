import dash
from dash import html, dcc, dash_table, callback, Input, Output, State
from dash.exceptions import PreventUpdate
import pandas as pd
from data import data_loader as dl


data = dl.load_data()

def select_columns(dataframe, column_names):
    """
    Select specific columns from a DataFrame and return a new DataFrame.

    Parameters:
    - dataframe: pd.DataFrame from which to select columns.
    - column_names: list of str, the names of the columns to select.

    Returns:
    - pd.DataFrame containing only the specified columns.
    """
    # Ensure that all specified columns exist in the DataFrame
    columns_to_select = [column for column in column_names if column in dataframe.columns]
    
    # If any of the requested columns are missing, print a message
    missing_columns = set(column_names) - set(columns_to_select)
    if missing_columns:
        print(f"Warning: The following columns were not found in the DataFrame: {missing_columns}")

    # Select and return the new DataFrame with only the specified columns
    return dataframe[columns_to_select]

# Example usage:
#print(data.head())  # Print the first few rows of the old DataFrame to verify

df = data #full data
selected_columns = ['Row ID', 'Country/Region', 'State', 
                    'City', 'Region', 'Product Name','Category', 'Sub-Category',
                      'Sales','Quantity', 'Profit']  # Specify your desired columns

new_df = select_columns(df, selected_columns)
#print(new_df.head())  # Print the first few rows of the new DataFrame to verify

data = new_df

# App layout
layout = html.Div([
    html.H1("Data Table with Filters"),
    html.Div([
        dcc.Dropdown(
            id='country-dropdown',
            options=[{'label': country, 'value': country} for country in data['Country/Region'].unique()],
            value=None,
            placeholder='Select a country',
            className='dropdown'
        ),
        dcc.Dropdown(
            id='state-dropdown',
            options=[],
            value=None,
            placeholder='Select a state',
            className='dropdown'
        ),
        dcc.Dropdown(
            id='city-dropdown',
            options=[],
            value=None,
            placeholder='Select a city',
            disabled=True,
            className='dropdown'
        ),
    
        dash_table.DataTable(
            id='data-table',
            columns=[{"name": i, "id": i} for i in data.columns],
            data=data.to_dict('records'),
            filter_action='native',
            sort_action='native',
            page_size=10,
            editable=False,
       
        ),
        
    html.Div([
        dcc.Input(id='input-product-name', type='text', placeholder='Product Name', style={'marginRight': '10px'}),
        dcc.Input(id='input-category', type='text', placeholder='Category', style={'marginRight': '10px'}),
        dcc.Input(id='input-sub-category', type='text', placeholder='Sub-Category', style={'marginRight': '10px'}),
        dcc.Input(id='input-sales', type='number', placeholder='Sales', style={'marginRight': '10px'}),
        dcc.Input(id='input-quantity', type='number', placeholder='Quantity', style={'marginRight': '10px'}),
        dcc.Input(id='input-profit', type='number', placeholder='Profit', style={'marginRight': '10px'}),
        html.Button('Add Entry', id='add-entry-button', n_clicks=0,
                     style={
                        'backgroundColor': '#001b75',  # Bootstrap primary blue
                        'color': 'white',  # Text color
                        'border': 'none',
                        'padding': '10px 20px',  # Padding inside the button, vertical and horizontal
                        'fontSize': '16px',  # Text size
                        'borderRadius': '5px',  # Rounded corners
                        'cursor': 'pointer',  # Cursor indicates the element is clickable
                        'transition': 'background-color 0.3s',  # Smooth transition for hover effect
                          })
        ], 
        style={'display': 'flex', 'flexDirection': 'row', 'padding': '10px'}),

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
    Output('data-table', 'data', allow_duplicate=True),
    [Input('country-dropdown', 'value'),
     Input('state-dropdown', 'value'),
     Input('city-dropdown', 'value')],
     prevent_initial_call='initial_duplicate'
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


#------ new code  -----

# Callback to add new data to the table
# keeps country , state and city the same as before, rest entries NAN
@callback(
    Output('data-table', 'data', allow_duplicate=True),
    [Input('add-entry-button', 'n_clicks')],
    [State('data-table', 'data'),
     State('country-dropdown', 'value'),
     State('state-dropdown', 'value'),
     State('city-dropdown', 'value'),
     State('input-product-name', 'value'),
     State('input-category', 'value'),
     State('input-sub-category', 'value'),
     State('input-sales', 'value'),
     State('input-quantity', 'value'),
     State('input-profit', 'value')],
     prevent_initial_call='initial_duplicate'
)
def add_data(n_clicks, rows, country, state, city, product_name, category, sub_category, sales, quantity, profit):
    if n_clicks > 0:
        # Create a new row with the selected and inputted values
        new_row = {
            'Country/Region': country,
            'State': state,
            'City': city,
            'Product Name': product_name,
            'Category': category,
            'Sub-Category': sub_category,
            'Sales': sales,
            'Quantity': quantity,
            'Profit': profit
        }
        
        # Fill other columns with NaN if they exist in the dataframe
        all_columns = set(rows[0].keys())  # Get all column names from current data
        for col in all_columns:
            if col not in new_row:
                new_row[col] = pd.NA  # Using pandas NA for correct handling of missing data
        
        # Append to the existing data
        rows.append(new_row)
        return rows

    # If no clicks, do not update
    return dash.no_update
