import dash
from dash import dcc, html
import dash_bootstrap_components as dbc
from components.navbars import navbar

# Register the page
dash.register_page(__name__, path='/overview', name="Overview", order=1)

# Overview Text (Formatted for Markdown)
overview_text = """
This project, the **Laliga 2023/2024 Analytical Dashboard**, represents a comprehensive effort to transform raw sports data into an interactive, web-based platform for in-depth analysis. At its core, this dashboard is a testament to the power of data science in unraveling the intricate narratives of a football season, moving beyond simple scores and standings to explore the very fabric of team performance and match dynamics.

Built on a robust **Python** foundation, the dashboard leverages the **Flask** web framework as its backbone. The interactive user interface is powered by **Dash**, a framework specifically designed for creating analytical web applications. All the dynamic and engaging visualizations are generated using **Plotly**, which allows for a rich, user-driven exploration of the data. This technological stack was chosen to create a seamless and responsive experience, making complex data analysis accessible and intuitive.

The analysis is fueled by two comprehensive datasets: the **Laliga 23/24** match-by-match statistics and the **Spanish laliga full dataset for 23/24**. Together, these datasets provide a granular view of every single one of the 380 matches played, encompassing a wide array of metrics. This includes not only match outcomes but also detailed performance indicators such as shots, shots on target, fouls, corners, and disciplinary actions. This rich data source is the lifeblood of the dashboard, enabling a multi-faceted exploration of the season.  
  
  
### Project Goals and Objectives

The primary goal of this project is to create a centralized, web-based dashboard that serves as a one-stop solution for anyone looking to perform a deep-dive analysis of the 2023/2024 Laliga season. The key objectives to achieve this are:

* **Web-Based Accessibility:** To move away from static files and local scripts by creating a dashboard that is accessible via a web browser. This ensures that the analytical tools and insights are available to anyone, anywhere, without the need for complex setup or software installation.

* **Interactive Data Exploration:** To empower users to become active participants in the analysis. Instead of passive reports, the dashboard provides interactive components like **dropdown menus**, **tabs**, and **dynamic charts**. This allows users to filter data, select different metrics, and tailor the visualizations to their specific questions and curiosities.

* **Comprehensive Analysis:** To offer a holistic view of the season by providing a suite of analytical tools. The dashboard is designed to facilitate various types of analysis, including:

    * **Univariate Analysis:** Understanding the distribution of individual metrics like goals or shots.
    * **Categorical Analysis:** Breaking down data by categories, such as match results (Win/Loss/Draw).
    * **Comparative Analysis:** Comparing the performance of different teams across various statistical measures.
    * **Correlation Analysis:** Investigating the relationships between different variables to uncover underlying patterns.
    * **Trend Analysis:** To analyze the narrative of the season as it unfolds by aggregating and plotting key metrics over time. This includes viewing trends across **match rounds**, by **month**, or even by **day of the week** to identify temporal patterns.
    

* **Insight Generation:** To serve as a platform for discovery. By interacting with the data in a visual and intuitive way, users can identify trends, spot anomalies, and generate actionable insights that would be difficult to discern from raw data alone.

* **Visual Storytelling:** To use data visualization not just for presentation, but for telling a story. Each chart and graph is designed to answer a specific question and contribute to a larger narrative about the teams, their strategies, and the overall trajectory of the season.

### A Foundation for Analysis and Future Growth

**This project, in its current form, serves as a powerful proof-of-concept and an excellent starting point for anyone getting started with Dash. It provides a real-world blueprint for building sophisticated analytical tools, covering the entire workflow from loading and preparing data to structuring a multi-page application with complex, interactive callbacks and a cohesive visual theme.**

**However, this dashboard can be better, and it is designed to be a foundation for even more advanced features. The current platform can be extended in several key ways. Future enhancements could include the integration of predictive modeling to forecast match outcomes, the implementation of more advanced statistical analyses like team clustering based on playing style, or even connecting to a live API for real-time data updates during match days. As both a functional analytical tool and a launchpad for future development, this project demonstrates a scalable and compelling approach to data-driven storytelling in sports.**
"""

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
                        html.H1("Project Overview", className="display-4 text-white text-center mt-4 mb-2"),
                        html.P(
                            "An interactive portal for the analytical exploration of the 2023/2024 Laliga season.",
                            className="lead text-white-50 text-center mb-5",
                        ),
                    ]
                )
            ),
            dbc.Row(
                dbc.Col(
                    dbc.Card(
                        dbc.CardBody([
                            # Using dcc.Markdown to render the formatted text
                            html.H3("Welcome to the LaLiga 23/24 season analytical dashboard!", className="card-title text-white mb-4"),                            
                            dcc.Markdown(children=overview_text, className="text-white", id='overview-text'),
                        ]),
                        className="glass-card",
                    )
                )
            )
        ])
    ]
)