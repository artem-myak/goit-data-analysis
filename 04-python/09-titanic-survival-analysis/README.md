# Titanic: Exploratory Data Analysis & Survival Patterns

## Project Overview
This project is a comprehensive study of the Titanic passenger manifest using Python's data science stack (Pandas, Numpy, Matplotlib, Seaborn). The goal was to identify key factors that influenced survival rates, such as socio-economic status, age, and gender.

## Key Insights Discovered:
* **Gender Factor:** Female passengers had a significantly higher survival rate across all classes.
* **Class Impact:** Socio-economic status was a primary predictor, with 1st Class passengers prioritized during evacuation.
* **Demographics:** Analysis of the `who` column showed that children were also prioritized, consistent with the "women and children first" maritime protocol.
* **Missing Data:** Addressed significant gaps in the `age` and `deck` columns using imputation and filtering techniques.

## Technical Skills Applied:
* **Seaborn Datasets:** Working with built-in library data.
* **Data Cleaning:** Handling `NaN` values and dropping redundant columns (e.g., `alive` vs `survived`).
* **Statistical Visualization:** * Categorical plots (Boxplots, Barplots) for class-based analysis.
    * Distribution plots (Histograms, KDE) for age and fare analysis.
    * Heatmaps to identify correlations between numerical features.

🔗 **Live Version:** [Google Colab/Jupyter Link](https://colab.research.google.com/drive/1kD3bePhC2_YCmH6umOrpdjvGHfNI9Pf2?usp=sharing)

Note: This project was completed as part of the GoIT Data Analysis course.
