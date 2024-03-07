# World Cup Matches Analysis: Spain's Performance

This project aims to analyze Spain's performance in FIFA World Cup matches to determine if Spain has improved or deteriorated over the years. The analysis focuses on various metrics, including the total number of wins and losses, average goals scored and conceded, as well as identifying Spain's most frequent opponents.

## Overview

Spain's performance in FIFA World Cup matches has been a subject of interest for football enthusiasts. This project delves into Spain's match data to provide insights into their performance trends, identifying key statistics and patterns.

## Data Collection and Cleaning

The data used in this analysis consists of FIFA World Cup match records. Only matches involving Spain are considered for analysis. Data cleaning involves standardizing column names, converting data types, and filtering rows to include only matches where Spain participated.

### Functions Used for Data Cleaning:

- `update_columns_to_lower`: A function used to convert column names to lowercase for consistency.
- `float_to_int`: A function used to convert float values to integers where applicable.

## Analysis

The analysis focuses on the following key metrics:

- Total number of wins and losses for Spain in World Cup matches.
- Average number of goals scored and conceded by Spain per match.
- Identification of opponents that Spain has beaten the most and those that have beaten Spain the most.

## Libraries Used

The project utilizes the following Python libraries for data analysis and visualization:

- pandas: For data manipulation and analysis.
- seaborn: For statistical data visualization.
- matplotlib: For creating plots and visualizations.

## Usage

To replicate the analysis or explore the data further, follow these steps:

1. Ensure you have Python installed on your system.
2. Install the required libraries using pip:

    ```
    pip install pandas seaborn matplotlib
    ```

3. Clone the repository:

    ```
    git clone https://github.com/spizzolante/project1
    ```

4. Navigate to the project directory:

    ```
    cd notebooks
    cd spain_analysis.ipynb
    ```

5. Run the analysis script:

    ```
    python spain_analysis.ipynb
    ```

6. View the generated visualizations and analysis results.

## Contributors

- [Sergio Pizzolante](https://github.com/spizzolante)

## License

No known licenses for this project.
