# Wikipedia Movie Data: Comprehensive EDA & Data Integration

## Project Overview
This project involves collecting, merging, and analyzing movie data hosted on GitHub (originating from Wikipedia). The primary challenge was to programmatically fetch multiple JSON files representing different eras and consolidate them into a single, unified dataset for exploratory data analysis.

## Data Source
The dataset used in this project is sourced from the [Wikipedia Movie Data repository](https://github.com/prust/wikipedia-movie-data/tree/master). It contains structured information about movies, including titles, years, cast, and genres.

## Key Technical Achievements:
* **Data Integration:** Automated the process of fetching and concatenating multiple remote JSON files using Pandas and URL string formatting.
* **Exploratory Data Analysis (EDA):** Analyzed movie production trends and genre popularity shifts over decades.
* **Data Transformation:** Managed nested JSON structures (cast and genres arrays) using data flattening techniques like `explode`.
* **Statistical Visualization:** Used Seaborn and Matplotlib to visualize the distribution of movies by year and genre.

## Deliverables
* `Movies_Analysis_Artem_Miakenkyi.ipynb`: Complete Jupyter Notebook with data fetching logic and visualization.

🔗 **Live Version:** [Google Colab/Jupyter Link](https://colab.research.google.com/drive/1z8UlQ3wMXyROISxPaEKCT3WPhwXrKOYn?usp=sharing)

Note: This project was completed as part of the GoIT Data Analysis course.
