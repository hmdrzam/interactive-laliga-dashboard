from dash import html, dcc
import dash


dash.register_page(__name__, path='/', name="Index", order=0)

# The layout for the home page
layout = html.Div([
    html.Div([
        html.Img(src='/assets/logo.png', className="mx-auto d-block", style={'height': '250px', 'marginBottom': '80px'}, id='logo'),
        html.H1("LaLiga 2023/24 Season Interactive Analytical Dashboard", className="display-4 text-center text-white fw-bold mb-4",
                id='land-text',
                style={'textShadow': '2px 2px 4px rgba(0,0,0,0.3)', 'fontSize': '33px'}),
        html.Hr(className="w-50 mx-auto border-light"),
        html.Div([
            dcc.Link("Overview", href="/overview", className="btn btn-outline-light m-2 custom-btn"),
            dcc.Link("Dataset", href="/dataset", className="btn btn-outline-light m-2 custom-btn"),
            dcc.Link("Stats", href="/stats", className="btn btn-outline-light m-2 custom-btn"),
            dcc.Link("Visualization", href="/visualization", className="btn btn-outline-light m-2 custom-btn"),
        ], className="text-center mb-5"),
    ], className="d-flex flex-column justify-content-center align-items-center vh-100 text-white", style={'background': 'linear-gradient(135deg, #1a2a6c, #b21f1f, #fdbb2d)'}),
])