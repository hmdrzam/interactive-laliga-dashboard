import dash
from dash import dcc, html, callback, Input, Output
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px
from components.navbars import navbar

# Register the new page
dash.register_page(__name__, path='/visualization', name="Visualization", order=4)

# Load data
df = pd.read_csv("datasets/matches/preprocessed_laliga2324_matches.csv", index_col=0)

# Convert 'utc_time' to datetime format
df['utc_time'] = pd.to_datetime(df['utc_time'])


# Create 'day_of_week' column and set a chronological order for plotting
df['day_of_week'] = df['utc_time'].dt.day_name()
day_order = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
df['day_of_week'] = pd.Categorical(df['day_of_week'], categories=day_order, ordered=True)

# Create 'month' column and set a chronological order for plotting
df['month'] = df['utc_time'].dt.month
month_map = {1: 'Jan', 2: 'Feb', 3: 'Mar', 4: 'Apr', 5: 'May', 6: 'Jun', 
            7: 'Jul', 8: 'Aug', 9: 'Sep', 10: 'Oct', 11: 'Nov', 12: 'Dec'}
df['month_name'] = df['month'].map(month_map)
month_order = ['Aug', 'Sep', 'Oct', 'Nov', 'Dec', 'Jan', 'Feb', 'Mar', 'Apr', 'May']
df['month_name'] = pd.Categorical(df['month_name'], categories=month_order, ordered=True)
df.drop(columns=['month'], axis=1, inplace=True)
    

# Identify column types for dropdowns
numerical_cols = df.select_dtypes(include=['number']).columns.tolist()
categorical_cols = ['full_time_result', 'half_time_result', 'home_team', 'away_team']


# Helper function for graph styling
def style_figure(fig):
    """Applies the glassmorphism theme to a Plotly figure."""
    fig.update_layout(
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        title_font_color='white',
        xaxis_title_font_color='white',
        yaxis_title_font_color='white',
        xaxis=dict(tickfont=dict(color='white'), gridcolor='rgba(255, 255, 255, 0.2)'),
        yaxis=dict(tickfont=dict(color='white'), gridcolor='rgba(255, 255, 255, 0.2)'),
        font=dict(family="Montserrat, sans-serif"),
        legend_font_color='white',
        title_x=0.5, 
        title_font=dict(size=24, family="Arial")

    )
    return fig


corr_matrix = df[numerical_cols].corr()
# Create the heatmap figure using Plotly Express
fig_heatmap = px.imshow(
    corr_matrix,
    text_auto=True,  # Automatically display the correlation values on the cells
    aspect="auto",   # Adjust aspect ratio to fit the container
    title="Correlation Matrix of Numerical Metrics",
    color_continuous_scale=px.colors.diverging.RdBu_r # Use a red-blue color scale
)
style_figure(fig_heatmap)

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
                        html.H1("Dataset Plots", className="display-4 text-white text-center mt-4 mb-2"),
                        html.P(
                            "Generate dynamic charts to uncover patterns and trends within the season's data",
                            className="lead text-white-50 text-center mb-5",
                        ),
                    ]
                )
            ),
            dbc.Tabs(
                id="visualization-tabs",
                active_tab="tab-distribution",
                children=[
                    # Tab 1: Distribution Plot
                    dbc.Tab(label="Distribution", tab_id="tab-distribution", children=[
                        dbc.Card(
                            dbc.CardBody([
                                html.H5("Select a numerical column to see its distribution:", className="text-white"),
                                dcc.Dropdown(
                                    id='dist-column-dropdown',
                                    options=[{'label': col, 'value': col} for col in numerical_cols],
                                    value=numerical_cols[0] if numerical_cols else None
                                ),
                                dcc.Graph(id='distribution-graph', figure={})
                            ]), className="glass-card mt-4"
                        )
                    ]),
                    
                    # Tab 2: Categorical Plot
                    dbc.Tab(label="Categorical", tab_id="tab-categorical", children=[
                        dbc.Card(
                            dbc.CardBody([
                                html.H5("Select a categorical column to see its breakdown:", className="text-white"),
                                dcc.Dropdown(
                                    id='cat-column-dropdown',
                                    options=[{'label': col, 'value': col} for col in categorical_cols],
                                    value=categorical_cols[0] if categorical_cols else None
                                ),
                                dcc.Graph(id='pie-chart-graph', figure={})
                            ]), className="glass-card mt-4"
                        )
                    ]),
                    
                    # Tab 3: Box Plot
                    dbc.Tab(label="Comparison (Box Plot)", tab_id="tab-bivariate", children=[
                        dbc.Card(
                            dbc.CardBody([
                                dbc.Row([
                                    dbc.Col([
                                        html.H5("Select Numerical Column (Y-axis):", className="text-white"),
                                        dcc.Dropdown(
                                            id='box-numerical-dropdown',
                                            options=[{'label': col, 'value': col} for col in numerical_cols],
                                            value=numerical_cols[0] if numerical_cols else None
                                        ),
                                    ], width=6),
                                    dbc.Col([
                                        html.H5("Select Categorical Column (X-axis):", className="text-white"),
                                        dcc.Dropdown(
                                            id='box-categorical-dropdown',
                                            options=[{'label': col, 'value': col} for col in categorical_cols],
                                            value=categorical_cols[0] if categorical_cols else None
                                        ),
                                    ], width=6)
                                ]),
                                dcc.Graph(id='box-plot-graph', figure={})
                            ]), className="glass-card mt-4"
                        )
                    ]),
                    
                    # Tab 4: Scatter Plot
                    dbc.Tab(label="Correlation (Scatter Plot)", tab_id="tab-scatter", children=[
                        dbc.Card(
                            dbc.CardBody([
                                dbc.Row([
                                    dbc.Col([
                                        html.H5("Select X-Axis (Numerical):", className="text-white"),
                                        dcc.Dropdown(
                                            id='scatter-x-dropdown',
                                            options=[{'label': col, 'value': col} for col in numerical_cols],
                                            value=numerical_cols[0] if numerical_cols else None
                                        ),
                                    ], width=6),
                                    dbc.Col([
                                        html.H5("Select Y-Axis (Numerical):", className="text-white"),
                                        dcc.Dropdown(
                                            id='scatter-y-dropdown',
                                            options=[{'label': col, 'value': col} for col in numerical_cols],
                                            value=numerical_cols[1] if len(numerical_cols) > 1 else None
                                        ),
                                    ], width=6)
                                ]),
                                dcc.Graph(id='scatter-plot-graph', figure={})
                            ]), className="glass-card mt-4"
                        )
                    ]),
                    
                    # Tab 5: Correlation Heatmap
                    dbc.Tab(label="Correlation Heatmap", tab_id="tab-heatmap", children=[
                        dbc.Card(
                            dbc.CardBody([
                                html.H5("Correlation Matrix of All Numerical Variables", className="text-white"),
                                html.P("This heatmap shows the Pearson correlation coefficient between pairs of numerical columns. A value of 1 indicates a perfect positive correlation, -1 indicates a perfect negative correlation, and 0 indicates no linear correlation.", className="text-white-50"),
                                dcc.Graph(
                                    id='correlation-heatmap-graph',
                                    figure=fig_heatmap # Pass the pre-generated figure here
                                )
                            ]), className="glass-card mt-4"
                        )
                    ]),
                
                    # Tab 6: Time Series Analysis
                    dbc.Tab(label="Trend Analysis", tab_id="tab-advanced-trends", children=[
                        dbc.Card(
                            dbc.CardBody([
                                dbc.Row([
                                    dbc.Col([
                                        html.H5("Select Metric to Analyze:", className="text-white"),
                                        dcc.Dropdown(
                                            id='adv-metric-dropdown', 
                                            options=[{'label': col, 'value': col} for col in numerical_cols if col != 'round'],
                                            value='full_time_home_team_goals',  # Default value
                                            clearable=False
                                        ),
                                    ], width=6),
                                    dbc.Col([
                                        html.H5("Group Trend By:", className="text-white"),
                                        dcc.Dropdown(
                                            id='adv-group-by-dropdown',
                                            options=[
                                                {'label': 'Match Round', 'value': 'round'},
                                                {'label': 'Day of the Week', 'value': 'day_of_week'},
                                                {'label': 'Month', 'value': 'month_name'},
                                            ],
                                            value='round',
                                            clearable=False
                                        ),
                                    ], width=6)
                                ]),
                                dcc.Graph(id='advanced-trends-graph', figure={})
                            ]), className="glass-card mt-4"
                        )
                    ]),
                ]
            )
        ])
    ]
)


# Callbacks

# Callback for Distribution Tab
@callback(
    Output('distribution-graph', 'figure'),
    Input('dist-column-dropdown', 'value')
)
def update_distribution(selected_col):
    if not selected_col:
        return {}
    fig = px.histogram(df, x=selected_col, title=f"Distribution of {selected_col}", nbins=38)
    fig.update_layout(title_x=0.5, title_font=dict(size=24, family="Arial"))
    return style_figure(fig)

# Callback for Categorical Tab
@callback(
    Output('pie-chart-graph', 'figure'),
    Input('cat-column-dropdown', 'value')
)
def update_pie_chart(selected_col):
    if not selected_col:
        return {}
    counts = df[selected_col].value_counts()
    fig = px.pie(
        values=counts.values,
        names=counts.index,
        title=f"Breakdown of {selected_col}",
        hole=0.3
    )
    fig.update_layout(title_x=0.5, title_font=dict(size=24, family="Arial"))
    return style_figure(fig)

# Callback for Box Plot Tab
@callback(
    Output('box-plot-graph', 'figure'),
    Input('box-numerical-dropdown', 'value'),
    Input('box-categorical-dropdown', 'value')
)
def update_box_plot(numerical_col, categorical_col):
    if not numerical_col or not categorical_col:
        return {}
    fig = px.box(df, x=categorical_col, y=numerical_col, title=f"{numerical_col} by {categorical_col}")
    fig.update_layout(title_x=0.5, title_font=dict(size=24, family="Arial"))
    return style_figure(fig)

# Callback for Scatter Plot Tab
@callback(
    Output('scatter-plot-graph', 'figure'),
    Input('scatter-x-dropdown', 'value'),
    Input('scatter-y-dropdown', 'value')
)
def update_scatter_plot(x_col, y_col):
    if not x_col or not y_col:
        return {}
    fig = px.scatter(
        df,
        x=x_col,
        y=y_col,
        title=f"Correlation between {x_col} and {y_col}",
        trendline="ols",  # Adds an Ordinary Least Squares regression trendline
        trendline_color_override="yellow"
    )
    fig.update_layout(title_x=0.5, title_font=dict(size=24, family="Arial"))

    return style_figure(fig)

# Callback for Time Series Analysis Tab
@callback(
    Output('advanced-trends-graph', 'figure'),
    Input('adv-metric-dropdown', 'value'), 
    Input('adv-group-by-dropdown', 'value')
)
def update_advanced_trends(selected_metric, group_by_col):
    if not selected_metric or not group_by_col:
        return {}

    # Group data by the selected dimension and calculate the average
    dff_grouped = df.groupby(group_by_col, observed=True)[selected_metric].mean().reset_index()

    # correct sorting for categorical time dimensions
    if group_by_col in ['day_of_week', 'month_name']:
        dff_grouped = dff_grouped.sort_values(group_by_col)

    # Create a dynamic title
    y_axis_label = f"Average {selected_metric.replace('_', ' ').title()}"
    x_axis_label = group_by_col.replace('_', ' ').title()

    fig = px.line(
        dff_grouped,
        x=group_by_col,
        y=selected_metric,
        title=f"Trend of {y_axis_label} by {x_axis_label}",
        labels={group_by_col: x_axis_label, selected_metric: y_axis_label},
        markers=True
    )
    
    # Apply the standard glassmorphism styling
    return style_figure(fig)