import dash_bootstrap_components as dbc
from dash import dcc, html


navbar = dbc.NavbarSimple(
    children=[
        dbc.NavItem(dcc.Link("Overview", href="/overview", className="nav-link text-dark fw-bold")),
        dbc.NavItem(dcc.Link("Dataset", href="/dataset", className="nav-link text-dark fw-bold")),
        dbc.NavItem(dcc.Link("Stats", href="/stats", className="nav-link text-dark fw-bold")),
        dbc.NavItem(dcc.Link("Visualization", href="/visualization", className="nav-link text-dark fw-bold")),
    ],
    brand=html.Div([
        dcc.Link(
            dbc.Row([
                dbc.Col(html.Img(src="/assets/logo.png", height="60px")),
                dbc.Col(dbc.NavbarBrand("LaLiga Dashboard", className="ms-2 text-dark")),
            ], align="center", className="g-0"),
            href="/",
            style={"textDecoration": "none"},
        )
    ]),
    dark=False,
)