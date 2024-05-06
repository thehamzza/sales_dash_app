# Super Store Sales Dash App
# Created by Muhammad Hamza Shakoor 


## Overview
This Dash application analyzes Superstore sales data. 
The dataset used for this project can be found in the "Sample - Superstore.xlsx" file.

link: 
https://datawonders.atlassian.net/wiki/spaces/TABLEAU/blog/2022/10/26/1953431553/Where+Can+I+Find+Superstore+Sales#Workbooks-and-Data-Sources

## Installation
To run this application, follow these steps:

1. Clone the repository or download the files.

2. Create a virtual Python environment, activate it, and install the required packages:
   
   ```bash
   python -m venv /path/to/new/virtual/environment
   
   source /path/to/new/virtual/environment/bin/activate
   
   pip3 install -r requirements.txt


#### NOTE: Run index.py file, because it's the main app file
    ```bash
      python3 index.py



## Overview

This Dash application serves as an interactive data analysis tool for sales data, providing insights through tables and graphical representations. It is designed to facilitate easy navigation, data manipulation, and in-depth analysis across various business metrics such as sales performance, profit ratios, and shipping efficiency.

### Navigation

The application consists of three main pages, each accessible via a top-level navigation bar with clear icons representing each page:

- **Home/Landing Page**: Provides a quick summary of key metrics and direct links to detailed views.
- **Table Page**: Offers a detailed tabular view of the sales data with interactive filtering and data entry capabilities.
- **Graph Page**: Displays dynamic charts that allow users to visualize data trends and relationships comprehensively.

### Page Details

#### Home/Landing Page

The landing page is designed to give a quick overview of the most critical data points, like accumulated sales or profit ratios. It features:
- Summary cards that show key data points.
- Navigation links to other pages with descriptive icons for intuitive access.

#### Table Page

This page features a comprehensive DataTable that showcases the sales data. Key functionalities include:
- **Filterable Data**: Users can filter data using dropdown menus that dynamically adjust available options based on previous selections.
- **Data Entry**: Below the table, users can add new data entries through input fields. An 'Add' button commits the new entries to the table, ensuring data integrity by avoiding duplicate entries for primary keys.

#### Graph Page

Designed for visual data exploration, this page includes:
- **Timeline Graph**: On the left, displaying trends over time for selected metrics like Sales, Returns, or Profit Ratio.
- **Bubble Chart**: On the right, which visualizes the relationships between two metrics with additional categorization controlled by user-selected dropdowns.
- **Data Controls**: At the top, users can filter data based on date ranges and choose data granularity (Week, Month, Quarter, Year) to refine their views.

### Interaction and Data Manipulation

Users can interact with the data in several ways:
- **Dropdown Menus**: Used for filtering data across the application to allow users to drill down into specific areas of interest.
- **Input Fields on the Table Page**: Enable the addition of new records directly into the dataset, reflecting immediately in the visualizations if applicable.
- **Graph Controls**: Users can select different data properties to display and explore data interactions dynamically in the graphs.

### Getting Started

To run the application:
1. Ensure you have Python and necessary packages (`dash`, `pandas`, `plotly`) installed.
2. Clone the repository and navigate to the app directory.
3. Run the command `python3 index.py` to start the server.
4. Open a web browser and go to `http://127.0.0.1:8050/` to access the app.


   ![Screenshot 2024-05-06 at 19-57-08 Superstores Dash App](https://github.com/thehamzza/sales_dash_app/assets/45312947/55ccf433-40dd-4c6b-b756-5159c523d930)

   ![Screenshot 2024-05-06 at 19-57-21 Superstores Dash App](https://github.com/thehamzza/sales_dash_app/assets/45312947/ab6b5d4e-09b2-46c0-abe6-59734fc5d177)

![Screenshot 2024-05-06 at 19-57-30 Superstores Dash App](https://github.com/thehamzza/sales_dash_app/assets/45312947/f1de92be-b0dc-4cfa-8c65-3a9846523e9f)

![Screenshot 2024-05-06 at 20-05-37 Superstores Dash App](https://github.com/thehamzza/sales_dash_app/assets/45312947/6488782f-01ab-4731-a879-0904f1970a7a)


