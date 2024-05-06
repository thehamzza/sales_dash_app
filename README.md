# Super Store Sales Dash App
# Created by Muhammad Hamza Shakoor 


## Overview
This Dash application analyzes Superstore sales data. 
The dataset used for this project can be found in the "Sample - Superstore.xlsx" file.
link: https://datawonders.atlassian.net/wiki/spaces/TABLEAU/blog/2022/10/26/1953431553/Where+Can+I+Find+Superstore+Sales#Workbooks-and-Data-Sources

## Installation
To run this application, follow these steps:

1. Clone the repository or download the files.

2. Create a virtual Python environment:
   ```bash
   python -m venv /path/to/new/virtual/environment

Activate the virtual environment:
```bash
source /path/to/new/virtual/environment/bin/activate

Install the required packages:
```bash
pip3 install -r requirements.txt

## OVER VIEW

### Page 1: Home/ Landing Page

Upon entering the base URL (Localhost) of the app, the user is redirected to the landing page. This page provides an overview of the most recent data (e.g., accumulated Sales or Profit Ratio) and two cards that link to the other pages. Inspiration for this page can be drawn from the Super Sample Superstore Dashboard -> Descriptive View.

### Page 2: Table Page

At the beginning of the page, there is a Dash DataTable containing the sales data described in the introduction. The table is filterable by three dropdowns with properties of your choice. Optionally, include dropdowns that form a hierarchy and interact with each other (e.g., excluding an option if the first dropdown is filled). At the bottom of the page, there are five input fields with properties of your choice and an "Add" button. Clicking "Add" adds the entry to the table above. One of the input fields should serve as a primary key. Optionally, prevent adding duplicated entries.

### Page 3: Graph Page

On the left side of the page, there is a fitting timeline graph for properties such as Days to Ship, Discount, Profit, Profit Ratio, Quantity, Returns, and Sales. On the right side of the page, there is a Bubble chart. Next to the Bubble chart, include two-axis dropdowns containing the properties mentioned earlier. Selecting one dropdown excludes the option in the other. The dropdowns set the values for the Bubble chart. Add a third dropdown that breaks down the bubble chart and contains properties such as Segment, Ship Mode, Customer Name, Category, Sub-Category, and Product Name. At the top of the page, include a date filter and a granularity dropdown (Week, Month, Quarter, Year). Add a sidebar, which navigates to the three pages and has icons per next to the page title.
