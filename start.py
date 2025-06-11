from dash import Dash, html
import dash
import dash_bootstrap_components as dbc

# Initialize the app and tell it to use pages.
# This file is the main "shell" and is NOT a page itself.
app = Dash(__name__, use_pages=True, pages_folder='apps', external_stylesheets=[dbc.themes.BOOTSTRAP])

# The layout for the entire app. It must include dash.page_container.
app.layout = html.Div([
    dash.page_container
])

if __name__ == '__main__':
    app.run(debug=True)