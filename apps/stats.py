import os
import dash
from dash import dcc, html, dash_table, callback, Input, Output
import dash_bootstrap_components as dbc
import pandas as pd
import glob  # Used to find files
from components.navbars import navbar
import os


dash.register_page(__name__, path='/stats', name="Stats", order=3)

csv_files = glob.glob('datasets/stats/*.csv')

# Label the dropdown options based on the CSV filenames
def format_label(filepath):
    """Takes a full file path and returns a formatted label."""
    base_name = os.path.basename(filepath)
    name_without_ext = os.path.splitext(base_name)[0]
    formatted_label = name_without_ext.replace('_', ' ').title()
    return formatted_label

dropdown_options = [{'label': format_label(f), 'value': f} for f in csv_files]

# Page Layout
layout = html.Div(
    className="glassmorphism-container",
    children=[
        navbar,
        html.Br(),
        html.Br(),
        dbc.Container([
            dbc.Row(
                dbc.Col(
                    [
                        html.H1("Team & Players Statistics", className="display-4 text-white text-center mt-4 mb-2"),
                        html.P(
                            "Explore the foundational datasets that power this dashboard's analytical tools.",
                            className="lead text-white-50 text-center mb-5",
                        ),
                    ]
                )
            ),
            # Card for the Dropdown Control
            dbc.Card(
                dbc.CardBody([
                    html.H5("Select a Dataset", className="card-title text-white"),
                    dcc.Dropdown(
                        id='csv-dropdown',
                        options=dropdown_options,
                        # Set a default value if files are found, otherwise None
                        value=dropdown_options[0]['value'] if dropdown_options else None,
                        clearable=False
                    )
                ]),
                className="glass-card mb-4",
                style={'zIndex': 10, 'position': 'relative'} # zIndex ensures dropdown menu is on top
            ),
            html.Div(id='table-container'),
        ])
    ]
)


# Callback to load and display the selected table
@callback(
    Output('table-container', 'children'),
    Input('csv-dropdown', 'value')
)
def update_table(selected_filename):
    if not selected_filename:
        return html.Div("Please select a file to view.", className="p-4 text-white")

    try:
        # Read the selected CSV file into a pandas DataFrame
        df = pd.read_csv(selected_filename)
        
        # Create the DataTable
        table = dash_table.DataTable(
            data=df.to_dict("records"),
            columns=[{"name": i, "id": i, "selectable": True} for i in df.columns],
            
            # Enables horizontal scrolling
            style_table={'overflowX': 'auto'},
            
            # Removes grid lines for a cleaner look 
            style_as_list_view=True,
            
            # Glassmorphism style
            style_cell={
                'padding': '10px',
                'backgroundColor': 'transparent',
                'color': 'white',
                'fontFamily': 'Montserrat, sans-serif'
            },
            style_header={
                'backgroundColor': 'rgba(255, 255, 255, 0.1)',
                'fontWeight': 'bold',
                'borderBottom': '1px solid rgba(255, 255, 255, 0.2)'
            },
            page_size=20,
            selected_columns=[],
        )
        return table
        
    except Exception as e:
        # Handle potential errors like a file not being found or unreadable
        return html.Div(f"Error loading file: {e}", className="p-4 text-danger")