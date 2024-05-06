import dash
from dash import html, dcc, Input, Output, callback
from dash import dash_table
import pandas as pd
from datetime import datetime as dt
from data import data_loader as dl

import plotly.graph_objs as go

df = dl.load_data()

# Convert dates to datetime and calculate Days to Ship
df['Order Date'  ] = pd.to_datetime(df['Order Date'])
df['Ship Date'   ] = pd.to_datetime(df['Ship Date'])
df['Days to Ship'] = (df['Ship Date'] - df['Order Date']).dt.days
df['Profit Ratio'] = df['Profit'] / df['Sales']

# TODO calculate these columns as well

# Calculate Returns based on negative profit assumption
df['Returns'] = df['Profit'].apply(lambda x: abs(x) if x < 0 else 0)


# Define the layout
layout = html.Div([
    html.H1("Graph Analysis Page"),
    dcc.DatePickerRange(
        id='date-picker-range',
        min_date_allowed=df['Order Date'].min(),
        max_date_allowed=df['Ship Date'].max(),
        start_date=df['Order Date'].min(),
        end_date=df['Ship Date'].max(),
        #className='date-picker'
        className='dropdown' #for css
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
        clearable=False,
        className='dropdown'
    ),
    html.Div(id='filtered-data-display'),
    dcc.Graph(id='data-graph'),

    html.Div(
        id= 'bubble-chart',
        children= [
            dcc.Dropdown(
                id='bubble-dropdown-1',
                value='Days to Ship',
                clearable=False,
                options= [
                    {'label': 'Days to Ship', 'value': 'Days to Ship',},
                    {'label': 'Discount'    , 'value': 'Discount'    ,},
                    {'label': 'Profit'      , 'value': 'Profit'      ,},
                    {'label': 'Profit Ratio', 'value': 'Profit Ratio',},
                    {'label': 'Quantity'    , 'value': 'Quantity'    ,},
                    {'label': 'Returns'     , 'value': 'Returns'     ,},
                    {'label': 'Sales'       , 'value': 'Sales'       ,},
                ],
                className='dropdown'
            ),
            dcc.Dropdown(
                id='bubble-dropdown-2',
                value='Discount',
                clearable=False,
                options= [
                    {'label': 'Days to Ship', 'value': 'Days to Ship',},
                    {'label': 'Discount'    , 'value': 'Discount'    ,},
                    {'label': 'Profit'      , 'value': 'Profit'      ,},
                    {'label': 'Profit Ratio', 'value': 'Profit Ratio',},
                    {'label': 'Quantity'    , 'value': 'Quantity'    ,},
                    {'label': 'Returns'     , 'value': 'Returns'     ,},
                    {'label': 'Sales'       , 'value': 'Sales'       ,},
                ],
                className='dropdown'
            ),
            dcc.Dropdown(
                id='bubble-dropdown-3',
                value='Segment',
                clearable=False,
                options= [
                    {'label': 'Segment'      , 'value': 'Segment'      ,},
                    {'label': 'Ship Mode'    , 'value': 'Ship Mode'    ,},
                    {'label': 'Customer Name', 'value': 'Customer Name',},
                    {'label': 'Category'     , 'value': 'Category'     ,},
                    {'label': 'Sub-Category' , 'value': 'Sub-Category' ,},
                    {'label': 'Product Name' , 'value': 'Product Name' ,},
                ],
                className='dropdown'
            ),
            
            dcc.Graph(
                id= 'bubble-chart-graph'
            )
        ]
    ),
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

@callback(
        [Output('bubble-dropdown-1', 'options'),
         Output('bubble-dropdown-2', 'options')],
        [Input('bubble-dropdown-1', 'value'),
         Input('bubble-dropdown-2', 'value')]
)
def update_bubble_dropdowns(drop_down_1_value, drop_down_2_value):
    options = [
        {'label': 'Days to Ship', 'value': 'Days to Ship',},
        {'label': 'Discount'    , 'value': 'Discount'    ,},
        {'label': 'Profit'      , 'value': 'Profit'      ,},
        {'label': 'Profit Ratio', 'value': 'Profit Ratio',},
        {'label': 'Quantity'    , 'value': 'Quantity'    ,},
        {'label': 'Returns'     , 'value': 'Returns'     ,},
        {'label': 'Sales'       , 'value': 'Sales'       ,},
    ]
    return (
        [option for option in options if option['value'] != drop_down_2_value],
        [option for option in options if option['value'] != drop_down_1_value]
    )


@callback(
        Output('bubble-chart-graph', 'figure'),
        [Input('bubble-dropdown-1', 'value'),
         Input('bubble-dropdown-2', 'value'),
         Input('bubble-dropdown-3', 'value')]
)
def update_bubble_chart(drop_down_1_value, drop_down_2_value, drop_down_3_value):
    global df
    df2 = ( df
        .groupby(drop_down_3_value)
        .apply(lambda df: df.select_dtypes(include= 'number').sum())
    )
    scaledProfits = (df2['Profit'] - df2['Profit'].min()) / df2['Profit'].max() * 100 + 10
    
    fig = go.Figure()
    fig.add_trace(
        go.Scatter(
            x     = df2[drop_down_1_value],
            y     = df2[drop_down_2_value],
            text  = df2.index,
            mode  = 'markers',
            marker= dict(                
                size      = scaledProfits,
                color     = scaledProfits,
                colorscale= 'Viridis',
                showscale = True
            ),
            hoverinfo='text+x+y',
            hovertemplate=(
                "<b>%{text}</b><br>" +
                drop_down_1_value + ": %{x}<br>" +  # Correct use of variables within hovertemplate
                drop_down_2_value + ": %{y}<br>" +
                "Scaled Profit: %{marker.size}<extra></extra>"  
        )
    )
    )
    fig.update_layout(
        title= 'Bubble Chart',
        xaxis= dict(title=drop_down_1_value),
        yaxis= dict(title=drop_down_2_value)
    )
    return fig