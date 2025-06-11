from dash import html, dash_table
import pandas as pd
import dash
import dash_bootstrap_components as dbc
from components.navbars import navbar


# Register the page
dash.register_page(__name__, path='/dataset', name="Dataset", order=1)

df = pd.read_csv("datasets/matches/preprocessed_laliga2324_matches.csv", index_col=0)

# Function to create a list item for each column's information
def column_info_item(column_name, description, data_type):
    return dbc.ListGroupItem([
        html.B(f"{column_name}: ", className="fs-6 me-2"),
        description,
        html.Span(f"({data_type})", className="text-success float-end")
    ])

# Page layout
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
                        html.H1("Dataset Structure", className="display-4 text-white text-center mt-4 mb-2"),
                        html.P(
                            "A detailed breakdown of the dataset used for the LaLiga 2023/24 season analysis.",
                            className="lead text-white-50 text-center mb-5",
                        ),
                    ]
                )
            ),

            dbc.Card(
                [
                    dbc.CardHeader(html.H4("Identifiers", className="m-0")),
                    dbc.CardBody(
                        dbc.ListGroup(
                            [
                                column_info_item("round", "Match round number (1 to 38)", "integer"),
                                column_info_item("home_team", "Name of the home team (e.g., 'Real Madrid', 'Barcelona')", "categorical"),
                                column_info_item("away_team", "Name of the away team", "categorical"),
                                column_info_item("utc_time", "Date and time of the match in UTC (e.g., '2023-08-11 17:30:00+00:00')", "datetime"),
                            ],
                            flush=True,
                        )
                    ),
                ],
                className="glass-card mb-4",
            ),

            dbc.Card(
                [
                    dbc.CardHeader(html.H4("Match Outcomes", className="m-0")),
                    dbc.CardBody(
                        dbc.ListGroup(
                            [
                                column_info_item("full_time_home_team_goals", "Goals scored by the home team at full time", "integer"),
                                column_info_item("full_time_away_team_goals", "Goals scored by the away team at full time", "integer"),
                                column_info_item("full_time_result", "Match result at full time ('H' for home win, 'A' for away win, 'D' for draw)", "categorical"),
                                column_info_item("half_time_home_team_goals", "Goals scored by the home team at half time", "integer"),
                                column_info_item("half_time_away_team_goals", "Goals scored by the away team at half time", "integer"),
                                column_info_item("half_time_result", "Match result at half time ('H' for home win, 'A' for away win, 'D' for draw)", "categorical"),
                            ],
                            flush=True,
                        )
                    ),
                ],
                className="glass-card mb-4",
            ),

            dbc.Card(
                [
                    dbc.CardHeader(html.H4("Performance Metrics", className="m-0")),
                    dbc.CardBody(
                        dbc.ListGroup(
                            [
                                column_info_item("home_team_shots", "Total shots by the home team", "integer"),
                                column_info_item("away_team_shots", "Total shots by the away team", "integer"),
                                column_info_item("home_team_shots_on_target", "Shots on target by the home team", "integer"),
                                column_info_item("away_team_shots_on_target", "Shots on target by the away team", "integer"),
                                column_info_item("home_team_fouls_committed", "Fouls committed by the home team", "integer"),
                                column_info_item("away_team_fouls_committed", "Fouls committed by the away team", "integer"),
                                column_info_item("home_team_corners", "Corners won by the home team", "integer"),
                                column_info_item("away_team_corners", "Corners won by the away team", "integer"),
                            ],
                            flush=True,
                        )
                    ),
                ],
                className="glass-card mb-4",
            ),

            dbc.Card(
                [
                    dbc.CardHeader(html.H4("Disciplinary Stats", className="m-0")),
                    dbc.CardBody(
                        dbc.ListGroup(
                            [
                                column_info_item("home_team_yellow_cards", "Yellow cards received by the home team", "integer"),
                                column_info_item("away_team_yellow_cards", "Yellow cards received by the away team", "integer"),
                                column_info_item("home_team_red_cards", "Red cards received by the home team", "integer"),
                                column_info_item("away_team_red_cards", "Red cards received by the away team", "integer"),
                            ],
                            flush=True,
                        )
                    ),
                ],
                className="glass-card mb-4",
            ),
            
                    
            html.Br(),
            
            dash_table.DataTable(
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
                    'fontFamily': 'Montserrat, sans-serif',
                },
                style_header={
                    'backgroundColor': 'rgba(255, 255, 255, 0.1)',
                    'fontWeight': 'bold',
                    'borderBottom': '1px solid rgba(255, 255, 255, 0.2)'
                },
                page_size=20,
                selected_columns=[],
            )
    ]),
    ]
)