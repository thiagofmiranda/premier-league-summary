# Premier League Summary Application

This project is a Streamlit application designed to summarize and visualize results from the Premier League using match statistics. It provides insights into match performance, team standings, and other relevant metrics.

## Project Structure

```
premier-league-summary
├── app.py                  # Main entry point for the Streamlit application
├── data
│   ├── df_matches_results_stats.parquet  # Detailed match statistics
│   └── df_matches_results_sumstats.parquet # Summarized match statistics
├── tabs
│   ├── general_results.py  # Tab for general league results
│   ├── team_results.py     # Tab for team-specific results
│   └── about_me.py         # Tab with author information
├── utils
│   ├── data_loader.py      # Utility functions for loading and processing data
│   ├── plot_loader.py      # Utility functions for generating visualizations
│   └── css_loader.py       # Utility for loading custom CSS styles
├── static
│   ├── img/                # Images used in the dashboard
│   └── styles/             # CSS styles for the application
├─── .streamlit
│   └── config.toml         # Streamlit layout configuration
├── requirements.txt        # Project dependencies
└── README.md               # Project documentation
```

## Features

- **General Results**: View overall league statistics, including team standings, points, goals, and more.
- **Team Results**: Explore detailed statistics for specific teams, including match performance and trends.
- **About Me**: Learn more about the author and the purpose of the dashboard.
- **Interactive Filters**: Customize the data displayed by selecting specific teams, matches, or metrics.
- **Visualizations**: Generate dynamic charts and tables for better insights.

## Installation

1. Clone the repository:
   ```bash
   [git clone https://github.com/thiagofmiranda/premier-league-summary.git
   cd premier-league-summary
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Running the Application

To run the Streamlit application, execute the following command in your terminal:
```bash
streamlit run app.py
```

## Usage

- **Home Page**: Provides an overview of the dashboard and its features.
- **General Results Tab**: Displays league-wide statistics and rankings.
- **Team Results Tab**: (In development) Allows users to dive deeper into team-specific performance.
- **About Me Tab**: Contains information about the creator of the dashboard.

Once the application is running, open the provided URL in your browser to interact with the dashboard.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any suggestions or improvements.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.

## Acknowledgments

- Data sourced from [Flashscore](https://www.flashscore.com/).
