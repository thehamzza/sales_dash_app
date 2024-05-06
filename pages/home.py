from dash import html, dcc
from data import data_loader as dl


# Function to calculate some metrics to display
def calculate_metrics(df):
    total_sales = df['Sales'].sum()
    total_profit = df['Profit'].sum()
    profit_ratio = df['Profit'].sum() / total_sales
    df['Returns'] = df['Profit'].apply(lambda x: abs(x) if x < 0 else 0) #negative profit
    total_returns = df['Returns'].sum()
    loss_ratio = df['Returns'].sum() / total_sales
    return total_sales, total_profit, profit_ratio,total_returns, loss_ratio

# Load your data
df = dl.load_data()
total_sales, total_profit, profit_ratio,total_returns, loss_ratio = calculate_metrics(df)



# Define the layout for the home page
layout = html.Div([
    
    html.H1("Welcome to the Superstore Sales Dashboard", style={'textAlign': 'center'}),
    html.Div([
        html.Div([
            html.H3(f"Total Sales: ${total_sales:,.2f}"),
            html.H3(f"Total Profit: ${total_profit:,.2f}"),
            html.H3(f"Total Returns: ${total_returns:,.2f}"),
            html.H3(f"Profit Ratio: {profit_ratio:.2%}"),
            html.H3(f"Loss Ratio: ${loss_ratio:.2%}")
        ], className="cards"),
    ]),
    

    html.Div([
                # Container for cards
                html.Div([
                    dcc.Link(
                        html.Div([
                            html.H3("View Detailed Tables"),
                            html.P("Click here to view detailed sales and profit tables."),
                        ], className="cards"), 
                        href='/table'
                    ),
                    dcc.Link(
                        html.Div([
                            html.H3("View Graphs"),
                            html.P("Click here to explore various sales and profit graphs."),
                        ], className="cards"),  
                        href='/graph'
                    ),
                ], style={'display': 'flex', 'margin': 'auto','maxWidth': '1000px', 'justifyContent': 'space-between', 'alignItems': 'center'})
            ]),

    html.Div([
        dcc.Graph(
            id='sales-overview',
            figure={
                'data': [{'x': df['Order Date'], 'y': df['Sales'], 'type': 'bar'}],
                
                'layout':{
                'title':'Total Sales Over Time',
                'xaxis':{
                    'title':'Time'
                },
                'yaxis':{
                    'title':'No. of Sales'
                }
                }
            }
        )
    ], className="home-graph"),

    html.Div([
        dcc.Graph(
            id='profit-overview',
            figure={
                'data': [{'x': df['Order Date'], 'y': df['Profit'], 'type': 'bar', 'name': 'Profit'}],
                'layout': {
                    'title': 'Total Profit Over Time',
                    'xaxis': {
                        'title': 'Time'
                    },
                    'yaxis': {
                        'title': 'Profit'
                    }
                }
            }
        )
    ], className="home-graph"),

])
