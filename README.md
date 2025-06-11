# 📊 Laliga 2023/2024 Analytical Dashboard

An interactive web dashboard built with Python, Dash, and Plotly for the in-depth analysis of the 2023/2024 Spanish Laliga season.

---

### 📖 About The Project

This project, the **Laliga 2023/2024 Analytical Dashboard**, represents a comprehensive effort to transform raw sports data into an interactive, web-based platform for in-depth analysis. At its core, this dashboard is a testament to the power of data science in unraveling the intricate narratives of a football season, moving beyond simple scores and standings to explore the very fabric of team performance and match dynamics.

Built on a robust **Python** foundation, the dashboard leverages the **Flask** web framework as its backbone. The interactive user interface is powered by **Dash**, a framework specifically designed for creating analytical web applications. All the dynamic and engaging visualizations are generated using **Plotly**, which allows for a rich, user-driven exploration of the data. This technological stack was chosen to create a seamless and responsive experience, making complex data analysis accessible and intuitive.

The analysis is fueled by two comprehensive datasets: the **Laliga 23/24** match-by-match statistics and the **Spanish laliga full dataset for 23/24**. Together, these datasets provide a granular view of every single one of the 380 matches played, encompassing a wide array of metrics. This includes not only match outcomes but also detailed performance indicators such as shots, shots on target, fouls, corners, and disciplinary actions. This rich data source is the lifeblood of the dashboard, enabling a multi-faceted exploration of the season.

---

### ✨ Key Features

* **Multi-Page Application:** A clean and organized multi-page layout for different sections: Overview, Dataset Details, Interactive Tables, and Visualizations.
* **Interactive Visualizations:** A dedicated visualizer with multiple tabs for different types of analysis:
    * **Distribution Analysis:** Explore the spread of any numerical metric with interactive histograms.
    * **Categorical Analysis:** Visualize the breakdown of categorical data (like match results) with pie charts.
    * **Comparative Analysis:** Compare team performance using insightful box plots.
    * **Correlation Analysis:** Investigate relationships between two metrics using scatter plots with regression trendlines.
    * **Correlation Heatmap:** Get a high-level overview of how all numerical variables relate to each other.
    * **Trend Analysis:** Track key statistics as the season progresses by match round, month, or day of the week.
* **Interactive Data Tables:** View, sort, and filter the raw datasets directly within the application.
* **Themed UI:** A custom "glassmorphism" theme applied consistently across all pages and components for a modern and professional look.

---

### 🛠️ Built With

This project is powered by the following key technologies and libraries:

* **Python**
* **Dash** - The core framework for building the web application.
* **Plotly** - For creating interactive charts and graphs.
* **Pandas** - For all data manipulation and analysis.
* **Dash Bootstrap Components** - For responsive layouts and modern UI components.
* **Flask** - As the underlying web server for Dash.

---

### 🚀 Getting Started

To get a local copy up and running, follow these simple steps.

#### Prerequisites

Make sure you have Python (3.8+) and pip installed on your system.

#### Installation

1.  **Clone the repository:**
    ```sh
    git clone [https://github.com/hmdrzam/interactive-laliga-dashboard.git](https://github.com/hmdrzam/interactive-laliga-dashboard.git)
    ```

2.  **Navigate to the project directory:**
    ```sh
    cd your_repository_name
    ```

3.  **Create and activate a virtual environment (recommended):**
    * **For Windows:**
        ```sh
        python -m venv venv
        .\venv\Scripts\activate
        ```
    * **For macOS/Linux:**
        ```sh
        python3 -m venv venv
        source venv/bin/activate
        ```

4.  **Install the required packages from `req.txt`:**
    ```sh
    pip install -r req.txt
    ```

5.  **Run the application:**
    *Ensure your CSV data files are in the project's root directory.*
    ```sh
    python start.py
    ```

6.  Open your web browser and navigate to `http://127.0.0.1:8050/` to see the dashboard live.